# xdg-desktop-portal-termfilechooser

How to use:

- install the xdg-desktop-portal-termfilechooser bundle
- run `cf-termfilechooser-postinstall.sh`
- copy the wrapper you need to ~/.config/xdg-desktop-portal-termfilechooser
- edit `~/.config/xdg-desktop-portal-termfilechooser/config`:

```
[filechooser]
cmd=/home/$USER/.config/xdg-desktop-portal-termfilechooser/yazi-wrapper.sh
default_dir=/tmp

```
- check wrapper script for available terminal emulator


How to uninstall:

- remove the bundle: `swupd 3rd-party bundle-remove xdg-desktop-portal-termfilechooser`
- run `cf-termfilechooser-postinstall.sh`
