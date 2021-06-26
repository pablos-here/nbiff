## Developing

### Architectural overview

<pre>
/////////////////////
/ Mail client files /
/////////////////////
     |
     |    +-----------------------+    +----------------------+
     +--> | Get 'Unread messages' | -> | 'systray' visualizer |
          +-----------------------+    +----------------------+
</pre>

`nbiff` is divided into two components:

1. The engine to get **unread messages** and
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

### stuff goes here 

Two technologies are used:

1. `bash` shell scripting and
2. `Python` with `PyQt5`

### Icon development

To contribute to the `nbiff` icons, see the documentation on [icon
development](src/icons/README.md).

To make it easy:

1. Upload your images to an image sharing website (e.g. https://imgur.com)
2. [Create a new
   issue](https://github.com/pablo-blueoakdb/nbiff/issues/new) and
   reference the images.

### Development configuration

**TODO**

The base software supports running multiple instances of `nbiff`.
Furthermore, the source tree supports the existence of a **dev**
directory structure at the top-levl of the proejct tree:

```
something may go here ...
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
