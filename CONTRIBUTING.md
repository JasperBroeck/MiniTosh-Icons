# Contributing to MiniTosh

First off, thank you for your interest in contributing to **MiniTosh**! Whether you are submitting a new app icon or requesting one, your help makes the project better.

Please follow these guidelines to keep the icon pack clean, consistent, and minimal.

---

## Designing New Icons

MiniTosh is built around a cohesive, minimalist, macOS-inspired **squircle (rounded square)** aesthetic with flat fills and clean geometry. 

When creating or modifying icons:
1. **Shape & Style:** Stick to a smooth squircle base geometry. Keep the design flat, clean, and modern to match the rest of the pack.
2. **Format:** Export all icons as scalable vector graphics (`.svg`).
3. **Location:** Place your SVGs inside the `MiniTosh/apps/scalable/` directory.
4. **Naming:** Name the file lowercase and match the application's desktop file name (e.g., `spotify.svg`, `discord.svg`, `obsidian.svg`).

---

## How to Submit a Pull Request

1. **Fork** the repository and create your branch from `main`.
2. Add or update your `.svg` files in `MiniTosh/apps/scalable/`.
3. Test your changes locally by copying your folder to `~/.local/share/icons/` and refreshing your icon cache:
   ```bash
   gtk-update-icon-cache -f ~/.local/share/icons/MiniTosh
