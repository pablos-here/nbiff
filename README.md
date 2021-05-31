![nbiff logo](doc/logo.png)
# nbiff 

`nbiff` is an intentionally simple, extensible systray email
notifier. Geared for Linux, yet it may (eventually) work on Windows.

## Features

`nbiff` has the following features:

- It is dynamic.  It self-adjusts when email accounts are
  added/deleted and folders are created/deleted
- While dynamic, it is designed to be light-weight and quick
- Largely it is immune from `Thunderbird`'s API changes
- Supports both `x11` and `wayland`
- Users can customize their own systray icons
- The systray icon provides high-level information such as whether
  there are unread messages or not.  
- Details are presented, when supported, as a tool tip or a menu
  accessed by clicking on the systray icon
  
## Installing / Getting started

1. [Go to the release
   page](https://github.com/pablo-blueoakdb/nbiff/releases) and note
   the latest release is listed first.
2. Expand a release's **Assets** and download either compressed
   version of choice.
3. Unpack the source file in a directory.  A new directory will be
   created with the version.
4. Change directories (`cd`) to the new directory.
5. Run the installer and follow the on-screen instructions:

```shell
./Install_latest.tbird
```

### Installation script

The installation script is written with the belief that the majority
of people prefer to *do* than to *read-and-do*

It handles both installs and upgrades.  It is *not* a package
manager.

### Requirements

`Python 3` is required along with some additional libraries:

```
pip3 install PyQt5 psutil
```

### GNOME + Wayland support

Some **GNOME** versions require the `KStatusNotifierItem/AppIndicator
Support` extension for **Wayland** support. 


1. [Go to extension's webpage](https://extensions.gnome.org/extension/615/appindicator-support)
2. Enable the extension:![KStatusNotifierItem](doc/KStatusNotifierItem.png)

### Initial Configuration

Some projects require initial configuration (e.g. access tokens or keys, `npm i`).
This is the section where you would document those requirements.

## Known quirks

There are rare times when an `.msf` is not immediately flushed to disk.
This causes `nbiff` to believe there are still **Unread messages**
when there are none.

Within a minute or two, `Thunderbird` eventually synchronizes the file
to disk and all is well.  Clicking on the corresponding folder
(typically an Inbox with a filter) immediately causes a flush.

Running `tbird_new_msgs` can be used to identify the offending
folder(s).

## Temporarily disabling autostart

There may be times when it is desired to not run `nbiff` and leave it
configured for autostarting.

Edit `$HOME/.nbiff/local/conf/nbiff.conf` and define the following variable:

```
DISABLE="stop you"
```

To reenable, either comment or delete the line.

## Developing

Here's a brief intro about what a developer must do in order to start developing
the project further:

```shell
git clone https://github.com/your/awesome-project.git
cd awesome-project/
packagemanager install
```

And state what happens step-by-step.

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

## Configuration

... scripts go here ... TODO
.. talk about .confs

## Contributing

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

* Create a **package** rather than using an installation script
* Provide Windows support.  To handle spaces in file/directory names
  (almost all?) variables are double quoted.  `bash` (and other tools
  such as `rsync`) would be required.

  If there is sufficient demand ...

## Licensing

The code in this project is licensed under MIT license.
