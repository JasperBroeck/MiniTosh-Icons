<!--
<p align="center">
  <img src="icons/logo.svg" width="128" alt="MiniTosh logo">
</p>
-->

# MiniTosh-Icons

> Minimal macOS-inspired icon theme based on the [Colloid icon theme by vinceliuice](https://github.com/vinceliuice/Colloid-icon-theme)

## About

**MiniTosh** is a lightweight, curated icon pack designed specifically for minimal Linux desktop environments (like Niri and Noctalia).

Rather than bundling thousands of rarely-used system and file-type icons, MiniTosh focuses purely on a tight, cohesive set of high-impact **app icons**. Everything else (folders, file types, status and action icons) is inherited from [Adwaita](https://gitlab.gnome.org/GNOME/adwaita-icon-theme).

### Transparency & Origins

This project is a derivative work built directly upon the foundation of [Colloid-icon-theme](https://github.com/vinceliuice/Colloid-icon-theme). To maintain a consistent minimalist aesthetic across my desktop, I took the base app icons from Colloid and performed targeted tweaks, color adjustments, and complete custom redesigns for select suites (such as the JetBrains IDEs and media applications).

Some icons in this pack are pulled directly from Colloid as-is to ensure a complete fallback experience, while others are heavily modified or custom-built. All redistributed and modified work remains strictly under the terms of the original project's GNU General Public License v3.0.

## Install

### Quick install (recommended)

Clone the repository straight into your local icons directory:

```bash
mkdir -p ~/.local/share/icons
cd ~/.local/share/icons
git clone https://github.com/JasperBroeck/MiniTosh-Icons.git
```

That's it. The extra repository files (README, templates, ...) are harmless, and updating later is just:

```bash
cd ~/.local/share/icons/MiniTosh-Icons
git pull
```

### Manual install

If you'd rather not keep the git history:

1. Clone or download this repository.
2. Copy the folder into your local icons directory:
   ```bash
   mkdir -p ~/.local/share/icons
   cp -a MiniTosh-Icons ~/.local/share/icons/
   ```
3. *(Optional)* Refresh the icon cache:
   ```bash
   gtk-update-icon-cache -f ~/.local/share/icons/MiniTosh-Icons
   ```

### Apply the theme

Select **MiniTosh** in your desktop environment's appearance settings (for example GNOME Tweaks) or in your shell configuration. You may need to restart running apps, or log out and back in, before every icon updates.

## Missing an icon?

- **Want to design one?** Follow the design rules in [CONTRIBUTING.md](CONTRIBUTING.md) and start from the files in [`templates/`](templates/). Export your icon as `.svg` and share it through a pull request or an issue.
- **Just want one added?** Open an issue and tell me which app you're missing.
- **App installed but showing the wrong icon?** It's probably asking for a different icon name. CONTRIBUTING.md explains how to find it and add a link.

## License

GPL-3.0, inherited from Colloid. See [LICENSE](LICENSE).
