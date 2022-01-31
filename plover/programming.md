# Programming Dictionary

SKW-T: \' # single quote character
KR-GS: \" # double quote character
PW-RB: \\ # backslash
HAERB: \# # hash character on the right hand side
'#-T': 9 # you should not escape the # in strokes

## C Programming

```yaml
STR                :  {^}str
STR/KOP            :  {^}strcpy({^}
STP/KOPB           :  {^}strncpy({^}
PHEPL/SET          :  {^}memset({^}
TP*R               :  {^}for(int i=0;i<{^}
TP*R/TP*R          :  {^};i++)\\n
ST-D/RO*ER         :  stderr
ST-D/O*UT          :  stdout
ED                 :  {^};\\n{^}  # end line with semicolon
EDZ                :  {^});\\n{^} # end line with closing parentheses and semicolon
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
```

## C Sharp

```yaml
O/STR*EUPBG    : {^}.ToString()
```

## Terminal

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

## Vim

```yaml
PHAOEUFP   : "{#Escape}{^zz^}{PLOVER:SET_CONFIG:'translation_frame_opacity':100}"  # Commands like this require quote wrapping like this
TKHRAO*ET  :  ^dd^
KWO*RD     :  {\#Escape}{^ciw^}
PR*EPL     :  {\#Escape}:%smagic/
STPA       :  {\#Escape}{^zz^} # Mapped in vim to :update<CR>
STPHA      :  {\#Escape}{^ZZ^}
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
