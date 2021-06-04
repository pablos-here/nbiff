![nbiff logo](doc/logo.png) 

## Table of contents

- [Features](#features)
- [Online help?](#online-help-)
- [Software requirements](#software-requirements)
  * [GNOME + Wayland support](#gnome---wayland-support)
- [Installing/Upgrading](#installing-upgrading)
  * [Known quirks](#known-quirks)
    + [Thunderbird](#thunderbird)
- [Setting up autostart](#setting-up-autostart)
  * [Temporarily disabling autostart](#temporarily-disabling-autostart)
- [Uninstalling](#uninstalling)
- [Links](#links)
  * [Related projects](#related-projects)
- [Customizing icons](#customizing-icons)
  * [Local icon directory](#local-icon-directory)
  * [Local nbiff.conf](#local-nbiffconf)
    + [Previewing changes](#previewing-changes)
    + [Affecting changes](#affecting-changes)
    + [Enable the local icon directory](#enable-the-local-icon-directory)
    + [Local icon example](#local-icon-example)
- [Troubleshooting](#troubleshooting)
  * [Where to begin?](#where-to-begin-)
  * [No systray icon?](#no-systray-icon-)
  * [Still stuck?](#still-stuck-)
  * [High-level architecture](#high-level-architecture)
    + [gen_new_msgs](#gen-new-msgs)
    + [tbird_new_msgs](#tbird-new-msgs)
    + [Test suite](#test-suite)
    + [nbiff](#nbiff)
- [Developing](#developing)
  * [Icon development](#icon-development)
  * [Architectural overview](#architectural-overview)
  * [Development configuration](#development-configuration)
  * [Contributing](#contributing)
- [Future](#future)
- [Licensing](#licensing)

## nbiff

`nbiff`, [good, **new**
dawgy!](https://en.wikipedia.org/wiki/Biff_\(Unix\)), is
an intentionally simple, extensible systray email notifier. Geared for
Linux, yet it may (eventually) work on Windows.

## Features

`nbiff` has the following features:

- It is dynamic.
  - It self-adjusts when email accounts are added or
    deleted.
  - In real-time, it captures changes to the local folder structure.
- While dynamic, it is designed to be light-weight and quick.
  - It has been tested with over 1,000 `.msf`'s with no discernible
    performance degredation.
  - After the first iteration, the evaluation window is reduced to the
    last check thus the number of `.msf`'s does not affect **2..N**
    performance.
- Largely it is immune from `Thunderbird`'s API changes.
- Supports both `x11` and `wayland`.
- The systray icon provides both high-level and detailed information.
  - High-level, intuitive and subtle icon changes indicate status
    changess.
  - Details are presented by clicking on the icon.
  - Tool tips are available when supported by the user environment.
- User customizable systray icons.

## Online help?

For online help, join the `nbiff`
[subreddit](https://www.reddit.com/r/nbiff).

## Software requirements

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

## Installing/Upgrading

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

There are rare times when, it appears that an `.msf` is not
immediately flushed to disk.  This causes `nbiff` to believe there are
 **Unread messages** when there are none. 

Within a two or three minutes, `Thunderbird` synchronizes the disk
file and all is well.

There are two possible work-arounds:

1. Restart `Thunderbird` or
2. Use `tbird_new_msgs` to identify which `.msf` is out of sync.  Once
   identified, click on it and `Thunderbird` will syncrhornize it.

   To read more about about `tbird_new_msgs`, [see the Troubleshooting
   section](#Troubleshooting).

## Setting up autostart

Each [Desktop
environment](https://en.wikipedia.org/wiki/Desktop_environment) has
its own method to set up a program/script to start at login.

As **Desktop enviroments** continue to evolve, it is best to perform a
web-search that includes your environment
(e.g. [KDE](https://en.wikipedia.org/wiki/KDE),
[GNOME](https://en.wikipedia.org/wiki/GNOME), etc.) on how to start a
program/script at login.

### Temporarily disabling autostart

There may be times when it is desired to not run `nbiff` and leave it
configured to autostart.

Edit `$HOME/.nbiff/local/conf/nbiff.conf` and define the following variable:

```shell
DISABLE="stop you"
```

To renable, either comment out the variable (prefix it with `#`) or
delete it and manually restart `nbiff`.

## Uninstalling

1. Click on the systray icon and select the menu item `quit`.
2. If [autostart was set up](#setting-autostart), delete the entry.
3. Delete the code:
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

### Local icon directory

Local icons can be placed in `$HOME/.nbiff/local/icons` along with
symbolic links to the `nbiff` icons.

The symbolic links allow for customizing a subset of the `nbiff`
icons.

Over time, there will be more `nbiff` icons released and with each
release, new symbolic links will be created in
`$HOME/.nbiff/local/icons`.

The `nbiff` icons are all prefixed with a two-digit number.  To avoid
collisions, never use this naming pattern with local icons.

A sample icon file is included named `unread_msgs.png`.

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

#### Previewing changes

To preview changes, run `nbiff` as follows:

```shell
cd $HOME/.nbiff/systray
./Run_nbiff -f ../gen_new_msgs/Test/cycle_icons nbiff_qt5.py
```

`-f ../gen_new_msgs/Test/cycle_icons` instructs `nbiff` to run the
script `cycle_icons` instead of the configured script.  The curious
may wish to run the script on its own:

```shell
cd $HOME/.nbiff/gen_new_msgs/Test/
./cycle_icons
```

To stop running `nbiff`, use either CTRL-C or click on the systray
icon and `quit`.

#### Affecting changes

When done, restart `nbiff`:

1. Click on the systray icon and select the menu item `quit`.
2. Start it:

```shell
$HOME/.nbiff/systray/Run_nbiff nbiff_qt5.py &
```

#### Enable the local icon directory

To start using the local icon directory uncomment `ICONS_DIR`:

```shell
ICONS_DIR="../local/icons"
```

At this point `nbiff` is still using the configured
icons via the symbolic links.

#### Local icon example

As mentioned in the [Local icon directory](#local-icon-directory)
section, a sample file named `unread_msgs.png` is provided at
install.

To use it instead, uncomment the following:

```shell
ICON_UNREAD_MSGS="unread_msgs.png"
```

Restart `nbiff` and mark some messages `unread` to see the different icon.

## Troubleshooting

The sections below assume that you have read the [High-level
architecture](#high-level-architecture) section.

### Where to begin?

- Ensure that `nbiff` can create its icons independent of `gen_new_msgs`:
  - See [previewing changes](#previewing-changes).
  - Invoking `nbiff` using this method is independent of
    `gen_new_msgs`.
- Ensure that `gen_new_msgs` is working properly:
  - See [tbird_new_msgs](#tbird_new_msgs) on how to run the
    `Thunderbird` script in a terminal.

### No systray icon?

This will happen when `nbiff` cannot access its icons.

To troubleshoot this issue, change directories to the `systray`
directory and in a `bash` shell, load the respective configuration
files:

```
cd $HOME/.nbiff/systray
. ../Globals
. ../conf/nbiff.conf
```

Each `.` command will return silently if there are no errors.

Next, confirm that the directory variable is properly set.  The
command below will return the list of icons contained in the
directory:

```
ls -la $ICONS_DIR
```

The final step is to ensure each icon variable points to a file:

```
ls -la $ICONS_DIR/$ICON_UNREAD_MSGS
ls -la $ICONS_DIR/$ICON_NO_UNREAD_MSGS
ls -la $ICONS_DIR/$ICON_ERROR
ls -la $ICONS_DIR/$ICON_MUA_IS_DOWN
```

### Still stuck?

If you are stuck, get [online help](#online-help).

### High-level architecture

There are two high-level components for `nbiff`:

<pre>
    [ gen_new_msgs ] <-> [ nbiff ]
</pre>

Scripts in `gen_new_msgs` can be run standalone or are called by
`nbiff`.

`nbiff` is the data visualizer.  It reads the input from a
`gen_new_msgs` script and changes the systray icon accordingly.

#### gen_new_msgs

`$HOME/.nbiff/gen_new_msgs` stores the scripts/programs with the logic
to determine the count of unread messages for the mail client.

For testing purposes, multiple instances of it can be running.

#### tbird_new_msgs

`tbird_new_msgs` is tailored for `Thunderbird`.

For testing purposes, multiple instances of it can be running.

To run it:

```shell
cd $HOME/.nbiff/gen_new_msgs
./tbird_new_msgs
```

This is some [sample output](doc/sample_gen_new_msgs_output.png).

Use the argument `-?` to see its options:

```shell
./tbird_new_msgs '-?'
```

#### Test suite

Within the `gen_new_msgs/` is the `Test/` subdirectory.  These scripts
can be used to isolate issues and/or exercise `nbiff`'s icons.

This is an example of running oe of the scripts:

```shell
cd $HOME/.nbiff/gen_new_msgs/Test
./cycle_icons
```

This is [its output](doc/sample_cycle_icons_output.png).

#### nbiff

`nbiff` is the data visualizer.  It runs a script/program and
depending on the results, displays different systray icons.

It is designed to be invoked from any directory as it changes its
directory to the directory from where it is located.

Below is an example calling it to run the `nbiff_qt5.py` script:

```shell
cd $HOME/.nbiff/systray
$HOME/.nbiff/systray/Run_nbiff nbiff_qt5.py &
```

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

**TODO** potentially reference **high-level architecture?**

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

### Development configuration

**TODO*

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

### Contributing

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

## Future

* Create a **package** rather than using an installation script.
* Potentially provide Windows support.  To handle spaces in
  file/directory names (almost all?) variables are double quoted.
  `bash` (and other tools such as `rsync`) would be required.

  If there is sufficient demand ...
* Potentially extend `nbiff` to `minimize` the mail client.  This
  request may be an artifact of coming from an environment with a
  single **Desktop**.
* Provide localization.

## Licensing

The code in this project is licensed under MIT license.
