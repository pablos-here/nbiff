![nbiff logo](doc/logo.png) 

## Table of contents

- [nbiff](#nbiff)
- [Features](#features)
- [Online help](#online-help)
- [Software requirements](#software-requirements)
  - [Python](#python)
  - [Additional packages](#additional-packages)
  - [Wayland support on GNOME](#wayland-support-on-gnome)
- [Installing / upgrading](#installing--upgrading)
- [Uninstalling](#uninstalling)
- [Mouse-clicks](#mouse-clicks)
  - [Desktop Environments](#desktop-environments)
  - [Xfce](#xfce)
  - [Swap mouse-click actions](#swap-mouse-click-actions)
- [Customizing](#customizing)
- [Troubleshooting](#troubleshooting)
- [Development](#development)

## nbiff

`nbiff`, [good **new**
dawgy!](https://en.wikipedia.org/wiki/Biff_\(Unix\)), is
an intentionally simple, extensible systray email notifier. Geared for
Linux, yet it may (eventually) work on Windows.

## Features

`nbiff` has the following features:

- It self-adjusts when accounts and/or folders are created/deleted.
- It is designed to be light-weight and scalable.
- Largely it is immune from `Thunderbird`'s API changes.
- Supports both `x11` and `wayland`.
- The systray icon displays a status when there are **unread
  messages**.
- Further details are available by clicking on the icon and when
  supported, as a **tool tip**.
- Use mouse-clicks to iconify/activate `Thunderbird` windows with
  smart (Virtual) desktop swapping.
- User customizable systray icons.

## Online help

For online help, join the `nbiff`
[subreddit](https://www.reddit.com/r/nbiff).

## Software requirements

### Python

`python3` is required along with some additional modules.  Choose
the desired method to install them:

| Method   | Information                                                  |
|----------|--------------------------------------------------------------|
| `pip`    | <pre lang="shell">pip3 install PyQt5 psutil</pre>            |
| Packages | <ul><li>python**X**-psutil</li><li>python**X**-qt5</li></ul> |
|          | where **X** matches the installed version of `Python`.       |

*Note:  Depending on your system, additional modules may be
required.  When `nbiff` is run, there must be no errors.*

### Additional packages

| Distro     | Packages                                                                                                                               |
|------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **Fedora** | <pre lang="shell">libX11-xcb libxcb xcb-util xcb-util-image xcb-util-keysyms xcb-util-renderutil xcb-util-wm</pre>                     |
| Others     | <pre lang="shell">ibxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0 libxcb-xkb1 libxkbcommon-x11-0 libxcb-xinerama0</pre> |

Optionally install `xdotool` for window iconifying/activation.

```shell
xdotool
```

### Wayland support on GNOME

Some **GNOME** versions require the `KStatusNotifierItem/AppIndicator
Support` extension for **Wayland** support.

Install it as follows:

1. [Go to the extension's webpage](https://extensions.gnome.org/extension/615/appindicator-support).
2. [Enable](https://github.com/pablo-blueoakdb/nbiff/blob/main/doc/KStatusNotifierItem.png)
   the extension by moving the slider to the **On** position.

## Installing / upgrading

The installation script handles installs and upgrades.

Below is how to install/upgrade:

1. [Get the latest the
   release](https://github.com/pablo-blueoakdb/nbiff/releases),
   uncompress the file and switch to the newly created directory.
2. Run the installer for your **email client** and follow the on-screen
   instructions:

   * `Thunderbird` <pre lang="shell">./Install_latest.tbird</pre>

## Uninstalling

1. Click on the systray icon and select the menu item `quit`.
2. Delete the code:
```shell
rm -rf ~/.nbiff
```

## Mouse-clicks

If the necessary package is installed, mouse-clicks on the systray
`nbiff` icon have actions.

The systray icon has at least one context-menu which display `nbiff`
data.  Typically it is accessed by a right-click or left-click.

In the table below, window activation is mentioned.  In this
documentation it means the following:

1. If needed, switch the desktop to where the main `Thunderbird`
   window is located.
2. If needed, de-iconify all of the `Thunderbird` windows.  Any
  children windows on the main desktop are de-iconified last so they
  stack above the parent. 

Using **KDE** as the gold standard, the following is supported:

| Mouse action | Result                                                                                                                                                   |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| click        | <ul><li>If not on the main `Thunderbird` window, activate it.</li><li>Otherwise, return to the original desktop.</li></ul>                               |
| middle-click | <ul><li>if not on main, activate.  Save the current desktop in case of **click**.</li><li>Otherwise, activate/iconify `Thunderbird` window(s).</li></ul> |

### Desktop Environments

As each **Desktop Environment** seems to implement mouse-clicks
differently, it is best to try the different mouse-click combinations
and see what happens ... :p

* left-click
* right-click
* double-click
* middle-click

### Xfce

The default **Status Tray Plugin** setting is to present an **Xfce**
configuration menu on one of the clicks.  Only middle-click is enabled
and it behaves like KDE's *click* (see above).

To enable proper (*opinion*) mouse clicks, uncheck the **Menu is
primary action**:

* Right-click on the `nbiff` systray icon to obtain the **Status Tray
  Plugin** menu. 
* Select **Properties**.
* In the **Status Tray Items** window, under **Features**, uncheck
  **Menu is primary action**.
  
To revert the setting:

* Right-click systray panel, **Panel -> Panel preferences ...**
* Click the **Items** tab
* Select **Status Tray Plugin (external)** and
* Click the **gear** at the bottom of the list
* Check **Menu is primary action**

### Swap mouse-click actions

View the current setting before switching the mouse-click acions:

```shell
fgrep SWAP_MOUSE_ACTION= ~/.nbiff/local/conf/nbiff.conf
```

If the line is preceded with an **#**, it is commented out.  The
system default applies.

To swap mouse-click actions - remove the **#**:

```shell
sed -i 's/^#SWAP_MOUSE_ACTION=/SWAP_MOUSE_ACTION=/' ~/.nbiff/local/conf/nbiff.conf
```

To restore the system default:

```shell
sed -i 's/^SWAP_MOUSE_ACTION=/#SWAP_MOUSE_ACTION=/' ~/.nbiff/local/conf/nbiff.conf
```

After making the above changes, restart `nbiff`.

## Customizing

The following can be customized:

* The systray icons.
* Always ignore **unread messages** from a folder tree/name.

Details can be found [here](doc/CUSTOMIZING.md).

## Troubleshooting

Problems?  Head over to the [Troubleshooting](doc/TROUBLESHOOTING.md) document.

## Development

If you are interested in contributing, see the
[Development](src/README.md) document.
