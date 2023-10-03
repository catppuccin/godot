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

BASE_REDS = {
    "latte": "#e8b9c6",
    "frappe": "#5e4856",
    "macchiato": "#563f51",
    "mocha": "#53394d",
}

PIN = "v0.2.0"
URL = f"https://github.com/catppuccin/palette/blob/{PIN}/palette-porcelain.json?raw=1"


def download(url, path):
    print(f"Downloading {url} to {path}")
    resp = urlopen(url)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as f:
        f.write(resp.read())


def palette():
    palette_path = Path(".cache/palette.json")

    if not palette_path.exists():
        download(URL, palette_path)

    with palette_path.open() as f:
        return json.load(f)


template = string.Template(Path("template.tet").read_text())

for flavour, colours in palette().items():
    hexes = {name: v["hex"] for name, v in colours.items()}
    hexes["accent"] = hexes[ACCENT]
    hexes["base_red"] = BASE_REDS[flavour]
    path = Path("themes") / f"Catppuccin {FLAVOUR_NAMES[flavour]}.tet"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(template.substitute(hexes))
