import json
import string
from pathlib import Path
from urllib.request import urlopen

ACCENT = "mauve"


FLAVOUR_NAMES = {
    "latte": "Latte",
    "frappe": "Frappé",
    "macchiato": "Macchiato",
    "mocha": "Mocha",
}


def download(url, path):
    print(f"Downloading {url} to {path}")
    resp = urlopen(url)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as f:
        f.write(resp.read())


def palette():
    palette_path = Path(".cache/palette.json")

    if not palette_path.exists():
        url = "https://raw.githubusercontent.com/catppuccin/palette/main/palette-porcelain.json"
        download(url, palette_path)

    with palette_path.open() as f:
        return json.load(f)


template = string.Template(Path("template.tet").read_text())

for flavour, colours in palette().items():
    hexes = {name: v["hex"] for name, v in colours.items()}
    hexes["accent"] = hexes[ACCENT]
    path = Path("themes") / f"Catppuccin {FLAVOUR_NAMES[flavour]}.tet"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(template.substitute(hexes))
