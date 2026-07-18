import os, json
import cv2
from PIL import Image

BASE = os.path.join(os.path.dirname(__file__), "..", "images", "players")
TARGET_W, TARGET_H = 720, 960

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

with open(os.path.join(BASE, "_meta.json"), encoding="utf-8") as f:
    players = json.load(f)

report = []

for p in players:
    if p["status"] != "ok":
        continue
    pid = p["id"]
    out_path = os.path.join(BASE, f"{pid}.jpg")

    # re-download original thumb fresh isn't necessary; we still have the
    # already-cropped 720x960 file, but we need the *pre-crop* source to
    # recenter properly. Re-fetch original thumbnail instead.
    import requests
    HEADERS = {"User-Agent": "WhosBetterApp/1.0 (research/demo project)"}
    r = requests.get(p["thumb"], headers=HEADERS, timeout=30)
    r.raise_for_status()
    tmp_path = os.path.join(BASE, f"_src_{pid}.jpg")
    with open(tmp_path, "wb") as f:
        f.write(r.content)

    cv_img = cv2.imread(tmp_path)
    gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))

    img = Image.open(tmp_path).convert("RGB")
    src_w, src_h = img.size
    target_ratio = TARGET_W / TARGET_H

    if len(faces) > 0:
        # pick the largest detected face
        fx, fy, fw, fh = max(faces, key=lambda f: f[2]*f[3])
        face_cx = fx + fw/2
        face_cy = fy + fh/2
        method = "face-detected"
    else:
        face_cx = src_w/2
        face_cy = src_h*0.32  # bias toward upper portion (typical headshot placement)
        method = "fallback-top-bias"

    # crop box at target aspect ratio, sized to fit within source, centered on face
    src_ratio = src_w/src_h
    if src_ratio > target_ratio:
        crop_h = src_h
        crop_w = int(crop_h*target_ratio)
    else:
        crop_w = src_w
        crop_h = int(crop_w/target_ratio)

    x0 = int(face_cx - crop_w/2)
    y0 = int(face_cy - crop_h*0.38)  # keep face in upper-third, room for shoulders below
    x0 = max(0, min(x0, src_w-crop_w))
    y0 = max(0, min(y0, src_h-crop_h))

    cropped = img.crop((x0, y0, x0+crop_w, y0+crop_h)).resize((TARGET_W, TARGET_H), Image.LANCZOS)
    cropped.save(out_path, "JPEG", quality=90)
    os.remove(tmp_path)

    report.append({"id": pid, "method": method, "faces_found": len(faces)})
    print(f"{pid}: {method} ({len(faces)} face(s))")

print("\nDone.")
