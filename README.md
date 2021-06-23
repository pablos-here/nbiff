![nbiff logo](doc/logo.png) 

## Table of contents

- [nbiff](#nbiff)
- [Features](#features)
- [Online help](#online-help)
- [Software requirements](#software-requirements)
  - [Wayland support on GNOME](#wayland-support-on-gnome)
- [Installing / upgrading](#installing--upgrading)
  - [Known quirks](#known-quirks)
    - [Thunderbird](#thunderbird)
- [Uninstalling](#uninstalling)
- [Links](#links)
  - [Related projects](#related-projects)
- [Customizing icons](#customizing-icons)
- [Troubleshooting](#troubleshooting)
- [Development](#development)

## nbiff

`nbiff`, [good **new**
dawgy!](https://en.wikipedia.org/wiki/Biff_\(Unix\)), is
an intentionally simple, extensible systray email notifier. Geared for
Linux, yet it may (eventually) work on Windows.

## Features

`nbiff` has the following features:

- It self-adjusts when accounts and/or folders are changed.
- It is designed to be light-weight and scalable.
- Largely it is immune from `Thunderbird`'s API changes.
- Supports both `x11` and `wayland`.
- The systray icon displays a status when there are **unread
  messages**.
- The **unread count** is provided by clicking on the icon and when
  supported, as a **tool tip**.
- User customizable systray icons.

## Online help

For online help, join the `nbiff`
[subreddit](https://www.reddit.com/r/nbiff).

## Software requirements

`Python 3` is required along with some additional libraries:

```shell
pip3 install PyQt5 psutil
```

You may need to install `pip3` (or try `pip`).

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
   release](https://github.com/pablo-blueoakdb/nbiff/releases).
2. Expand the release's **Assets** and download the compressed file of
   your choice.
3. After uncompressing the file, a new directory is created.  Change
   directories to it.
4. Run the installer for your email client and follow the on-screen
   instructions:

| Mail client   | Installation script                            |
|---------------|------------------------------------------------|
| `Thunderbird` | <pre lang="shell">./Install_latest.tbird</pre> |

### Known quirks

#### Thunderbird

It appears that there are rare conditions when an `.msf` is not immediately
flushed to disk.  This causes `nbiff` to believe there are **Unread
messages** when there are none.

There are several work-arounds:

1. Wait.  Within a two or three minutes, `Thunderbird` synchronizes
   the disk file and `nbiff` will note the change,
2. Restart `Thunderbird`,
3. Use `tbird_new_msgs` to identify which `.msf` is out of sync.  Once
   identified, click on it and `Thunderbird` will syncrhornize it.

   To read more about about `tbird_new_msgs`, see the [Troubleshooting
   section](#Troubleshooting).

The [issue](https://github.com/pablo-blueoakdb/nbiff/issues/2) is
being tracked.

## Uninstalling

1. Click on the systray icon and select the menu item `quit`.
2. Delete the code:
```shell
rm -rf $HOME/.nbiff
```

## Links

- [Software repository](https://github.com/pablo-blueoakdb/nbiff)
- [Project
  tracker](https://github.com/users/pablo-blueoakdb/projects/1)
- [Issue tracker](https://github.com/pablo-blueoakdb/nbiff/issues)

### Related projects

The following projects are `Thunderbird`-centric:

- [birdtray](https://github.com/gyunaev/birdtray)
- [systray-x](https://github.com/Ximi1970/systray-x)

## Customizing icons

To customize one or more of the default `nbiff` icons, see how to it
is done in [Customizing icons](doc/CUSTOMIZING_ICONS.md).

## Troubleshooting

Problems?  Head over to the [Troubleshooting](doc/TROUBLESHOOTING.md) document.

## Development

If you are interested in contributing, see the
[Development](src/README.md) document.
