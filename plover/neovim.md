# Neovim Dictionary

## Vim Vocabulary

```yaml
TREUT : treesitter # Amazing smart parsing tool
```

## Operators

```yaml
KWO*RD  : {^ciw^}
KR*EU   : {^ci^}
KWR*EU  : {^yi^}
SR*EU   : {^vi^}
TK*EU   : {^di^}
KRA*    : {^ca^}  # Overwrites California
KWRA*   : {^ya^}  # Overwrites suffix 'ia'
SRA*    : {^va^}  # Overwrites Virginia
TKA*    : {^da^}
TKPW-PL : {^gc^}  # Line wise comment operator. GM doesn't really mean anything.
TKPW*PL : {^gb^}  # Block wise comment operator. GM doesn't really mean anything.
```

## Commands

```yaml
PHAOEUFP       :  "{#Escape}{^zzz^}{PLOVER:SET_CONFIG:}"  # This command is will save my file in vim and reload Plover
-FP            :  {^}{\#Control_R(u)}{^} # easy control + u for up scrollOEUFPj
-PL            :  {^}{\#Control_R(d)}{^} # easy control + d for down scroll
K-PL           :  {^gcc^} # Comment current line in line wise style
K*PL           :  {^gbc^} # Comment current line in block wise style
TKHRAO*ET      :  ^dd^ # Delete line
PR*EPL         :  {^}{\#Escape}:%smagic/{^}
PRO*EUPL       :  {^}:smagic/{^}
#SR-RS         :  {^}{\#Control_R(backslash)}{\#Control_R(n)}{^}
STPA           :  {\#Escape}{^zzz^} # Mapped in vim to :update<CR>
STPHA          :  {\#Escape}{^ZZ^}
KW*EUT         :  {\#Escape}:q\\n{^}
KW*EUTS        :  {\#Escape}:wqa\\n{^}
TPH*EUPL       :  nvim{^}
TPH*EUPL/RAED  :  {^}nvim README.md
TPHOEUPL       :  neovim # sounds like 'noim'
TPHO*EUPL      :  {^}nvim
TPHO*EUPL/TPHO*EUPL      :  {^}nvim --cmd \"set rtp+=.\"
KPH-D          : {^}{\#Escape}:{^}
KPHOEUD        : {^}:{^}
KPH-DZ         : {^}{\#Escape}:lua{^ ^}
KPHOEUDZ       : {^}:lua{^ ^}
KPH-DZ/KPH-DZ  : {^}{\#Escape}:luafile %\\n{^}
SREUPL         :  vim    # Swap with victim as I use this more
SR*EUPL        :  victim # Swap with vim as I use this less
HRAO*ERD       :  {^}<leader>{^}
KR-R           :  {^}<CR>{^}
HRAOUF         :  {^}luafile %{^}
```

## Special Commands To Trigger Autosnippets -- Essential For Fast Programming

```yaml
#TP*       : IF{^}
#*EFLS      : ELS_EI_F{^} # this one is weird because it must not contain the words "else" or "if" or it'll trigger over snippets
#*ELS       : ELSE{^}
#TP*R      : FOR{^}
#TPRAO*EFP : FOREACH{^}
#TP*UBGS   : FUNCTION{^}
#T*EFT     : TEST{^}
#STKRAO*EUB : DESCRIBE{^}
#PR*EUPBT  : PRINT{^}
```

## Personal Mappings That Need To Be Fast

```yaml
KH*EBGD            :  {^},vl{^} # Mark down check box
TRAO*E             :  {^},fe{^} # File tree toggle
T*EFT              :  {^},ui{^} # Test
R*UPB              :  {^},uu{^} # Run
PW-D               :  {^},u;{^} # Build
KW*EUBG            :  {^},la{^} # LSP code action version 1
KWO*EUBG            :  {^},lb{^} # LSP code action version 2
TKPW*URB           :  {^}Pp{^} # Git push (gush)
TPO*RPLT           :  {^},lf{^} # Format code
TKPW*URB/TKPW*URB  :  {^}git push\\n
TKPW*UL            :  {^}pp{^} # Git pull (gull)
TKPW*UL/TKPW*UL    :  {^}git pull\\n
PHRA*US            :  {^}vip:s/{^}   # 'plahs' for selecting paragraph and start replace
HRA*US             :  {^}gv:s/{^}    # 'lahs' for selecting previous selection and start replace
TPAO*EUL           :  {^},fF{^} # File search
TKPWAO*EUL         :  {^},fG{^} # (Guiles) File search for git files
PW*UFR             :  {^},fb{^} # Search buffers
TKPWR*EP           :  {^},fg{^} # Grep files command
HOEUP              :  {^},fh{^} # Grep files command
TK*EUFR            :  {^},gd{^} # Call plugin DiffViewOpen
TKPW*EUT           :  {^},gg{^} # Call plugin neogit
PHRUP          :  {^},aa{^} # PackerSync
TR*EUT         :  {^},ab{^} # :TSPlaygroundToggle<CR>')
HRO*EDZ         :  {^},ac{^} # Reload my entire neovim config
PHR*EPB       : {^},dP{^} # Run plenary tests for neovim plugins
WRAO          : {^}]d{^}
KWAO          : {^}[d{^}
```

## Neovim API

### Meant To Trigger Snippet

```yaml
TPHO*EFT: VIM.NOTIFY{^}
```

### Not Meant To Trigger Snippet

```yaml
SRAO*EUP : vim.api.{^}
TP*PB : vim.fn.{^}
KPH*D: vim.cmd{^}
```

## Other Vim Programs

