![nbiff logo](doc/logo.png) 

# Table of contents

**TODO** Recreate this

# nbiff

`nbiff` is an intentionally simple, extensible systray email
notifier. Geared for Linux, yet it may (eventually) work on Windows.

## Features

`nbiff` has the following features:

- It is dynamic.  It self-adjusts when email accounts are
  added/deleted and folders are created/deleted.
- While dynamic, it is designed to be light-weight and quick.
- Largely it is immune from `Thunderbird`'s API changes.
- Supports both `x11` and `wayland`.
- Users can customize their own systray icons.
- The systray icon provides high-level information such as whether
  there are unread messages or not.
- Details are presented by clicking on the icon.  Tool tips are
  available when the environment supports it.

## Online help

For online help, join the `nbiff`
[subreddit](https://www.reddit.com/r/nbiff).

## nbiff requirements

> Link [on github](https://github.com/pablo-blueoakdb/nbiff#nbiff-requirements)

`Python 3` is required along with some additional libraries:

```shell
pip3 install PyQt5 psutil
```

You may need to install `pip3` (or try `pip`).

### GNOME + Wayland support

> Link [on github](https://github.com/pablo-blueoakdb/nbiff#gnome--wayland-support)

Some **GNOME** versions require the `KStatusNotifierItem/AppIndicator
Support` extension for **Wayland** support.

Install it as follows:

1. [Go to the extension's webpage](https://extensions.gnome.org/extension/615/appindicator-support).
2. [Enable](https://github.com/pablo-blueoakdb/nbiff/blob/main/doc/KStatusNotifierItem.png)
   the extension by moving the slider to the **On** position.

## Installing / Upgrading

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
| `thunderbird` | <pre lang="shell">./Install_latest.tbird</pre> |

### Known quirks

#### Thunderbird

There are rare times when, it appears that an `.msf` is not
immediately flushed to disk.  This causes `nbiff` to believe there are
 **Unread messages** when there are none. 

Within a two or three minutes, `thunderbird` synchronizes the disk
file and all is well.

There are two possible work-arounds:

1. Restart `thunderbird` or
2. Use `tbird_new_msgs` to identify which `.msf` is out of sync.  Once
   identified, click on it and `thunderbird` will syncrhornize it.

   To read more about about `tbird_new_msgs`, [see the Troubleshooting
   section](#Troubleshooting).

## Temporarily disabling autorun

There may be times when it is desired to not run `nbiff` and leave it
configured to autorun.

Edit `$HOME/.nbiff/local/conf/nbiff.conf` and define the following variable:

```shell
DISABLE="stop you"
```

To renable, either comment out the variable (prefix it with `#`) or
delete it and manually restart `nbiff`.

## Custom icons

### Local icon directory

Local icons can be placed in `$HOME/.nbiff/local/icons`.

Once local icons are used, it is an all-or-nothing.  That is, `nbiff`
will be told to pull all its icons from the local directory.

For convenience, this directory is seeded with symbolic links to
several `nbiff`'s core icons.

The symbolic links makes it easy to mix-and-match one or more of the
`nbiff` icons with local changes.

In addition to the symbolic links, the sample file `unread_msgs.png`
file is included.

It is referenced in the commented code fragment found in the [Local
nbiff.conf](#Local_nbiffconf) file.

### Local nbiff.conf

`$HOME/.nbiff/local/conf/nbiff.conf` contains icon site-localizations.

To simplify implementation, the following code fragment is included:

```shell
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Use local icons
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# See the README.md on how to enable local icons.
#
# In the example below, only one icon is localized:
#
#    ICON_UNREAD_MSGS="unread_msgs.png"
#
#ICONS_DIR="../local/icons"
#ICON_UNREAD_MSGS="unread_msgs.png"
#ICON_NO_UNREAD_MSGS="01.no_unread_msgs.png"
#ICON_ERROR="01.error.png"
#ICON_MUA_IS_DOWN="01.MUA_is_down.png"
```

#### Affecting changes

After each change, restart `nbiff`:

1. Click on the systray icon and select the menu item `quit`.
2. Start it:

```shell
$HOME/.nbiff/systray/Run_nbiff nbiff_qt5.py &
```

#### Start using the local icon directory

Uncomment `ICONS_DIR` to start using the local icon directory:

```shell
ICONS_DIR="../local/icons"
```

At this point, the symbolic links in this directory are used to point
to the base `nbiff` icons.  That is, `nbiff` will continue to use the
configured icons.

#### Use the sample icon

As mentioned in the [Local icon directory](#local-icon-directory)
section, a sample file named `unread_msgs.png` is provided at
install. 

```shell
ICON_UNREAD_MSGS="unread_msgs.png"
```

## Troubleshooting

## Uninstalling

## Setting autorun



## Developing

**TODO**

Here's a brief intro about what a developer must do in order to start developing
the project further:

```shell
git clone https://github.com/your/awesome-project.git
cd awesome-project/
packagemanager install
```

### Icon development

To contribute to the `nbiff` icons, see the documentation on [icon
development](src/icons/README.md).

To make it easy:

1. Upload your images to an image sharing website (e.g. https://imgur.com)
2. [Create a new
   issue](https://github.com/pablo-blueoakdb/nbiff/issues/new) and
   reference the images.

### Architectural overview

High-level, there are two components:

1. The **unread messages** engine and
2. The **systray** visualizer.

**systray** runs a supplied program.  It ignores all lines but those
with the string **Unread count = N**  It updates the systray icon and
menu based on **N**.

The **Thunderbird unread messages** code runs asynchronously from
**Thunderbird**.  It only dependents on the format of the .msf flies.
This avoids issues that others encounter with refactoring of the APIs
and such.

The script is written to be performant.  It tries to be clever in how
it does its work:

- Tracking updates to .msfs since the last iteration to process the
  minimum number between each iteraton
- By processing .msfs bottom-up and halting the scan as quickly as
  possible, it is largely unaffected by the size of the .msf

## Development configuration
The base software supports running multiple instances of `nbiff`.
Furthermore, the source tree supports the existence of a **dev**
directory structure at the top-levl of the proejct tree:

```
dev
└── conf
    ├── nbiff.conf
    └── tbird_new_msgs.conf
```

Populate it the the corresponding `...src/conf/*.conf` file and suit
to taste.

## Contributing

**TODO**

When you publish something open source, one of the greatest motivations is that
anyone can just jump in and start contributing to your project.

These paragraphs are meant to welcome those kind souls to feel that they are
needed. You should state something like:

"If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome."

If there's anything else the developer needs to know (e.g. the code style
guide), you should link it here. If there's a lot of things to take into
consideration, it is common to separate this section to its own file called
`CONTRIBUTING.md` (or similar). If so, you should say that it exists here.

## Links

**TODO**

Even though this information can be found inside the project on machine-readable
format like in a .json file, it's good to include a summary of most useful
links to humans using your project. You can include links like:

- Project homepage: https://your.github.com/awesome-project/
- Repository: https://github.com/your/awesome-project/
- Issue tracker: https://github.com/your/awesome-project/issues
  - In case of sensitive bugs like security vulnerabilities, please contact
    my@email.com directly instead of using issue tracker. We value your effort
    to improve the security and privacy of this project!
- Related projects:
  - Your other project: https://github.com/your/other-project/
  - Someone else's project: https://github.com/someones/awesome-project/

## Future

**TODO**

* Create a **package** rather than using an installation script.
* Potentially provide Windows support.  To handle spaces in
  file/directory names (almost all?) variables are double quoted.
  `bash` (and other tools such as `rsync`) would be required.

  If there is sufficient demand ...
* Extend `nbiff` to `minimize` the mail client.
* Provide localization.

## Licensing

The code in this project is licensed under MIT license.
