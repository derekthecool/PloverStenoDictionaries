# Programming Dictionary

SKW-T: \' # single quote character
KR-GS: \" # double quote character
PW-RB: \\ # backslash
HAERB: \# # hash character on the right hand side
'#-T': 9 # you should not escape the # in strokes

## Frequently Used Words

```yaml
RAO*T: reboot # This word should be one stroke!
RAOEBT: reboot
KRORPL: cross platform
ARGS: args
KAO*UT: execute
KAOUBL: executable
```

## Technical Jargon

```yaml
AOU/ART: UART
KPAP: pcap
PHAO*U: MCU
PH*BG : MQTT
PH*BG/PH*BG : LWT
PH*BG/PH*BG/PH*BG : QoS
TAOEP : TCP
TAOEP/TAOEP : TCP/IP
HREUBGS : Linux
KEUG    : config # Overwrites: can Iing
K*EUG   : {^}Config # Overwrites: Qiing
```

## Common File Names

```yaml
RA*ED: README.md
KHOG: CHANGELOG.md
```

## File Extensions

```yaml
SKWR-FPB: json # over writes uppercase version of JSON
KWRAUPL: yaml
```

## C Programming

```yaml
STR                :  {^}str
STR/KOP            :  {^}strcpy({^}
STR/HREPB          :  {^}strlen({^}
STR/KOPB           :  {^}strncpy({^}
STR/KPH-P          :  {^}strcmp({^}
STR/TOBG           :  {^}strtok({^}
PHEPL/SET          :  {^}memset({^}
TP*R               :  {^}for(int i=0;i<{^}
TP*R/TP*R          :  {^};i++)\\n
ST-D/RO*ER         :  stderr
ST-D/O*UT          :  stdout
*ED                :  {^};\\n{^}  # end line with semicolon and new line
#*ED               :  {^};{^}  # end line with semicolon
*EDZ               :  {^});\\n{^} # end line with closing parentheses and semicolon and new line
#*EDZ              :  {^});{^} # end line with closing parentheses and semicolon
PHAO*EBG           :  -=
PHRAO*EBG          :  +=
TPH*UL             :  "\\{'\\0'\\}" # Print {'\0'}, this needs to be quoted
TPH*UL/TPH*UL      :  "'\\0'"       # Print '\0', this needs to be quoted
KHR*U/ST*D         :  {^}\#include <stdio.h>\\n\#include <stdlib.h>\\n
KHR*U/STR*EUPBG    :  {^}\#include <string.h>\\n
EUPBT/PHAEUPB      :  {^}int main()\\n\\{\\n
EUPBT/PHAEUPB/ARG  :  {^}int main(int argc, char *argv[])\\n\\{\\n
PR*EUF             :  {^}printf(\"{^}
TPR*EUF            :  {^}fprintf(stderr, \"{^}
KHROET             :  {^}\",{^ ^}  # Klote... Closing quote with comma
KPHAEUBG           :  cmake
KPHAEUBG/KPHAEUBG  :  CMakeLists.txt
TP/TP              :  {^}\#if
EFPBD              :  {^}\#endif\\n
*EFPBD             :  {^}\#endif
TK*UF              :  {^}\#define
*EUF               :  {^}if ({^}
EFL                :  {^}\\}\\nelse if({^}
E8S                :  {^}else\\n\\{\\n
-PBD               :  {^})\\n\\{\\n
-PBD/-PBD          :  {^})\\n
TPR-R              :  {=1234/some/none}
```

## C Sharp

```yaml
SHA*RP          : csharp
SPROPBLG        : {^}.csproj{^}
KA*UPBT : const
HRAO*EPBG       : Linq
SHA*RP/SHA*RP   : C\#
TPAUR           : =>
O/STR*EUPBG     : {^}.ToString()
TKOT/TPHET      : dotnet
TKOT/TPHET/TPHU : dotnet new
TKOT/TPHET/TPHU/KOPBS : dotnet new console --framework net6.0
TKOT/TPHET/TPHU/HREUB : dotnet new classlib --framework net6.0
TPRAOEFP        : {^}foreach(var{^ ^}
```

## Lua

```yaml
HRAOU: lua
```

## Terminal

### General

```yaml
EBG                :  echo{^ ^}
KR*D               :  cd{^ ^}
R-PL               :  rm{^ ^}
PH-BG/TKEUR        :  mkdir{^ ^}
T*ERPL             :  terminal
KHRAO*EU           :  CLI
PW-RB              :  PowerShell
PHUBGS             :  tmux
PROE/TOE/SAOE      :  protoc
PROE/TOE/PWUF      :  protobuf
TKPWO*             :  {./^}
H-F                :  {^}{\#Control(c)}{^}
```

### Getting Help

```yaml
KHAO*ET                  :  {^}cht.sh {^ ^} # Run script on Linux
KHAO*ET/KHAO*ET          :  {^}curl cht.sh/{^}{MODE:SET_SPACE:+} # Again Linux but using curl
KHAO*ET/KHAO*ET/KHAO*ET  :  {^}(curl cht.sh/).Content{\#Left}{\#Left}{\#Left}{\#Left}{\#Left}{\#Left}{\#Left}{\#Left}{\#Left}{^}{MODE:SET_SPACE:+} # For use on windows
T*ERB                    :  {^}nc termbin.com 9999
T*ERB/T*ERB              :  https://termbin.com/{^}
```

### Names Of Programs That Are Not Used In A Shell Command Manner

```yaml
A/HRABG: Alacritty
```

### Linux Shell Scripting

