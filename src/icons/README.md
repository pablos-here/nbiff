# Icon development

## Icon sets

Each icon-set must have at least four different image files:

| Icon type              | Description                                                 |
|------------------------|-------------------------------------------------------------|
| **No unread messages** | No unread messages.                                         |
| **Unread messages**    | Unread messages.                                            |
| **Error**              | An error was encountered (e.g. a non-integer was returned). |
| **MUA is down**        | The mail client is not running.                             |

## Group numbering

Prefix each icon-set with the next available sequential number (`01`,
`02`, etc.).

## Base file name

* Use `.`s to separate the icon attributes.
* Avoiding using **cryptic** naming.

## Sharing files among icon-sets

Use `symlink`s to create new icon-sets.

## Example

Using the current icon-set as examples and avoiding repetition:

- `01.error.png`
  - `01` - `group number`
  - `error` - self-explanatory
  - `png` - self-explanatory
- `01.MUA_is_down.png`
  - `MUA_is_down` - self-explanatory
- `01.no_unread_msgs.png`
  - `no_unread_msgs` - self-explanatory
- `01.unread_msgs.big_red_dot.png`
  - `unread_msgs` - self-explanatory
  - `big_red_dot` - self-explanatory
- `01.unread_msgs.w2r.png`
  - `w2r` - white-to-red.  While a bit crytpic, when viewing the
    image, it should be obvious.  Right?  Hmmm.
