# Contributing to MiniTosh

Thanks for helping out! MiniTosh is an app-icon theme for Linux. Everything that isn't an app icon is inherited from Adwaita, so only application icons belong here.

There are three ways to contribute:

1. **Add a new icon** (pull request or issue)
2. **Add a missing link** for an app that doesn't pick up its icon
3. **Report a problem** (wrong icon, bad rendering, wrong name)

## Repository layout

```
apps/scalable/          Base icons only, one SVG per app
apps/scalable/links/    Relative symlinks to base icons (alternative names)
templates/              Starter SVGs with a helper grid
```

## Designing an icon

1. Start from one of the files in [`templates/`](https://github.com/JasperBroeck/MiniTosh-Icons/tree/main/templates) using any SVG-compatible editor (Inkscape, Figma, Penpot, ...).
2. Use the helper grid in the template while designing.
3. **Delete the grid** from the file once the icon is finished.
4. Save the result as a clean, plain `.svg`.

## Adding a new icon

Place the base icon in `apps/scalable/`.

- Use **only lowercase letters, numbers and dashes**: `visual-studio-code.svg`, not `Visual Studio Code.svg`.
- Keep **one base file per app**. Alternative names belong in `links/` (see below), not here.

Then submit it in one of two ways:

- **Pull request:** add the SVG and include the app name, what it's used for and a link to the app.
- **Issue:** attach the `.svg` file with the same information. We'll review it and add it if it fits the style of the pack.

Icons need to follow the MiniTosh design standards to be accepted. If you're unsure, open an issue first.

## Adding a link (when an icon doesn't show up)

Test your icon locally before submitting. Many apps find their icon straight away, but some look for a different name than the one you chose. When that happens, add a symlink in `apps/scalable/links/`. This keeps `apps/scalable/` readable while still supporting every name an app asks for.

### 1. Find the name the app wants

Look at the app's `.desktop` file:

```bash
grep '^Icon=' /usr/share/applications/<app>.desktop
```

For Flatpaks, check `/var/lib/flatpak/exports/share/applications/` (system) or `~/.local/share/flatpak/exports/share/applications/` (user). The value after `Icon=` is the exact name the app requests. Flatpak apps usually use their app ID, e.g. `org.gnome.Nautilus`.

### 2. Create the link

From inside `apps/scalable/links/`:

```bash
ln -s ../base-name.svg requested-name.svg
```

Example:

```bash
ln -s ../file-manager.svg org.gnome.Nautilus.svg
```

### Link rules

- **Relative links only.** Always start the target with `../`. Absolute paths break for everyone else.
- **Copy the requested name exactly.** Icon names are case-sensitive, so `Alacritty.svg` and `Nextcloud.svg` are intentionally capitalised. Don't "fix" those.
- **Never reuse a name** that already exists in `apps/scalable/`.
- Check for broken links before committing: `find apps -xtype l` should print nothing.

## Testing locally

Copy or link the repo into your icon folder, then restart the app (or log out and in) to see changes:

```bash
ln -s /path/to/MiniTosh-Icons ~/.local/share/icons/MiniTosh
```

Then select **MiniTosh** in GNOME Tweaks (or your desktop's appearance settings).

## Checklist before opening a PR

- [ ] SVG is clean and the helper grid has been removed
- [ ] Base icon is in `apps/scalable/` with a lowercase-dash name
- [ ] Any extra names are relative symlinks in `apps/scalable/links/`
- [ ] The icon shows up correctly in the real app
- [ ] `find apps -xtype l` reports no broken links