```yaml
SRAOEB : Vieb
SRAOEP : Vieb
```

## Remapped Finger Spelling

This dictionary is from
[antistic steno-dictionaries/fingerspelling.json](https://github.com/antistic/steno-dictionaries/blob/main/fingerspelling.json)
and is designed for use with vim. The idea is that in vim you would want to be
able to type `gg` then be able to type another key such as `a` without having a
space in between.

```yaml
A*         : {^}{>}a{^}
A*P        : {^}{-|}a{^}
A*RBGS     : {>}{&a}
A*FPLT     : {-|}{&a}
PW*        : {^}{>}b{^}
PW*P       : {^}{-|}b{^}
PW*RBGS    : {>}{&b}
PW*FPLT    : {-|}{&b}
KR*        : {^}{>}c{^}
KR*P       : {^}{-|}c{^}
KR*RBGS    : {>}{&c}
KR*FPLT    : {-|}{&c}
TK*        : {^}{>}d{^}
TK*P       : {^}{-|}d{^}
TK*RBGS    : {>}{&d}
TK*FPLT    : {-|}{&d}
*E         : {^}{>}e{^}
*EP        : {^}{-|}e{^}
*ERBGS     : {>}{&e}
*EFPLT     : {-|}{&e}
TW*        : {^}{>}e{^}
TW*P       : {^}{-|}e{^}
TW*RBGS    : {>}{&e}
TW*FPLT    : {-|}{&e}
TP*        : {^}{>}f{^}
TP*P       : {^}{-|}f{^}
TP*RBGS    : {>}{&f}
TP*FPLT    : {-|}{&f}
TKPW*      : {^}{>}g{^}
TKPW*P     : {^}{-|}g{^}
TKPW*RBGS  : {>}{&g}
TKPW*FPLT  : {-|}{&g}
H*         : {^}{>}h{^}
H*P        : {^}{-|}h{^}
H*RBGS     : {>}{&h}
H*FPLT     : {-|}{&h}
*EU        : {^}{>}i{^}
*EUP       : {^}{-|}i{^}
*EURBGS    : {>}{&i}
*EUFPLT    : {-|}{&i}
TWR*       : {^}{>}i{^}
TWR*P      : {^}{-|}i{^}
TWR*RBGS   : {>}{&i}
TWR*FPLT   : {-|}{&i}
SKWR*      : {^}{>}j{^}
SKWR*P     : {^}{-|}j{^}
SKWR*RBGS  : {>}{&j}
SKWR*FPLT  : {-|}{&j}
K*         : {^}{>}k{^}
K*P        : {^}{-|}k{^}
K*RBGS     : {>}{&k}
K*FPLT     : {-|}{&k}
HR*        : {^}{>}l{^}
HR*P       : {^}{-|}l{^}
HR*RBGS    : {>}{&l}
HR*FPLT    : {-|}{&l}
PH*        : {^}{>}m{^}
PH*P       : {^}{-|}m{^}
PH*RBGS    : {>}{&m}
PH*FPLT    : {-|}{&m}
TPH*       : {^}{>}n{^}
TPH*P      : {^}{-|}n{^}
TPH*RBGS   : {>}{&n}
TPH*FPLT   : {-|}{&n}
O*         : {^}{>}o{^}
O*P        : {^}{-|}o{^}
O*RBGS     : {>}{&o}
O*FPLT     : {-|}{&o}
P*         : {^}{>}p{^}
P*P        : {^}{-|}p{^}
P*RBGS     : {>}{&p}
P*FPLT     : {-|}{&p}
KW*        : {^}{>}q{^}
KW*P       : {^}{-|}q{^}
KW*RBGS    : {>}{&q}
KW*FPLT    : {-|}{&q}
R*         : {^}{>}r{^}
R*P        : {^}{-|}r{^}
R*RBGS     : {>}{&r}
R*FPLT     : {-|}{&r}
S*         : {^}{>}s{^}
S*P        : {^}{-|}s{^}
S*RBGS     : {>}{&s}
S*FPLT     : {-|}{&s}
T*         : {^}{>}t{^}
T*P        : {^}{-|}t{^}
T*RBGS     : {>}{&t}
T*FPLT     : {-|}{&t}
*U         : {^}{>}u{^}
*UP        : {^}{-|}u{^}
*URBGS     : {>}{&u}
*UFPLT     : {-|}{&u}
TR*        : {^}{>}u{^}
TR*P       : {^}{-|}u{^}
TR*RBGS    : {>}{&u}
TR*FPLT    : {-|}{&u}
SR*        : {^}{>}v{^}
SR*P       : {^}{-|}v{^}
SR*RBGS    : {>}{&v}
SR*FPLT    : {-|}{&v}
W*         : {^}{>}w{^}
W*P        : {^}{-|}w{^}
W*RBGS     : {>}{&w}
W*FPLT     : {-|}{&w}
KP*        : {^}{>}x{^}
KP*P       : {^}{-|}x{^}
KP*RBGS    : {>}{&x}
KP*FPLT    : {-|}{&x}
KWR*       : {^}{>}y{^}
KWR*P      : {^}{-|}y{^}
KWR*RBGS   : {>}{&y}
KWR*FPLT   : {-|}{&y}
STKPW*     : {^}{>}z{^}
STKPW*P    : {^}{-|}z{^}
STKPW*RBGS : {>}{&z}
STKPW*FPLT : {-|}{&z}
SWR*       : {^}{>}z{^}
SWR*P      : {^}{-|}z{^}
SWR*RBGS   : {>}{&z}
SWR*FPLT   : {-|}{&z}
```
