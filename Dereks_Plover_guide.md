# Derek's Plover Guide

This guide is a rough and random list of items I like to keep as a Plover
reference.

## Shortcut Key Names

Here are the key names you'll want to use:

| Keys                                     | Command Key Names (case-insensitive)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Letters                                  | `a`, `b`, `c`, `d`, `e`, `f`, `g`, `h`, `i`, `j`, `k`, `l`, `m`, `n`, `o`, `p`, `q`, `r`, `s`, `t`, `u`, `v`, `w`, `x`, `y`, `z`                                                                                                                                                                                                                                                                                                                                                                                            |
| Accented Letters (international layouts) | `udiaeresis`, `eacute`, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Numbers                                  | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Control Keys                             | `Escape`, `Tab`, `Caps_Lock`, `space`, `BackSpace`, `Delete`, `Return`, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| F-Keys                                   | `F1`, `F2`, `F3`, `F4`, `F5`, `F6`, `F7`, `F8`, `F9`, `F10`, `F11`, `F12`                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Common Named Keys                        | `= equal`<br />`- minus`<br />`[ bracketleft`<br />`] bracketright`<br />`/ slash`<br />`\ backslash`<br />`' quoteright`<br />`, comma`<br />`. period`<br />`; semicolon`<br />`~ asciitilde`<br />`^ asciicircum`<br />`` ` quoteleft``<br />[???and more](https://github.com/openstenoproject/plover/blob/master/plover/key_combo.py#L21)                                                                                                                                                                                 |
| Media Keys                               | **Common**: `AudioRaiseVolume`, `AudioLowerVolume`, `AudioMute`, `AudioNext`, `AudioPrev`, `AudioStop`, `AudioPlay`, `AudioPause`, `Eject`<br />**Mac**: `MonBrightnessUp`, `MonBrightnessDown`, `KbdBrightnessUp`, `KbdBrightnessDown`<br />**Windows**: `Back`, `Forward`, `Refresh`<br />**Linux**: XF86 key names are supported, for example `XF86_MonBrightnessUp` - refer to [the definition file in `python-xlib`](https://github.com/python-xlib/python-xlib/blob/master/Xlib/keysymdef/xf86.py) for the key names. |

Consult the code for the [full list of supported keyboard shortcut keys](https://github.com/openstenoproject/plover/blob/master/plover/key_combo.py#L21).

**Note:** a key name will determine a key to emulate with **no modifiers** based on your keyboard layout. For example, let's say we want to make a keyboard shortcut to hit shift-2 which is "@" in QWERTY: `{#at}` will only press the `2` key. To get the `@` symbol, we need to add the shift key: `{#shift(at)}`, which is functionally the same as `{#shift(2)}`.

```
'aacute'            :  '\xe1', # ??
'acircumflex'       :  '\xe2', # ??
'acute'             :  '\xb4', # ??
'adiaeresis'        :  '\xe4', # ??
'ae'                :  '\xe6', # ??
'agrave'            :  '\xe0', # ??
'ampersand'         :     '&', # &
'apostrophe'        :     "'", # '
'aring'             :  '\xe5', # ??
'asciicircum'       :     '^', # ^
'asciitilde'        :     '~', # ~
'asterisk'          :     '*', # *
'at'                :     '@', # @
'atilde'            :  '\xe3', # ??
'backslash'         :    '\\', # \
'bar'               :     '|', # |
'braceleft'         :     '{', # {
'braceright'        :     '}', # }
'bracketleft'       :     '[', # [
'bracketright'      :     ']', # ]
'brokenbar'         :  '\xa6', # ??
'ccedilla'          :  '\xe7', # ??
'cedilla'           :  '\xb8', # ??
'cent'              :  '\xa2', # ??
'clear'             :  '\x0b', # 
'colon'             :     ':', # :
'comma'             :     ',', # ,
'copyright'         :  '\xa9', # ??
'currency'          :  '\xa4', # ??
'degree'            :  '\xb0', # ??
'diaeresis'         :  '\xa8', # ??
'division'          :  '\xf7', # ??
'dollar'            :     '$', # $
'eacute'            :  '\xe9', # ??
'ecircumflex'       :  '\xea', # ??
'ediaeresis'        :  '\xeb', # ??
'egrave'            :  '\xe8', # ??
'equal'             :     '=', # =
'eth'               :  '\xf0', # ??
'exclam'            :     '!', # !
'exclamdown'        :  '\xa1', # ??
'grave'             :     '`', # `
'greater'           :     '>', # >
'guillemotleft'     :  '\xab', # ??
'guillemotright'    :  '\xbb', # ??
'hyphen'            :  '\xad', # ??
'iacute'            :  '\xed', # ??
'icircumflex'       :  '\xee', # ??
'idiaeresis'        :  '\xef', # ??
'igrave'            :  '\xec', # ??
'less'              :     '<', # <
'macron'            :  '\xaf', # ??
'masculine'         :  '\xba', # ??
'minus'             :     '-', # -
'mu'                :  '\xb5', # ??
'multiply'          :  '\xd7', # ??
'nobreakspace'      :  '\xa0', # ??
'notsign'           :  '\xac', # ??
'ntilde'            :  '\xf1', # ??
'numbersign'        :     '#', # #
'oacute'            :  '\xf3', # ??
'ocircumflex'       :  '\xf4', # ??
'odiaeresis'        :  '\xf6', # ??
'ograve'            :  '\xf2', # ??
'onehalf'           :  '\xbd', # ??
'onequarter'        :  '\xbc', # ??
'onesuperior'       :  '\xb9', # ??
'ooblique'          :  '\xd8', # ??
'ordfeminine'       :  '\xaa', # ??
'oslash'            :  '\xf8', # ??
'otilde'            :  '\xf5', # ??
'paragraph'         :  '\xb6', # ??
'parenleft'         :     '(', # (
'parenright'        :     ')', # )
'percent'           :     '%', # %
'period'            :     '.', # .
'periodcentered'    :  '\xb7', # ??
'plus'              :     '+', # +
'plusminus'         :  '\xb1', # ??
'question'          :     '?', # ?
'questiondown'      :  '\xbf', # ??
'quotedbl'          :     '"', # "
'quoteleft'         :     '`', # `
'quoteright'        :     "'", # '
'registered'        :  '\xae', # ??
'return'            :    '\r', #
'section'           :  '\xa7', # ??
'semicolon'         :     ';', # ;
'slash'             :     '/', # /
'space'             :     ' ', #
'ssharp'            :  '\xdf', # ??
'sterling'          :  '\xa3', # ??
'tab'               :    '\t', #
'thorn'             :  '\xfe', # ??
'threequarters'     :  '\xbe', # ??
'threesuperior'     :  '\xb3', # ??
'twosuperior'       :  '\xb2', # ??
'uacute'            :  '\xfa', # ??
'ucircumflex'       :  '\xfb', # ??
'udiaeresis'        :  '\xfc', # ??
'ugrave'            :  '\xf9', # ??
'underscore'        :     '_', # _
'yacute'            :  '\xfd', # ??
'ydiaeresis'        :  '\xff', # ??
'yen'               :  '\xa5', # ??
```
