import requests, json, os
from PIL import Image
from io import BytesIO

HEADERS = {"User-Agent": "WhosBetterApp/1.0 (research/demo project; contact: majki.btako@gmail.com)"}
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "images", "players")

TARGET_W, TARGET_H = 720, 960  # 3:4 portrait, high quality for mobile

with open(os.path.join(OUT_DIR, "_meta.json"), encoding="utf-8") as f:
    players = json.load(f)

credits = []
for p in players:
    if p["status"] != "ok":
        print(f"SKIP {p['id']}: {p['status']}")
        continue
    r = requests.get(p["thumb"], headers=HEADERS, timeout=30)
    r.raise_for_status()
    img = Image.open(BytesIO(r.content)).convert("RGB")

    # center-crop to target aspect ratio, then resize
    src_ratio = img.width / img.height
    target_ratio = TARGET_W / TARGET_H
    if src_ratio > target_ratio:
        # too wide -> crop width
        new_w = int(img.height * target_ratio)
        x0 = (img.width - new_w) // 2
        img = img.crop((x0, 0, x0 + new_w, img.height))
    else:
        # too tall -> crop height (bias slightly toward top, keeps faces)
        new_h = int(img.width / target_ratio)
        y0 = max(0, int((img.height - new_h) * 0.25))
        img = img.crop((0, y0, img.width, y0 + new_h))

    img = img.resize((TARGET_W, TARGET_H), Image.LANCZOS)
    out_path = os.path.join(OUT_DIR, f"{p['id']}.jpg")
    img.save(out_path, "JPEG", quality=90)
    print(f"SAVED {p['id']}.jpg ({TARGET_W}x{TARGET_H})")

    lic = p.get("license") or {}
    credits.append({
        "id": p["id"],
        "wikipedia_article": p["title"],
        "commons_file": p["file"],
        "license": lic.get("license"),
    })

with open(os.path.join(OUT_DIR, "CREDITS.json"), "w", encoding="utf-8") as f:
    json.dump(credits, f, indent=2, ensure_ascii=False)

print(f"\nDone. {len(credits)} images processed.")
