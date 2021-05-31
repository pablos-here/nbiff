# Icons

All icons must be Portable Network Graphics (png)

## Icon sets

At a minimum, there are three icon **types** per group that may be
displayed in the systray:

1. read.png - there are **no** unread messages
2. unread.png - there are unread messages
3. error.png - an error is encountered 

## File naming

- Prefix each group with the next available sequential number
  (e.g. `01`, `02`)  This becomes the `group number` for the `icon
  set`
- Use a period (`.`) to break up attributes.

### Examples

- `01.unread_msg.big_red_dot.png`
  - `01` - group **01**
  - `unread_msg` 
  - `big_red_dot` 
- `01.unread_msg.w2r.png`
  - `w2r` - white to read

## Icon set `01`

At a minimum, these are the icons that make up the `01 icon set`:

- `01.error.png`
- `01.read.png`
- `01.unread_msg.big_red_dot.png`
- `01.unread_msg.w2r.png`

## src/

This directory is used to store the `base` icon image from which an
`icon set` is built.

Prefix the file name with the `group number`

### Example

- `01.read.src.png` - We use the `src` attribute to minimize clobbering
  `01.read.png` file by mistake.
