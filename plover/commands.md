# Plover Commands

## Basic Commands

```yaml
PW-FP       : {\#BackSpace}
PW*FP       : {\#Control(BackSpace)} # Delete backward by word
PW-FPL      : {\#Delete}
PW*FPL      : {\#Control(Delete)}  # Delete forward by word
PW-FPL      : {\#Delete}
R-R         : {MODE:RESET}{^\\n}{^} # Normal enter method
#R-R        : {^\\n}{^} # Back up method that does not reset mode
R-RB        : {MODE:RESET}{\#Shift_L(Return)}{^} # Good for teams and discord for multiline messages
R*R         : {^\\n}{^}{-|} # Single new line with making next word capitalized
SKWRA*URBGS : {MODE:RESET}{\#Shift_L(Return Return)}{^}{-|} # Good for teams and discord for multiline messages
SKWRAURBGS  : {MODE:RESET}{^\\n\\n^}{-|}
TA*B        : {\#Tab}{^}
TA*BT       : {\#Alt_L(Tab Tab)}
TK*EL       : {\#Delete}
TPEFBG      : {\#Escape}
SKWR        : {^^} # Another way besides.TK-LS
KW-R        : {\#Left}{^} # Replaces "inquire" use KWEUR instead
KW-RB       : {\#Control_L(Left)}{^} # Replaces "--" use Emily-symbols
KW-B        : {\#Down}{^} # Replaces "," not unique no issue
KW-G        : {\#Right}{^} # Replaces "requesting" use KW/-G instead
KW*BG       : {\#Control_L(Right)}{^} # Does not replace anything
KW-P        : {\#Up}{^} # Does not relace anything
```

## Plover Control

```yaml
TKUPT    : {PLOVER:ADD_TRANSLATION}
PHRO*F   : {PLOVER:SUSPEND}
PHRO*PB  : {PLOVER:RESUME}
PHROLG   : {PLOVER:TOGGLE}
PHR*UP   : {PLOVER:LOOKUP}
PHROFG   : {PLOVER:CONFIGURE}
PHROFBGS : {PLOVER:FOCUS}
PHROBGT  : {PLOVER:QUIT}
PHROFL   : "{PLOVER:SET_CONFIG:'translation_frame_opacity':100}"  # Commands like this require quote wrapping like this
PHROFS   : {PLOVER:SUGGESTIONS}
```

## Plover Modes

```yaml
SR-RS         : {\#Escape}{^}{MODE:RESET} # Suppress the next space after escape
SR*RS         : {\#Control_L(bracketleft)}{^}{MODE:RESET} # Alternate escape
S-P           : {MODE:RESET}{^ ^}
S*P           : {^ ^}
KA*PS         : {MODE:CAPS}
TAO*EULT      : {MODE:TITLE}
HRO*ERS       : {MODE:LOWER}
KAPL/*EL      : {^ ^}{MODE:CAMEL} # This mode deletes normal spaces and needs a space at the start
KAEPL         : {^ ^}{MODE:CAMEL} # This mode deletes normal spaces and needs a space at the start
KA*EPL        : {^ ^}{MODE:TITLE}{MODE:SET_SPACE:} # This mode deletes normal spaces and needs a space at the start
SKWRO*EUPB    : {^ ^}{MODE:SET_SPACE:} # This mode deletes normal spaces and needs a space at the start
STPHA*EUBG    : {^ ^}{MODE:SNAKE} # This mode deletes normal spaces and needs a space at the start
PH*UPB        : {^ ^}{MODE:SET_SPACE:????} # This mode deletes normal spaces and needs a space at the start
STKPWR/PRAPL  : {PLOVER:PRIORITY_DICT:programming.md}
STKPWR/WORBG : {PLOVER:PRIORITY_DICT:work.md}
```

## Plover Spacing

```yaml
KPAD    : {:retro_case:cap_first_word}
KPA*L   : {:case:upper_first_word}
*UPD    : {:retro_case:upper_first_word}
HRO*ER  : {:case:lower_first_char}
HRO*ERD : {:retro_case:lower_first_char}
#       : =repeat_last_stroke # Quick command to run the last stroke again
#*      : {*}  # Retroactively toggle the asterisk. The long format command has errors {=retrospective_toggle_asterisk}
AFPS    : {*?} # Retroactively insert a space. Writing the phrase "worth" + "while" makes the translation of worthwhile, running this command will split the phrase into two parts. The long format command has errors {=retrospective_insert_space}
TK-FPS  : {*!} # Retroactively delete a space. Writing any two words can be jammed back together using this stroke. The long format command has errors {=retrospective_delete_space}
```

## [plover_fancy_text](https://github.com/psethwick/plover_fancytext) Plugin Commands

Don't use the - in words that do not have a vowel.

```yaml
23*9          : "{:fancytext_set:off}"
23*9/S/1      : "{:fancytext_retro:1:figlet:script}"
23*9/S/2      : "{:fancytext_retro:2:figlet:script}"
23*9/S/3      : "{:fancytext_retro:3:figlet:script}"
23*9/S/4      : "{:fancytext_retro:4:figlet:script}"
23*9/S/5      : "{:fancytext_retro:5:figlet:script}"
23*9/T-/1     : "{:fancytext_retro:1:figlet}"
23*9/T-/2     : "{:fancytext_retro:2:figlet}"
23*9/T-/3     : "{:fancytext_retro:3:figlet}"
23*9/T-/4     : "{:fancytext_retro:4:figlet}"
23*9/T-/5     : "{:fancytext_retro:5:figlet}"
23*9/P/1      : "{:fancytext_retro:1:figlet:shadow}"
23*9/P/2      : "{:fancytext_retro:2:figlet:shadow}"
23*9/P/3      : "{:fancytext_retro:3:figlet:shadow}"
23*9/P/4      : "{:fancytext_retro:4:figlet:shadow}"
23*9/P/5      : "{:fancytext_retro:5:figlet:shadow}"
23*9/PHORS    : "{:fancytext_set:morse}"
23*9/PWORD    : "{:fancytext_set:blackboardbold}"
23*9/SPWAP    : "{:fancytext_set:smallcaps}"
23*9/PWUB    : "{:fancytext_set:bubble}"
23*9/KRAOEU  : "{:fancytext_set:crytyping}"
23*9/SRAEUP  : "{:fancytext_set:fullwidth}"
23*9/PHED    : "{:fancytext_set:medieval}"
23*9/SA-RBG   : "{:fancytext_set:sarcasm}"
23*9/UP      : "{:fancytext_set:upsidedown}"
23*9/AOU     : "{:fancytext_set:uwu}"
23*9/AO*U     : "{:fancytext_set:UwU}"
23*9/STKPWAL : "{:fancytext_set:zalgo}"
```

## [plover_number_conversion](https://github.com/Volensia/plover_number_format) Plugin Commands

```yaml
TPHUPL/WORD/0     : "{:number_word_conversion:0:2}"
TPHUPL/WORD/1     : "{:number_word_conversion:1:2}"
TPHUPL/WORD/2     : "{:number_word_conversion:2:2}"
TPHUPL/WORD/ROEPL : "{:number_format_roman:0:0}"
```
