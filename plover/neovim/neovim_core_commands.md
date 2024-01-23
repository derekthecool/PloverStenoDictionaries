# Neovim Dictionary

## Snippet Triggers

This is the most important category for easy programming.

The primary snippet actions include:

- Triggering a non-autosnippet
- Jumping to next and previous snippet nodes

The secondary snippet actions include:

- Jumping to next and previous choice nodes
- Opening choice node fuzzy selection tool

## Vim Vocabulary

```yaml
SREUPL: vim # Swap with victim as I use this more
SR*EUPL: victim # Swap with vim as I use this less
TPHOEUPL: neovim # sounds like 'noim'
```

### Other Vim Inspired Programs

- [Vieb](https://vieb.dev/)

```yaml
SRAOEB: Vieb # How the word reads
SRAOEP: Vieb # How the website says it is pronounced
```

## Quick Command-line Neovim Commands

```yaml
TPH*EUPL                 :  nvim{^}
TW                       : {^}nvim{^ ^} # Very quick method
TW-S                     : {^}nvim $(fzf)
TPHO*EUPL                :  {^}nvim
TW-R                     :  {^}nvim README.md
TPH*EUPL/RAED            :  {^}nvim README.md
TPHO*EUPL/TPHO*EUPL      :  {^}nvim --cmd \"set rtp+=$(pwd)\"
TPH*EUPL/TPH*EUPL        :  {^}nvim --cmd \"set rtp+=$(pwd)\"
TPH*EUPL/TEFT            :  '{^}nvim --headless -c "PlenaryBustedDirectory ."'
```

## Operators

```yaml
KWO*RD: { ^ciw^ }
KR*EU: { ^ci^ }
KWR*EU: { ^yi^ }
SR*EU: { ^vi^ }
TK*EU: { ^di^ }
KRA*: { ^ca^ } # Overwrites California
KWRA*: { ^ya^ } # Overwrites suffix 'ia'
SRA*: { ^va^ } # Overwrites Virginia
TKA*: { ^da^ }
TKPW-PL: { ^gc^ } # Line wise comment operator. GM doesn't really mean anything.
TKPW*PL: { ^gb^ } # Block wise comment operator. GM doesn't really mean anything.
```

## Text Objects

```yaml
SA   : {^}sa{^}
S-R  : {^}sr{^}
S-D  : {^}sd{^}
W*EU : {^}iw{^}
WA*  : {^}aw{^}
```

## Copy Commands

```yaml
KWR*S : {^}yy{^}    # Normal line copy, nothing crazy
KWR*Z : {^}\"Tyy{^} # Special line copy with appending to register T
KWR*D : {^}qtq{^}   # Clear register T for a clean start
KWR*L : {^}\"tp{^}  # Paste contents of the T register
```

## G Commands

Any command that starts with `g` or `G` or `:g`.
There are so many they deserve their own category.

See [neovim_plugin_commands](./neovim_plugin_commands.md#G Commands)
for similar mappings for neovim plugins such as `gcc` which comments the current
line.

```yaml
TKPW-G : {^}gg{^} # Top of page
TKPW-T : {^}gt{^} # Next tab
TKPW*T : {^}gT{^} # Previous tab
TKPWU  : {^}gu{^}  # Prepare to lowercase change some text
TKPW*U : {^}gU{^}  # Prepare to uppercase change some text
```

### Language Server Protocol Commands

```yaml
TKPW-D  : {^}gd{^}  # gd -- go to definition
TKPW*D  : {^}gD{^}  # gD -- go to declaration
TKPWEU  : {^}gi{^}  # gi -- go to implementation
TKPW-R  : {^}gr{^}  # gr -- go to references
TKPW*R  : {^}gR{^}  # gR -- replace symbol
TKPW-PB : {^}gn{^}  # gn -- go to next diagnostic
TKPW-P  : {^}gp{^}  # gp -- go to previous diagnostic
```

## Commands

```yaml
PHAOEUFP       :  "{#Escape}{^zzz^}{PLOVER:SET_CONFIG:}"  # This command is will save my file in vim and reload Plover
TK-D   : {^}dd{^}
TKHRAO*ET      :  ^dd^ # Delete line
-FP            :  {^}{\#Control_R(u)}{^} # easy control + u for up scroll
-PL            :  {^}{\#Control_R(d)}{^} # easy control + d for down scroll
#SR-RS         :  {^}{\#Control_R(backslash)}{\#Control_R(n)}{^}
STPA           :  {\#Escape}{^zzz^} # Mapped in vim to :update<CR>
STPA/STPA      :  {^}{\#Escape}:w\\n{^} # Twice for a forced write to single file
STPHA          :  {\#Escape}{^ZZ^}
KW*EUTD        :  {\#Escape}:wq\\n{^}
KW*EUT         :  {\#Escape}:q\\n{^}
KW*EUTS        :  {\#Escape}:wqa\\n{^}
KPH-D          : {^}{\#Escape}:{^}
KPHOEUD        : {^}:{^}
KPH-DZ         : {^}{\#Escape}:lua{^ ^}
KPHOEUDZ       : {^}:lua{^ ^}
KPH-DZ/KPH-DZ  : {^}{\#Escape}:luafile %\\n{^}
HRAO*ERD       :  {^}<leader>{^}
KR-R           :  {^}<CR>{^}
HRAOUF         :  {^}luafile %{^}
HRAO*UF  : {^}{\#Escape}:luafile %\\n{^}
SKWR*URPL : {^},fd{^}
```

### Searching And Replacing Commands

```yaml
PR*EPL         :  {^}{\#Escape}:%smagic/{^}
PRO*EUPL       :  {^}:smagic/{^}
HRAO*UD        :  {^}:luado return line
```

## Special Commands To Trigger Autosnippets

These are meant to trigger autosnippets, meaning that as soon as this exact text
is typed/written/stenoed the snippet will activate.

### Core Programming Items

```yaml
#TP*             : IF{^}
#*EFLS           : ELS_EI_F{^} # this one is weird because it must not contain the words "else" or "if" or it'll trigger over snippets
#*ELS            : ELSE{^}
#TP*R            : FOR{^}
#WHAO*EUL        : WHILE{^}
#TPRAO*EFP       : FREACH{^} # FOREACH conflicts with FOR
#TP*UBGS         : FUNCTION{^}
#PR*EUPBT        : PRINT{^}
#PR*EUPBTS       : ERRORPRINT{^}
KHR*U: INCLUDE{^} # Most languages have some kind of include such as #include, using, open, import etc.
#KHR*U           : INCLUDE{^} # Most languages have some kind of include such as #include, using, open, import etc.
#TK*PB           : DEFINE{^}
#TPO*RPLT        : FRMAT{^} # FORMAT conflicts with FOR
#TA*FBG          : TASK{^}
#TRAO*EU         : TRY{^}
#KA*UL           : {^}{MODE:RESET}CALL{^}  # For expanding function calls
#KHRA*S          : CLASS{^}
KAUPB/#STR*URBGT: CONSTRUCTOR{^}
#KA*UPB/#KA*UPB  : CONSTRUCTOR{^}
KRURBGT: constructor # easier normal spelling
#KR*URBGT        : CONSTRUCTOR{^}
TA*EUBL: TABLE{^}
TPHAOUPL: enum
#TPHAO*UPL       : ENUM{^} # Noom
#TPH*UPL         : ENUM{^} # Num
TPHAOUPLGS: enumeration
TPHAOUPLT: enumerate
#SW*EUFP         : SWITCH{^}
```

### Regex

This is such a important category it needs it's own block.

```yaml
#RA*FP : REGMATCH # Single regex match
#RA*FPS : ALLREGMATCH # All regex matches
#RA*EUS : REGREPLACE # Regex replace
```

### Testing

This is for both writing tests and running them.

```yaml
#S*ERT           : ASSERT{^}
#T*EFT           : TEST{^}
#STKRAO*EUB      : DESCRIBE{^}
```

### Helpers

```yaml
#-R              : FIRST{^}
#-B              : SECOND{^}
#-G              : THIRD{^}
TO*EUD: TODO{^}
```

## Neovim API

### Meant To Trigger Snippet

```yaml
TPHO*EFT: VIM.NOTIFY{^}
```

### Not Meant To Trigger Snippet

```yaml
SRAO*EUP: vim.api.{^}
SREUPBT: vim.print(
TP*PB: vim.fn.{^}
KPH*D: vim.cmd{^}
```
