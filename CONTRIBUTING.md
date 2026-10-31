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

## Design standards

Every MiniTosh icon follows the same shape and proportions so the pack feels consistent.

| Property | Value |
|---|---|
| Canvas | 64 × 64 px |
| Icon shape | 56 × 56 px, centered (4 px of empty space on every side) |
| Icon corner radius | 13 px |
| Center guide (circle) | 40 px diameter, dead center |
| Center guide (rounded square) | 40 × 40 px, corner radius 6 px, dead center |

The circle is only a visual aid. The rounded square is the one to follow.

### Placing a logo

Keep important elements, such as a centered logo, inside the 40 × 40 px rounded square.

- **Default:** scale the logo so its largest dimension is **40 px**, then center it.
- **Logos with sharp corners or square edges:** these look larger than round logos at the same size, so scale them down a little. **38 px** is usually enough. Only go smaller if it's really necessary.
- Going slightly outside the rounded square is fine. Just don't push important parts of the logo toward the edge of the icon.

Using an app's official logo in an icon is welcome. Logos and trademarks remain the property of their respective owners.

### Using the template

1. Start from one of the files in [`templates/`](https://github.com/JasperBroeck/MiniTosh-Icons/tree/main/templates) in any SVG-compatible editor (Inkscape, Figma, Penpot, ...).
2. Use the helper grid in the template while designing.
3. **Delete the grid** from your file once the icon is finished.
4. Save the result as a clean, plain `.svg` file. Other formats, including `.svgz`, are not accepted.

## Adding a new icon

Place the base icon in `apps/scalable/`.

- Use **only lowercase letters, numbers and dashes**: `visual-studio-code.svg`, not `Visual Studio Code.svg`.
- Keep **one base file per app**. Alternative names belong in `links/` (see below), not here.

Then submit it in one of two ways:

- **Pull request:** add the SVG and include the app name, what it's used for and a link to the app.
- **Issue:** attach the `.svg` file with the same information. We'll review it and add it if it fits the style of the pack.

Icons need to follow the [design standards](#design-standards) to be accepted. If you're unsure, open an issue first.

## Adding a link (when an icon doesn't show up)

Test your icon locally before submitting. Many apps find their icon straight away, but some look for a different name than the one you chose. When that happens, add a symlink in `apps/scalable/links/`. This keeps `apps/scalable/` readable while still supporting every name an app asks for.

### 1. Find the name the app wants

Look at the app's `.desktop` file:

```bash
grep '^Icon=' /usr/share/applications/<app>.desktop
```

For Flatpaks, check `/var/lib/flatpak/exports/share/applications/` (system) or `~/.local/share/flatpak/exports/share/applications/` (user). Some apps also store their `.desktop` files in `~/.local/share/applications/`. The value after `Icon=` is the exact name the app requests. Flatpak apps usually use their app ID, e.g. `org.gnome.Nautilus`.

### 2. Create the link

From inside `apps/scalable/links/`:

```bash
ln -s ../base-name.svg requested-name.svg
```

**Example:** the app requests `org.gnome.Nautilus` and the base icon is `file-manager.svg`:

```bash
ln -s ../file-manager.svg org.gnome.Nautilus.svg
```

### Link rules

- **Relative links only.** Always start the target with `../`. Absolute paths break for everyone else.
- **Copy the requested name exactly.** Icon names are case-sensitive, so some links are intentionally capitalised (for example `Alacritty.svg` and `Nextcloud.svg`, which point to `alacritty.svg` and `nextcloud.svg`). Don't "fix" those.
- **Never create a link with the same name as an existing file in `apps/scalable/`.** Names are case-sensitive.
- Check for broken links before committing. Run this from the root of the repository; it should print nothing:

  ```bash
  find apps -xtype l
  ```

## Reporting a problem

Open an issue and include:

- The name of the app
- The `Icon=` value from its `.desktop` file (see [Find the name the app wants](#1-find-the-name-the-app-wants))
- Where it's installed from (native package, Flatpak, Snap, ...)
- A screenshot, if the problem is how an icon looks

## Testing locally

Copy or link the repo into your icon folder, then restart the app (or log out and in) to see changes:

```bash
ln -s /PATH/TO/MiniTosh-Icons ~/.local/share/icons/MiniTosh
```

Then select **MiniTosh** in GNOME Tweaks (or your desktop's appearance settings).

## Checklist before opening a PR

- [ ] The icon follows the [design standards](#design-standards)
- [ ] SVG is clean, saved as plain `.svg`, and the helper grid has been removed
- [ ] Base icon is in `apps/scalable/` with a lowercase-dash name
- [ ] Any (optional) extra names are relative symlinks in `apps/scalable/links/`
- [ ] The icon shows up correctly in the real app
- [ ] `find apps -xtype l` reports no broken links

## License

By submitting an icon, you agree to license it under the same license as this repository.
