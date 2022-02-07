# Programming Dictionary

SKW-T: \' # single quote character
KR-GS: \" # double quote character
PW-RB: \\ # backslash
HAERB: \# # hash character on the right hand side
'#-T': 9 # you should not escape the # in strokes

## Technical Jargon

```yaml
PH*BG : MQTT
TAOEP : TCP
TAOEP/TAOEP : TCP/IP
HREUBGS : Linux
```

## C Programming

```yaml
STR                :  {^}str
STR/KOP            :  {^}strcpy({^}
STR/HREPB          :  {^}strlen({^}
STR/KOPB           :  {^}strncpy({^}
STR/KPH-P          :  {^}strcmp({^}
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
 is none none some 1234

## C Sharp

```yaml
O/STR*EUPBG    : {^}.ToString()
TKOT/TPHET     : dotnet
TKOT/TPHET/TPHU : dotnet new console --framework net6.0
```

## Terminal

### General

```yaml
EBG                :  echo
KHRAOEU            :  terminal
KHRAO*EU           :  CLI
PW-RB              :  PowerShell
PHUBGS             :  tmux
PROE/TOE/SAOE      :  protoc
PROE/TOE/PWUF      :  protobuf
TKPWO*             :  {./^}
```

### Linux Shell Scripting

```yaml
AUBG/AUBG : {^}awk \'\\{print $1\\}\'{^ ^}
AUBG/AUBG/AUBG : {^}awk \'/search/ \\{print $1\\}\'{^}
HR-PT : {^}lftp
KR*D  : {^}cd
PHOFBG : {^}mosquitto_sub -h \"192.168.100.35\" -t \"topic\"
PHOFBG : {^}mosquitto_pub -h \"192.168.100.35\" -t \"topic\" -m \"Hi\"
```

## Vim

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

### Commands

```yaml
PHAOEUFP   : "{#Escape}{^zz^}{PLOVER:SET_CONFIG:'translation_frame_opacity':100}"  # Commands like this require quote wrapping like this
TKHRAO*ET  :  ^dd^
KWO*RD     :  {\#Escape}{^ciw^}
PR*EPL     :  {\#Escape}:%smagic/
STPA       :  {\#Escape}{^zz^} # Mapped in vim to :update<CR>
STPHA      :  {\#Escape}{^ZZ^}
SREUPL     :  vim    # Swap with victim as I use this more
SR*EUPL    :  victim # Swap with vim as I use this less
```

## Git

```yaml
TKPWEUT                                  : git
ST*TS                                    : status
TKPW*EUT/TKEUF                           : git diff
TKPWEUT/ST*TS                            : git status
PHERPBLG                                 : merge
TKPWEUT/TKEUF/H-PBZ/KAERBD               : git diff --cached
TKPWEUT/KPHEUT/H-PBS/SR*                 : git commit -v
TKPWEUT/KPHEUT/H-PBS/SR*/H-PBZ/APLD      : git commit -v --amend
TKPWEUT/KHEBG/O*UT                       : git checkout
TKPWEUT/KHEBG/O*UT/H-PBS/PW*             : git checkout -b
TKPWEUT/PHERPBLG                         : git merge
TKPWEUT/HUB                              : GitHub
TKPWEUT/AD                               : git add
TKEUF                                    : diff
TKEUF/H-PBZ/KAERBD                       : diff --cached
KPHEUT/H*PB/SR*                          : commit -v
KHEBG/SKWROUT/H*PB/PW*/HOT/TK-LS/TPEUBGS : checkout -b hotfix
PURB/O*RPBLG/PHAFRT                      : push origin master
PUL/H-PBZ/RE/PWAEUS                      : pull --rebase
HROG/H*PB/P*                             : log -p
RE/SET/KPA*E/HED/KR-RT                   : reset HEAD ^
RE/SET/H-PBZ/HARD/O*RPBLG/OEU/PHAFRT     : reset --hard origin/master
AD/-P                                    : add .
```

## General Use

```yaml
S*UP     :  software update
TPRAEUR  :  firmware
TPUP     :  firmware update
PHA*     :  mA # Milliamp
PHAO*EU  :  uA # Microamp
```
