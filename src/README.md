## Table of contents

- [Developing](#developing)
- [Source tree](#source-tree)
- [Architectural overview](#architectural-overview)
- [Get 'unread messages'](#get-unread-messages)
  - [Standardized output](#standardized-output)
- ['systray' visualizer](#systray-visualizer)
- [Icon development](#icon-development)
- [Development configuration](#development-configuration)
  - [Local directory](#local-directory)
- [Contributing](#contributing)
- [Links](#links)
  - [Related projects](#related-projects)
- [Future](#future)
- [Licensing](#licensing)

## Developing

Please read and understand the user documenation before proceeding.

## Source tree

<pre>
tree -F --dirsfirst .
├── conf/
│   ├── nbiff.conf
│   └── tbird_new_msgs.conf
├── gen_new_msgs/
│   ├── Test/
│   │   ├── big_unread_count*
│   │   ├── cycle_icons*
│   │   ├── death_sim*
│   │   ├── MUA_up_down*
│   │   ├── README.md
│   │   ├── read_unread*
│   │   ├── sleep_4ever*
│   │   └── test_suite*
│   └── tbird_new_msgs*
├── icons/
│   ├── src/
│   │   └── 01.read.src.png
│   ├── 01.error.png
│   ├── 01.MUA_is_down.png
│   ├── 01.no_unread_msgs.png
│   ├── 01.unread_msgs.big_red_dot.png
│   ├── 01.unread_msgs.w2r.png
│   ├── README.md
│   └── Update_local_symlinks*
├── local/
│   ├── conf/
│   │   ├── nbiff.conf
│   │   └── tbird_new_msgs.conf
│   └── icons/
│       ├── 01.error.png -> ../../icons/01.error.png
│       ├── 01.MUA_is_down.png -> ../../icons/01.MUA_is_down.png
│       ├── 01.no_unread_msgs.png -> ../../icons/01.no_unread_msgs.png
│       ├── 01.unread_msgs.big_red_dot.png -> ../../icons/01.unread_msgs.big_red_dot.png
│       ├── 01.unread_msgs.w2r.png -> ../../icons/01.unread_msgs.w2r.png
│       └── unread_msgs.png
├── systray/
│   ├── nbiff_qt5.py*
│   ├── Run_nbiff*
│   └── Run_tbird_nbiff*
├── Globals
├── LICENSE
└── README.md
</pre>

## Architectural overview
<pre>
/////////////////////
/ Mail client data  /
/////////////////////
     |
     |    +-----------------------+    +----------------------+
     +--> | Get 'Unread messages' | -> | 'systray' visualizer |
          +-----------------------+    +----------------------+
                      1                           2
</pre>

`nbiff` is divided into two components:

1. The backend engine to get **unread messages** and
2. The frontend **systray** visualizer.

Each can be developed independently.

## Get 'unread messages'

This `bourne shell` script reads the **mail client** data to compute
the number of **Unread messages**.

It writes standardized messages to standard output.  The messages are
visualized by the **systray** visualizer.

The script can be run standalone. 

It is commonly a subprocess of the **systray** visualzier, which reads
and parses its output - more below.

Multiple instances of the script can run without interfering with
another.  This allows development while running a production version.

### Standardized output

Each line may have zero or one of the substrings listed below.

The **systray** visualizer should only act on the strings below.  Any
others can safely be ignored.

| Substring        | Definition                                       |
|------------------|--------------------------------------------------|
| MUA is up        | The mail client is running.                      |
| MUA is down      | The mail client is **not** running.              |
| Unread count = X | The **Unread messages** is in the integer **X**. |

## 'systray' visualizer

This `python/PyQt5` script runs a script and parses its output to
decide what icon and menu to display.

It searches for the above mentioned substrings in the output and acts
accordingly.

To facilitate development and testing, test scripts found in `.../gen_new_msgs/Tests`
can be used.

The wrapper script `Run_nbiff` performs all the edit-checks and calls
the `python` script with the correct arguments.

The overarching wrapper script `Run_tbird_nbiff` calls the previous
wrapper script and is specific to `Thunderbird`.  Each different
**email client** will have its own wrapper script.

## Icon development

To contribute to the `nbiff` icons, see the documentation on [icon
development](doc/CUSTOMIZING.md).

To make it easy:

1. Upload your images to an image sharing website (e.g. https://imgur.com)
2. [Create a new
   issue](https://github.com/pablo-blueoakdb/nbiff/issues/new) and
   reference the images.

## Development configuration

**TODO**

The base software supports running multiple instances of `nbiff`.
Furthermore, the source tree supports the existence of a **dev**
directory structure at the top-levl of the proejct tree:

```
something may go here ...
```

Populate it the the corresponding `...src/conf/*.conf` file and suit
to taste.

### Local directory

During installation, this directory is used to seed the user's
corresponding local directory.

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

- [Software repository](https://github.com/pablo-blueoakdb/nbiff)
- [Project
  tracker](https://github.com/users/pablo-blueoakdb/projects/1)
- [Issue tracker](https://github.com/pablo-blueoakdb/nbiff/issues)

### Related projects

The following projects are `Thunderbird`-centric:

- [birdtray](https://github.com/gyunaev/birdtray)
- [systray-x](https://github.com/Ximi1970/systray-x)

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

Distributed under the MIT License.  See [LICENSE](LICENSE) for more
information.
