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
| Common Named Keys                        | `= equal`<br />`- minus`<br />`[ bracketleft`<br />`] bracketright`<br />`/ slash`<br />`\ backslash`<br />`' quoteright`<br />`, comma`<br />`. period`<br />`; semicolon`<br />`~ asciitilde`<br />`^ asciicircum`<br />`` ` quoteleft``<br />[…and more](https://github.com/openstenoproject/plover/blob/master/plover/key_combo.py#L21)                                                                                                                                                                                 |
| Media Keys                               | **Common**: `AudioRaiseVolume`, `AudioLowerVolume`, `AudioMute`, `AudioNext`, `AudioPrev`, `AudioStop`, `AudioPlay`, `AudioPause`, `Eject`<br />**Mac**: `MonBrightnessUp`, `MonBrightnessDown`, `KbdBrightnessUp`, `KbdBrightnessDown`<br />**Windows**: `Back`, `Forward`, `Refresh`<br />**Linux**: XF86 key names are supported, for example `XF86_MonBrightnessUp` - refer to [the definition file in `python-xlib`](https://github.com/python-xlib/python-xlib/blob/master/Xlib/keysymdef/xf86.py) for the key names. |

Consult the code for the [full list of supported keyboard shortcut keys](https://github.com/openstenoproject/plover/blob/master/plover/key_combo.py#L21).

**Note:** a key name will determine a key to emulate with **no modifiers** based on your keyboard layout. For example, let's say we want to make a keyboard shortcut to hit shift-2 which is "@" in QWERTY: `{#at}` will only press the `2` key. To get the `@` symbol, we need to add the shift key: `{#shift(at)}`, which is functionally the same as `{#shift(2)}`.

```
'aacute'            :  '\xe1', # á
'acircumflex'       :  '\xe2', # â
'acute'             :  '\xb4', # ´
'adiaeresis'        :  '\xe4', # ä
'ae'                :  '\xe6', # æ
'agrave'            :  '\xe0', # à
'ampersand'         :     '&', # &
'apostrophe'        :     "'", # '
'aring'             :  '\xe5', # å
'asciicircum'       :     '^', # ^
'asciitilde'        :     '~', # ~
'asterisk'          :     '*', # *
'at'                :     '@', # @
'atilde'            :  '\xe3', # ã
'backslash'         :    '\\', # \
'bar'               :     '|', # |
'braceleft'         :     '{', # {
'braceright'        :     '}', # }
'bracketleft'       :     '[', # [
'bracketright'      :     ']', # ]
'brokenbar'         :  '\xa6', # ¦
'ccedilla'          :  '\xe7', # ç
'cedilla'           :  '\xb8', # ¸
'cent'              :  '\xa2', # ¢
'clear'             :  '\x0b', # 
'colon'             :     ':', # :
'comma'             :     ',', # ,
'copyright'         :  '\xa9', # ©
'currency'          :  '\xa4', # ¤
'degree'            :  '\xb0', # °
'diaeresis'         :  '\xa8', # ¨
'division'          :  '\xf7', # ÷
'dollar'            :     '$', # $
'eacute'            :  '\xe9', # é
'ecircumflex'       :  '\xea', # ê
'ediaeresis'        :  '\xeb', # ë
'egrave'            :  '\xe8', # è
'equal'             :     '=', # =
'eth'               :  '\xf0', # ð
'exclam'            :     '!', # !
'exclamdown'        :  '\xa1', # ¡
'grave'             :     '`', # `
'greater'           :     '>', # >
'guillemotleft'     :  '\xab', # «
'guillemotright'    :  '\xbb', # »
'hyphen'            :  '\xad', # ­
'iacute'            :  '\xed', # í
'icircumflex'       :  '\xee', # î
'idiaeresis'        :  '\xef', # ï
'igrave'            :  '\xec', # ì
'less'              :     '<', # <
'macron'            :  '\xaf', # ¯
'masculine'         :  '\xba', # º
'minus'             :     '-', # -
'mu'                :  '\xb5', # µ
'multiply'          :  '\xd7', # ×
'nobreakspace'      :  '\xa0', #  
'notsign'           :  '\xac', # ¬
'ntilde'            :  '\xf1', # ñ
'numbersign'        :     '#', # #
'oacute'            :  '\xf3', # ó
'ocircumflex'       :  '\xf4', # ô
'odiaeresis'        :  '\xf6', # ö
'ograve'            :  '\xf2', # ò
'onehalf'           :  '\xbd', # ½
'onequarter'        :  '\xbc', # ¼
'onesuperior'       :  '\xb9', # ¹
'ooblique'          :  '\xd8', # Ø
'ordfeminine'       :  '\xaa', # ª
'oslash'            :  '\xf8', # ø
'otilde'            :  '\xf5', # õ
'paragraph'         :  '\xb6', # ¶
'parenleft'         :     '(', # (
'parenright'        :     ')', # )
'percent'           :     '%', # %
'period'            :     '.', # .
'periodcentered'    :  '\xb7', # ·
'plus'              :     '+', # +
'plusminus'         :  '\xb1', # ±
'question'          :     '?', # ?
'questiondown'      :  '\xbf', # ¿
'quotedbl'          :     '"', # "
'quoteleft'         :     '`', # `
'quoteright'        :     "'", # '
'registered'        :  '\xae', # ®
'return'            :    '\r', #
'section'           :  '\xa7', # §
'semicolon'         :     ';', # ;
'slash'             :     '/', # /
'space'             :     ' ', #
'ssharp'            :  '\xdf', # ß
'sterling'          :  '\xa3', # £
'tab'               :    '\t', #
'thorn'             :  '\xfe', # þ
'threequarters'     :  '\xbe', # ¾
'threesuperior'     :  '\xb3', # ³
'twosuperior'       :  '\xb2', # ²
'uacute'            :  '\xfa', # ú
'ucircumflex'       :  '\xfb', # û
'udiaeresis'        :  '\xfc', # ü
'ugrave'            :  '\xf9', # ù
'underscore'        :     '_', # _
'yacute'            :  '\xfd', # ý
'ydiaeresis'        :  '\xff', # ÿ
'yen'               :  '\xa5', # ¥
```
