# Deepwick for Ptyxis

A deep navy terminal palette with Visual Studio 2022's syntax colors.

> Deepwick is an unofficial theme derived from
> [Polywick Blue](https://vscode.polywickstudio.net) by Polywick Studio (MIT).
> Not affiliated with Polywick Studio.

![Deepwick in Ptyxis](screenshot.png)

## Install

```sh
mkdir -p "${XDG_DATA_HOME:-$HOME/.local/share}/org.gnome.Ptyxis/palettes"
cp deepwick.palette "${XDG_DATA_HOME:-$HOME/.local/share}/org.gnome.Ptyxis/palettes/"
```

Or run `ptyxis --import-palette deepwick.palette`, which copies it to the
same directory (it refuses to overwrite an existing file).

For the Flathub build (`app.devsuite.Ptyxis`), run
`flatpak run app.devsuite.Ptyxis --import-palette deepwick.palette`, which
copies it to `~/.var/app/app.devsuite.Ptyxis/data/app.devsuite.Ptyxis/palettes/`.
Use `flatpak run --command=gsettings app.devsuite.Ptyxis` in place of
`gsettings` below; the schema names stay `org.gnome.Ptyxis`. (Flatpak steps
follow Ptyxis 50.1's source and the Flathub manifest; they were not run.)

## Activate

Open **Preferences → Appearance → Palette** and choose **Deepwick**, or set it
for your default profile from a shell:

```sh
gsettings set "org.gnome.Ptyxis.Profile:/org/gnome/Ptyxis/Profiles/$(gsettings get org.gnome.Ptyxis default-profile-uuid | tr -d "'")/" palette 'deepwick'
```

## Notes

- The superuser header bar (shown for `sudo`/`su` tabs) uses Red; the remote
  header bar (SSH) uses Magenta. Both use Background for text.
- Ptyxis does not support a custom selection color, so selection follows
  Ptyxis's default.

Tested with Ptyxis 50.1.

## License

MIT. See [LICENSE](LICENSE).
