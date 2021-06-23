## Table of contents

- [Customizing `nbiff`](#customizing-nbiff)
- [General strategy](#general-strategy)
- [Customization directory](#customization-directory)
- [Customizing `tbird_new_msgs`](#customizing-tbird_new_msgs)
  - [Local `tbird_new_msgs.conf`](#local-tbird_new_msgsconf)
- [Customizing icons](#customizing-icons)
  - [The local icon directory](#the-local-icon-directory)
    - [Protecting local icons from deletion](#protecting-local-icons-from-deletion)
  - [The local `nbiff.conf` file](#the-local-nbiffconf-file)
    - [Previewing changes](#previewing-changes)
    - [Affecting changes](#affecting-changes)
    - [Enable the local icon directory](#enable-the-local-icon-directory)
    - [Local icon example](#local-icon-example)

## Customizing `nbiff`

`nbiff` can be customized to:

* To use one or more different systray icons,
* Always ignore unread messages from a folder tree/name.

## General strategy

`nbiff` uses shell variables to store its **core** configuration
information.   Its configuration files are in `~/.nbiff/conf/`.

Customization involves re-defining the same variables in corresonding
files found in `~/.nbiff/local/{conf,icons}/`.

`nbiff` executes as follows:

1. Load the core configuration.
2. Load any corresponding local configuration which may redefine any
   previously defined **core** variables.

As an example, suppose the **core** configuration defined `A="woof"`
In the local file, it can be redefined as `A="purr"`

## Customization directory

`$HOME/.nbiff/local` has two subdirectories for customizations:

* `conf` - override one or more `nbiff` parameters.
* `icons` - icon customizations.

At install, these directories are seeded with sample data.  They will
never be overwritten during an upgrade.

## Customizing `tbird_new_msgs`

### Local `tbird_new_msgs.conf`

`tbird_new_msgs`'s configuration file provides extensive
documentation.  The following variables are available customizing:

| Variable name            | Description                                                     |
|--------------------------|-----------------------------------------------------------------|
| `TBIRD_DIR`              | The `Thunderbird` profile directory.                            |
| `USER_MSF_EXCLUSIONS`    | Name of `.msf`s to ignore.                                      |
| `TLF_MSF_EXCLUSIONS`     | Top-level folder tree to ignore.                                |
| `DEFAULT_SBD_EXCLUSIONS` | The default folder tree name to ignore.  Rarely needs tweaking. |
| `DEFAULT_MSF_EXCLUSIONS` | The default set of `.msf`'s to ignore (e.g. `Trash`)            |

## Customizing icons

### The local icon directory

Local icons can be placed in `~/.nbiff/local/icons` along with
symbolic links to the `nbiff` icons.

The symbolic links allow for customizing a subset of the `nbiff`
icons.

Over time, there will be more `nbiff` icons released and with each
release, new symbolic links will be created in
`~/.nbiff/local/icons`.

A sample icon file is included named `unread_msgs.png`.

It is referenced in the commented code fragment found in the [Local
nbiff.conf](#Local_nbiffconf) file.

#### Protecting local icons from deletion

The `nbiff` icons are all prefixed with a two-digit number.  During an
upgrade, all local icon file names matching this pattern are deleted
and resynchronized with the source tree.

> Never prefix your local icon with a two-digit number.  It will be
> deleted at the next upgrade.

### The local `nbiff.conf` file

`~/.nbiff/local/conf/nbiff.conf` contains icon site-localizations.

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
cd ~/.nbiff/systray
./Run_nbiff -f ../gen_new_msgs/Test/cycle_icons nbiff_qt5.py
```

`-f ../gen_new_msgs/Test/cycle_icons` instructs `nbiff` to run the
script `cycle_icons` instead of the configured script.  The curious
may wish to run the script on its own:

```shell
cd ~/.nbiff/gen_new_msgs/Test/
./cycle_icons
```

To stop running `nbiff`, use either CTRL-C or click on the systray
icon and `quit`.

#### Affecting changes

When done, restart `nbiff`:

1. Click on the systray icon and select the menu item `quit`.
2. Start it:

```shell
~/.nbiff/systray/Run_nbiff nbiff_qt5.py &
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
