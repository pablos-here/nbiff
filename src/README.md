## Table of contents

- [Contributing](#contributing)
- [Developing](#developing)
- [Source tree](#source-tree)
- [Architectural overview](#architectural-overview)
- [Get 'unread messages'](#get-unread-messages)
  - [Standardized output](#standardized-output)
- ['systray' visualizer](#systray-visualizer)
- [MUA affect window](#mua-affect-window)
- [Icon development](#icon-development)
- [Development configuration](#development-configuration)
- [Local directory](#local-directory)
- [Links](#links)
  - [Related projects](#related-projects)
- [Future](#future)
- [Licensing](#licensing)

## Contributing

There are several areas where one can contribute:

* Icon development - no coding required, see [Icon development](#icon-development).
* Backend - `Bourne shell`.
* Front-end - `Python/PyQt5`.

For backend and front-end development, please fork the repository and use a feature
branch. Pull requests are warmly welcome.  See the details below.

## Developing

Please read and understand the user documenation before proceeding.

## Source tree

Visualize the source tree using the `tree` command:

```
tree -F --dirsfirst src/
```

## Architectural overview
<pre>
/////////////////////
/ Mail client data  /
/////////////////////
     |
     |    +-----------------------+    +----------------------+
     +--> | Get 'Unread messages' | -> | 'systray' visualizer |
          +-----------------------+    +----------------------+
                      1                           2  ^
                                                     |
                                                     v
                                       +----------------------+
                                       |   MUA affect window  |
                                       +----------------------+
                                                  3
</pre>

`nbiff` functionality is abstracted into the following components:

1. The backend engine to get **unread messages** and
2. The front-end **systray** visualizer.
3. Mouse-click handler.

Each can be developed independently.

## Get 'unread messages'

This `Bourne shell` script reads the **mail client** data to compute
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

## MUA affect window

This `Bourne shell` script processes mouse-clicks and
per-specification, exit status and messags.

It understands the following arguments:

|                  | Additional     |                                                        |             |                    |
| Main argument    | argument(s)    | Action                                                 | Exit status | Return string      |
|------------------|----------------|--------------------------------------------------------|-------------|--------------------|
| iconify/activate |                | * If not on the main `thunderbird` window, activate it | 10          | Current desktop    |
|                  |                | * Otherwise honor the iconify/activate                 | 0           | **NULL**           |
| swap             | Target desktop | * Swap between the current and the main window.        | 11          | Current desktop or |
|                  | or '' for main |                                                        |             | '' when on main    |

* **activate** means to switch to that desktop and de-iconify all `Thunderbird` windows.
* A -1 **exit status** is an error.  Additional data may be in the
  **return string**.

## Icon development

To contribute to the `nbiff` icon sets, see the documentation on
[customization](/doc/CUSTOMIZING.md).

Once the icons are ready for consideration, use the following
streamline method:

1. [Create a new
   issue](https://github.com/pablo-blueoakdb/nbiff/issues/new) stating
   your intentions.
2. Upload your images to an image sharing website
   (e.g. https://imgur.com)
3. Update the issue with links to the images.  Note which image maps
   to which **Icon type** - as defined in the previously mentioned
   documentation. 

## Development configuration

The code is written such that the configuration files found in the
top-level `dev/` directory have precedence over the system/user
configuration files.

Use the configuration files found in `src/conf/` as a basis from which
to tailor your development environment.  These files have extensive
documentation.

Create the `dev/` directory at the same level as the `src/`
directory.  Below is a sample development tree:
<pre>
└─▬ $ tree -F --dirsfirst dev/
dev/
└── conf/
    ├── nbiff.conf
    └── tbird_new_msgs.conf

1 directory, 2 files
</pre>
## Local directory

During installation, this directory is used to seed the user's
corresponding local directory.

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
