import requests, json, os, sys

HEADERS = {"User-Agent": "WhosBetterApp/1.0 (research/demo project; contact: majki.btako@gmail.com)"}

PLAYERS = [
    ("messi", "Lionel Messi"),
    ("dibu", "Emiliano Martínez"),
    ("julian", "Julián Álvarez"),
    ("deniro", "Enzo Fernández"),
    ("mbappe", "Kylian Mbappé"),
    ("griezmann", "Antoine Griezmann"),
    ("tchouameni", "Aurélien Tchouaméni"),
    ("dembele", "Ousmane Dembélé"),
    ("bellingham", "Jude Bellingham"),
    ("kane", "Harry Kane"),
    ("foden", "Phil Foden"),
    ("saka", "Bukayo Saka"),
    ("vinicius", "Vinícius Júnior"),
    ("rodrygo", "Rodrygo"),
    ("raphinha", "Raphinha"),
    ("casemiro", "Casemiro"),
    ("ronaldo", "Cristiano Ronaldo"),
    ("bfernandes", "Bruno Fernandes"),
    ("cancelo", "João Cancelo"),
    ("neymar", "Neymar"),
]

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "images", "players")
os.makedirs(OUT_DIR, exist_ok=True)

def get_pageimage(title, size=1200):
    r = requests.get("https://en.wikipedia.org/w/api.php", params={
        "action": "query", "titles": title, "prop": "pageimages",
        "piprop": "thumbnail|name", "pithumbsize": size, "format": "json", "redirects": 1
    }, headers=HEADERS, timeout=20)
    r.raise_for_status()
    pages = r.json()["query"]["pages"]
    page = next(iter(pages.values()))
    thumb = page.get("thumbnail", {}).get("source")
    pi = page.get("pageimage")
    return thumb, pi, page.get("title")

def get_license(filename):
    if not filename:
        return None
    r = requests.get("https://commons.wikimedia.org/w/api.php", params={
        "action": "query", "titles": f"File:{filename}", "prop": "imageinfo",
        "iiprop": "extmetadata", "format": "json"
    }, headers=HEADERS, timeout=20)
    r.raise_for_status()
    pages = r.json()["query"]["pages"]
    page = next(iter(pages.values()))
    ii = page.get("imageinfo")
    if not ii:
        return None
    meta = ii[0].get("extmetadata", {})
    def g(k):
        return meta.get(k, {}).get("value", "")
    return {
        "license": g("LicenseShortName"),
        "artist": g("Artist"),
        "credit": g("Credit"),
    }

results = []
for pid, title in PLAYERS:
    try:
        thumb, pi, resolved_title = get_pageimage(title)
        if not thumb:
            print(f"MISSING: {pid} ({title}) - no pageimage found")
            results.append({"id": pid, "title": title, "status": "missing"})
            continue
        lic = get_license(pi)
        results.append({"id": pid, "title": resolved_title, "thumb": thumb, "file": pi, "license": lic, "status": "ok"})
        print(f"OK: {pid} -> {pi} | {lic}")
    except Exception as e:
        print(f"ERROR: {pid} ({title}) - {e}")
        results.append({"id": pid, "title": title, "status": "error", "error": str(e)})

with open(os.path.join(OUT_DIR, "_meta.json"), "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("\nDone. Meta saved.")
