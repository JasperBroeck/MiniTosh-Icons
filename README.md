# MiniTosh-Icons

> Minimal macOS-inspired icon theme based on the [Colloid icon theme by vinceliuice](https://github.com/vinceliuice/Colloid-icon-theme)

## About

**MiniTosh** is a lightweight, curated icon pack designed specifically for minimal Linux desktop environments (like Niri and Noctalia). 

Rather than bundling thousands of rarely-used system and file-type icons, MiniTosh focuses purely on a tight, cohesive set of high-impact **app icons**. 

### Transparency & Origins
This project is a derivative work built directly upon the foundation of [Colloid-icon-theme](https://github.com/vinceliuice/Colloid-icon-theme). To maintain a consistent minimalist aesthetic across my desktop, I took the base app icons from Colloid and performed targeted tweaks, color adjustments, and complete custom redesigns for select suites (such as the JetBrains IDEs and media applications). 

Some icons in this pack are pulled directly from Colloid as-is to ensure a complete fallback experience, while others are heavily modified or custom-built. All redistributed and modified code remains strictly under the terms of the original project's GNU General Public License v3.0.

## Install

To install MiniTosh locally on your system:

1. Clone or download this repository.
2. Move the `MiniTosh` folder into your local icons directory:
   ```bash
   mkdir -p ~/.local/share/icons
   cp -r MiniTosh ~/.local/share/icons/
   ```
3. Refresh your icon cache:
   ```bash
   gtk-update-icon-cache -f ~/.local/share/icons/MiniTosh
   ```
4. Apply **MiniTosh** using your desktop environment's appearance settings or shell configuration.

## New icons?
You can follow the design rules withing the CONTRIBUTING.md file and design icons using the templates. Export them as .svg and make a PR or issue and share them. You can also just ask for certain icons by adding an issue.

## Next Up?

- [ ] fedora media writer
