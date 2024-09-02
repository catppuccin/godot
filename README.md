<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	Catppuccin for <a href="https://godotengine.org/">Godot</a>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>

<p align="center">
	<a href="https://github.com/catppuccin/godot/stargazers"><img src="https://img.shields.io/github/stars/catppuccin/godot?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
	<a href="https://github.com/catppuccin/godot/issues"><img src="https://img.shields.io/github/issues/catppuccin/godot?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
	<a href="https://github.com/catppuccin/godot/contributors"><img src="https://img.shields.io/github/contributors/catppuccin/godot?colorA=363a4f&colorB=a6da95&style=for-the-badge"></a>
</p>

<p align="center">
	<img src="assets/preview.webp"/>
</p>

## Previews

<details>
<summary>🌻 Latte</summary>
<img src="assets/latte.webp"/>
</details>
<details>
<summary>🪴 Frappé</summary>
<img src="assets/frappe.webp"/>
</details>
<details>
<summary>🌺 Macchiato</summary>
<img src="assets/macchiato.webp"/>
</details>
<details>
<summary>🌿 Mocha</summary>
<img src="assets/mocha.webp"/>
</details>

## Usage

> [!NOTE]
> This theme is for Godot 4. For Godot 3 support, use the [godot3 branch](https://github.com/catppuccin/godot/tree/godot3)

### Text Editor Theme

#### Official Collection

Catppuccin is available in the [Godot Syntax Themes repository](https://github.com/godotengine/godot-syntax-themes), installation instructions are in the readme.

#### Manual Installation

1. Download the [`.tet` files](themes/) for the flavour(s) you want into Godot's text editor themes directory:
	- Linux: `~/.config/godot/text_editor_themes/`
	- macOS: `~/Library/Application Support/Godot/text_editor_themes/`
	- Windows: `%APPDATA%\Godot\text_editor_themes\` 
	- Steam: `steamapps/common/Godot Engine/editor_data/text_editor_themes/`
2. In Godot, go to Editor → Editor Settings → Text Editor → Theme
3. Choose your flavour in the Color Theme dropdown.

### Interface Theme

1. In Godot, go to Editor → Editor Settings → Interface → Theme
2. Use the following settings:
	- Base Color:
		- Latte: `#eff1f5`
		- Frappé: `#303446`
		- Macchiato: `#24273a`
		- Mocha: `#1e1e2e`
	- Accent:
		- Latte: `#8839ef`
		- Frappé: `#ca9ee6`
		- Macchiato: `#c6a0f6`
		- Mocha: `#cba6f7`
	- Contrast:
		- Latte: `0.06`
		- Mocha/Macchiato/Frappé: `0.2`
	- Icon Saturation:
		- Latte: `1.0`
		- Mocha/Macchiato/Frappé: `0.6`

## Customization

The text editor themes are generated from a [template file](godot.tera). You can customize the themes by editing the template file and running [catppuccin/whiskers](https://github.com/catppuccin/whiskers):

```shell
whiskers godot.tera
```

## 💝 Thanks to

- [Boranroni](https://github.com/boranroni)
- [backwardspy](https://github.com/backwardspy)

&nbsp;

<p align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" />
</p>

<p align="center">
	Copyright &copy; 2021-present <a href="https://github.com/catppuccin" target="_blank">Catppuccin Org</a>
</p>

<p align="center">
	<a href="https://github.com/catppuccin/catppuccin/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a>
</p>
