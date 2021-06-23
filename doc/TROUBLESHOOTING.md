## Table of contents

- [Troubleshooting](#troubleshooting)
- [Where to begin](#where-to-begin)
- [Missing or black systray icon](#missing-or-black-systray-icon)
- [Need more help?](#need-more-help)
- [High-level architecture](#high-level-architecture)
  - [gen_new_msgs](#gen_new_msgs)
  - [tbird_new_msgs](#tbird_new_msgs)
  - [Test suite](#test-suite)
  - [nbiff](#nbiff)

## Troubleshooting

The sections below assume that you have read the [High-level
architecture](#high-level-architecture) section.

## Where to begin

- Ensure that `nbiff` can create its icons independent of `gen_new_msgs`:
  - See [previewing changes](#previewing-changes).
  - Invoking `nbiff` using this method is independent of
    `gen_new_msgs`.
- Ensure that `gen_new_msgs` is working properly:
  - See [tbird_new_msgs](#tbird_new_msgs) on how to run the
    `Thunderbird` script in a terminal.

## Missing or black systray icon

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

## Need more help?

If you need help, it may be possible to get [online help](#online-help).

## High-level architecture

There are two high-level components for `nbiff`:

<pre>
    [ gen_new_msgs ] <-> [ nbiff ]
</pre>

Scripts in `gen_new_msgs` can be run standalone or are called by
`nbiff`.

`nbiff` is the data visualizer.  It reads the input from a
`gen_new_msgs` script and changes the systray icon accordingly.

### gen_new_msgs

`$HOME/.nbiff/gen_new_msgs` stores the scripts/programs with the logic
to determine the count of unread messages for the mail client.

For testing purposes, multiple instances of it can be running.

### tbird_new_msgs

`tbird_new_msgs` is tailored for `Thunderbird`.

For testing purposes, multiple instances of it can be running.

To run it:

```shell
cd $HOME/.nbiff/gen_new_msgs
./tbird_new_msgs
```

This is some [sample output](sample_gen_new_msgs_output.png).

Use the argument `-?` to see its options:

```shell
./tbird_new_msgs '-?'
```

### Test suite

Within the `gen_new_msgs/` is the `Test/` subdirectory.  These scripts
can be used to isolate issues and/or exercise `nbiff`'s icons.

This is an example of running one of the scripts:

```shell
cd $HOME/.nbiff/gen_new_msgs/Test
./cycle_icons
```

This is [its output](sample_cycle_icons_output.png).

### nbiff

`nbiff` is the data visualizer.  It runs a script/program and
depending on the results, displays different systray icons.

It is designed to be invoked from any directory as it changes its
directory to the directory where it is located.

Below is an example calling it to run the `nbiff_qt5.py` script:

```shell
cd $HOME/.nbiff/systray
$HOME/.nbiff/systray/Run_nbiff nbiff_qt5.py &
```
