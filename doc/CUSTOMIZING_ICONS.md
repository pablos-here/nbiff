## Customizing icons

### The local icon directory

Local icons can be placed in `$HOME/.nbiff/local/icons` along with
symbolic links to the `nbiff` icons.

The symbolic links allow for customizing a subset of the `nbiff`
icons.

Over time, there will be more `nbiff` icons released and with each
release, new symbolic links will be created in
`$HOME/.nbiff/local/icons`.

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