```yaml
TP*EU    : {^}fi
AO*EF    : env
AO*EF/AO*EF    : {^}$env:{^}
HO*EPL    : {^}~/{^}
HO*EPL/HO*EPL    : {^}$HOME/{^}
HO*EPL/HO*EPL/HO*EPL  : {^}192.168.{^}
AUBG/AUBG : {^}awk \'\\{print $1\\}\'{^ ^}
AUBG/AUBG/AUBG : {^}awk \'/search/ \\{print $1\\}\'{^}
HR-PT : {^}lftp
KR*D  : {^}cd
PHO*FBG : {^}mosquitto_sub -h \"192.168.100.35\" -t \"topic\"
PHOFBG : {^}mosquitto_pub -h \"192.168.100.35\" -t \"topic\" -m \"Hi\"
```

### Windows Shell Scripting

```yaml
AUPT : {^}APPDATA{^}
A*UPT : {^}LOCALAPPDATA{^}
```

## tmux

```yaml
-FP : {^}{\#Control_R(u)}{^}
-PL : {^}{\#Control_R(d)}{^}
```

## Vim

### Operators

```yaml
KWO*RD   :  {^ciw^}
KR*EU    :  {^ci^}
KWR*EU   :  {^yi^}
SR*EU    :  {^vi^}
TK*EU    :  {^di^}
KRA*     :  {^ca^}  # Overwrites California
KWRA*    :  {^ya^}  # Overwrites suffix 'ia'
SRA*     :  {^va^}  # Overwrites Virginia
TKA*     :  {^da^}
TKPW-PL  :  {^gc^}  # Line wise comment operator. GM doesn't really mean anything.
TKPW*PL  :  {^gb^}  # Block wise comment operator. GM doesn't really mean anything.
```

### Commands

```yaml
PHAOEUFP       :  "{#Escape}{^zz^}{PLOVER:SET_CONFIG:'translation_frame_opacity':100}"  # This command is meant to save my file in vim and reload Plover
K-PL           :  {^gcc^} # Comment current line in line wise style
K*PL           :  {^gbc^} # Comment current line in block wise style
TKHRAO*ET      :  ^dd^ # Delete line
PR*EPL         :  {\#Escape}:%smagic/
STPA           :  {\#Escape}{^zz^} # Mapped in vim to :update<CR>
STPHA          :  {\#Escape}{^ZZ^}
KW*EUT         :  {\#Escape}:q\\n{^}
TPH*EUPL       :  nvim{^ ^}
TPH*EUPL/RAED  :  {^}nvim README.md
TPHOEUPL       :  neovim # sounds like 'noim'
SREUPL         :  vim    # Swap with victim as I use this more
SR*EUPL        :  victim # Swap with vim as I use this less
HRAO*ERD       :  {^}<leader>{^}
KR-R           :  {^}<CR>{^}
HRAOUF         :  {^}luafile %{^}
```

### Personal Mappings That Need To Be Fast

```yaml
KH*EBGD            :  {^},vl{^} # Mark down check box
TRAO*E             :  {^},fe{^} # File tree toggle
T*EFT              :  {^},ui{^} # Test
R*UPB              :  {^},uu{^} # Run
PW-D               :  {^},u;{^} # Build
KW*EUBG            :  {^},lA{^} # LSP code action
TKPW*URB           :  {^},gp{^} # Git push (gush)
TPO*RPLT           :  {^},lf{^} # Format code
TKPW*URB/TKPW*URB  :  git push
TKPW*UL            :  {^},gP{^} # Git pull (gull)
TKPW*UL/TKPW*UL    :  git pull
PHRA*US            :  {^}vip:s/{^}   # 'plahs' for selecting paragraph and start replace
HRA*US             :  {^}gv:s/{^}    # 'lahs' for selecting previous selection and start replace
TPAO*EUL           :  {^},fF{^} # File search
TKPWAO*EUL         :  {^},fG{^} # (Guiles) File search for git files
PW*UFR             :  {^},fb{^} # Search buffers
TKPWR*EP           :  {^},fg{^} # Grep files command
TK*EUFR            :  {^},gd{^} # Call plugin DiffViewOpen
TKPW*EUT           :  {^},gg{^} # Call plugin neogit
```

### Other Vim Programs

```yaml
SRAOEB : Vieb
SRAOEP : Vieb
```

### Remapped Finger Spelling

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

## Git

```yaml
TKPWEUT                     :  git
ST*TS                       :  status
TKPWEUT/TKEUF               :  git diff
TKPWA*P                     :  add .
TKPWEUT/ST*TS               :  git status
TKPWEUT/TKPWEUT             :  git status\\n{^}
PHERPBLG                    :  merge
TKPWEUT/TKEUF/H-PBZ/KAERBD  :  git diff --cached
TKPWEUT/KPHEUT/H-PBS/SR*    :  git commit -v
TKPWEUT/KHEBG/O*UT          :  git checkout
TKPWEUT/KHEBGT/PW*          :  git checkout -b{^ ^}
TKPWEUT/PHERPBLG            :  git merge
TKPWEUT/AD                  :  git add
TKEUF                       :  diff
TKEUF/H-PBZ/KAERBD          :  diff --cached
KPHEUT/H*PB/SR*             :  commit -v
PURB/O*RPBLG/PHAFRT         :  push origin master
PUL/H-PBZ/RE/PWAEUS         :  pull --rebase
HROG/H*PB/P*                :  log -p
RE/SET/KPA*E/HED/KR-RT      :  reset HEAD ^
```

## General Use

```yaml
TPRAEUR  :  firmware
SWAEUR   :  software
TKRAEUR  :  hardware
S*UP     :  software update
TP*UP    :  firmware update
TKR*UP   :  hardware update
PHA*     :  mA # Milliamp
PHAO*EU  :  uA # Microamp
```
