# Icon development

## Icon sets

Each icon-set must have at least four different image files:

1. **No unread messages** - there are **no** unread messages.
2. **Unread messages** - there are unread messages.
3. **Error** - an error is encountered (e.g. a non-integer was
   returned)
4. **MUA is down** - the mail client is not running.

It is acceptable to use `symlink`s to share among icon-sets.

## Group numbering

Prefix each icon-set with the next available sequential number (`01`,
`02`, etc.).

## Base file name

* Use `.`s to separate the icon attributes.
* Avoiding using **cryptic** naming

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
