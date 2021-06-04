![nbiff logo](doc/logo.png) 

# Table of contents

- [nbiff](#nbiff)
  * [Features](#features)
  * [Online help](#online-help)
  * [nbiff requirements](#nbiff-requirements)
    + [GNOME + Wayland support](#gnome---wayland-support)
  * [Installing / Upgrading](#installing---upgrading)
    + [Known quirks](#known-quirks)
      - [Thunderbird](#thunderbird)
  * [Temporarily disabling autorun](#temporarily-disabling-autorun)
  * [Custom icons](#custom-icons)
    + [Local icon directory](#local-icon-directory)
    + [Local nbiff.conf](#local-nbiffconf)
      - [Affecting changes](#affecting-changes)
      - [Start using the local icon directory](#start-using-the-local-icon-directory)
      - [Use the sample icon](#use-the-sample-icon)
  * [Troubleshooting](#troubleshooting)
    + [No systray icon](#no-systray-icon)
    + [High-level architecture](#high-level-architecture)
      - [gen_new_msgs](#gen-new-msgs)
      - [tbird_new_msgs](#tbird-new-msgs)
      - [Test suite](#test-suite)
      - [nbiff](#nbiff-1)
  * [Uninstalling](#uninstalling)
  * [Setting autorun](#setting-autorun)
  * [Developing](#developing)
    + [Icon development](#icon-development)
    + [Architectural overview](#architectural-overview)
  * [Development configuration](#development-configuration)
  * [Contributing](#contributing)
  * [Links](#links)
  * [Future](#future)
  * [Licensing](#licensing)

# nbiff

`nbiff`, [good dawg!](https://en.wikipedia.org/wiki/Biff_\(Unix\)), is
an intentionally simple, extensible systray email notifier. Geared for
Linux, yet it may (eventually) work on Windows.

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

#### Enable local icon directory

To start using the local icon directory uncomment `ICONS_DIR`:

```shell
ICONS_DIR="../local/icons"
```

At this point `nbiff` is still using the configured
icons via the symbolic links.

#### Use the sample icon

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

### No systray icon?

This will happen when `nbiff` cannot access its icons.

To troubleshoot this issue, change directories to the `systray`
directory: 

```shell
cd $HOME/.nbiff/systray
```

Next, use the configuration files to define the variables in a shell.
Each `.` command will return silently if there are no errors:

```
bash
. ../Globals
. ../conf/nbiff.conf
```

Next, confirm that the directory variable is properly set:

```
ls -la $ICONS_DIR
```

Assuming so, the problem is with one or more of the icon variables.
To test them, do the following:

```
ls -la $ICONS_DIR/$ICON_UNREAD_MSGS
ls -la $ICONS_DIR/$ICON_NO_UNREAD_MSGS
ls -la $ICONS_DIR/$ICON_ERROR
ls -la $ICONS_DIR/$ICON_MUA_IS_DOWN
```

### Running gen_new_msgs

**TODO -- resume here ...**

### Running nbiff in test mode

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

#### tbird_new_msgs

`tbird_new_msgs` is tailored for `thunderbird`.  Multiple instances of
it can be running.

To run it:

```shell
cd $HOME/.nbiff/gen_new_msgs
./tbird_new_msgs
```

This is some [sample output](doc/sample_gen_new_msgs_output.png).

Use the argument `-?` to see its options:

```shell
./tbird_new_msgs '?'
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

It is designed to be invoked from any directory.

Below is an example calling it to run the `nbiff_qt5.py` script:

```shell
$HOME/.nbiff/systray/Run_nbiff nbiff_qt5.py &
```

During troublehshooting, it is easier to `cd $HOME/.nbiff/systray`.

## Uninstalling

1. Click on the systray icon and select the menu item `quit`.
2. If [autorun was set up](#setting-autorun), delete the entry.
3. Delete the code:
```shell
rm -rf $HOME/.nbiff
```

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
