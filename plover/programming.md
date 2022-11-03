# Programming Dictionary

## Frequently Used Words

```yaml
RAO*T: reboot # This word should be one stroke!
RAOEBT: reboot
KRORPL: cross platform
ARGS: args
KAO*UT: execute
KAOUBL: executable
SEUS/HROG: syslog
SHROG: syslog
RAOES: release
```

## Linux

```yaml
HREUBGS : Linux
PHAPB/SKWRA*R : Manjaro
TPOEUD : Fedora # Replaces "for identification"
SOEUD : {^}sudo
W-LS : [wsl](wsl)
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
PHABG : mac
PHABGD : mac address
KEUG    : config # Overwrites: can Iing
K*EUG   : {^}Config # Overwrites: Qiing
HROEUPBG : lat/long
```

## Numbers

```yaml
H*EBGS : {^}0x{^}
```

## Units

```yaml
H*ERTS : Hz
```

## Common File Names

```yaml
RA*ED: README.md
KHOG: CHANGELOG.md
TPH*EUT/TPH*EUT : {^}init.lua
```

## File Extensions

```yaml
SKWR-FPB: json # over writes uppercase version of JSON
KWRAUPL: {^}.yaml{^}
KR*S: {^}.cs{^}
PH-D : {^}md{^}
PH*D : {^}md{^}
TK-L : {^}.dll{^}
EBGS/EBGS : {^}.exe{^}
```

## C Programming

```yaml
STR                :  {^}str
STR/KOP            :  {^}strcpy({^}
STR/HREPB          :  {^}strlen({^}
STR/KOPB           :  {^}strncpy({^}
STR/KPH-P          :  {^}strcmp({^}
STR/TOBG           :  {^}strtok({^}
ST-D/RO*ER         :  stderr
STKER              :  stderr
ST-D/O*UT          :  stdout
STKOUT             :  stdout
STKEUPB            :  stdin
ST-D/EUPB          :  stdin
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
```

## Databases

```yaml
PHEU/SKW-L : MySQL
SKW*L : sql
```

## C Sharp

```yaml
PR-PLS                : {^}Program.cs
SHA*RP                : csharp
SPROPBLG              : {^}.csproj{^}
KA*UPBT               : const
HRAO*EPBG             : Linq
SHA*RP/SHA*RP         : C\#
TPAUR                 : {^ ^}=>{^ ^}
O/STR*EUPBG           : {^}.ToString()
TKOT/TPHET            : dotnet
TKOT/TPHET/TPHU       : dotnet new
TKRUPB                : dotnet run\\n
TKOT/TPHET/TPHU/KOPBS : dotnet new console --framework net6.0
TKOT/TPHET/TPHU/HREUB : dotnet new classlib --framework net6.0
TKOFP                 : dotnet watch run
AF/HROEPB/KWRA        : Avalonia
```

## Lua

```yaml
HRAOU: lua
```

## Go

### Hugo

```yaml
HAO*UG : hugo
HAO*UG/HAO*UG : {^}hugo server -D
HAO*UG/HAO*UG/HAO*UG : hugo server --bind $(hostname -I | tr -d ' ') --baseURL=http://$(hostname -I | tr -d ' ') -D
```

## Terminal

### General

```yaml
T*ERPL             :  terminal
KWOEUBG            :  {^}qmk
KHRAO*EU           :  CLI
PW-RB              :  PowerShell
PROE/TOE/SAOE      :  protoc
PROE/TOE/PWUF      :  protobuf
PROEUT             :  proto
TKPWO*             :  {./^}
H-F                :  {^}{\#Control(c)}{^}
```

### Getting Help

This makes using the terminal cheat tool very easy. See
[cht.sh](https://cht.sh/)

```yaml
KHAO*ET                  :  {^}cht.sh {^ ^} # Run script on Linux
KHAO*ET/KHAO*ET          :  {^}curl cht.sh/{^}{MODE:SET_SPACE:+} # Again Linux but using curl
KHAO*ET/KHAO*ET/KHAO*ET  :  {^}(Invoke-WebRequest cht.sh/).Content{\#Left}{\#Left}{\#Left}{\#Left}{\#Left}{\#Left}{\#Left}{\#Left}{\#Left}{^}{MODE:SET_SPACE:+} # For use on windows, need to use Invoke-WebRequest instead of the alias curl to work on all PowerShell versions
T*ERB                    :  {^}nc termbin.com 9999
T*ERB/T*ERB              :  https://termbin.com/{^}
```

### Names Of Programs That Are Not Used In A Shell Command Manner

```yaml
A/HRABG: Alacritty
```

### Linux Shell Scripting

#### Main terminal commands

```yaml
EBG                                                               :  {^}echo {^ ^}
KR*D/TKPW*EUT                                                     :  {^}cd $(git rev-parse --show-toplevel)\\n{^}
KR*D                                                              :  {^}cd {^ ^}
KR*D/KR*D                                                         :  {^}cd ../
KR*D/KR*D/KR*D                                                    :  {^}cd ../../
KR*D/KR*D/KR*D/KR*D                                               :  {^}cd ../../../
KR*D/KR*D/KR*D/KR*D/KR*D                                          :  {^}cd ../../../../
KR*D/KR*D/KR*D/KR*D/KR*D/KR*D                                     :  {^}cd ../../../../../
KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D                                :  {^}cd ../../../../../../
KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D                           :  {^}cd ../../../../../../../
KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D                      :  {^}cd ../../../../../../../../
KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D                 :  {^}cd ../../../../../../../../../
KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D            :  {^}cd ../../../../../../../../../../
KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D       :  {^}cd ../../../../../../../../../../../
KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D  :  {^}cd ../../../../../../../../../../../../
PH*F                                                              :  {^}mv {^ ^}
R-PL                                                              :  {^}rm {^ ^}
PH-BG/TKEUR                                                       :  {^}mkdir {^ ^}
TP*EU                                                             :  {^}fi{^ ^}
HR-PT                                                             :  {^}lftp {^ ^}
```

#### Command macros

```yaml
HO*EPL               : {^}~/{^}
HO*EPL/HO*EPL        : {^}$HOME/{^}
HO*EPL/HO*EPL/HO*EPL : {^}192.168.{^}
AUBG/AUBG            : {^}awk \'\\{print $1\\}\'{^ ^}
AUBG/AUBG/AUBG       : {^}awk \'/search/ \\{print $1\\}\'{^}
PHO*FBG              : {^}mosquitto_sub -h \"192.168.100.35\" -t \"topic\"
PHOFBG               : {^}mosquitto_pub -h \"192.168.100.35\" -t \"topic\" -m \"Hi\"
```

### PowerShell/Pwsh Scripting

```yaml
AUPT                 :  {^}APPDATA{^}
A*UPT                :  {^}LOCALAPPDATA{^}
AO*EF                :  env
AOEF                 :  {^}$env:{^}
AOEF/AOEF            :  {^}$env:APPDATA{^}
AOEF/AOEF/AOEF       :  {^}$env:LOCALAPPDATA{^}
AOEF/AOEF/AOEF/AOEF  :  {^}$env:USERPROFILE{^}
```

## tmux

```yaml
PHUBGS  : tmux
PH*UBGS : {^}{\#Control_R(a)}{^} # tmux prefix
KW*EU   : {^}{\#Control_R(a)}j{^} # Open my wiki in new tmux window
```

## Git

```yaml
TKPW*EUT/HO*EPL             :  {^}cd $(git rev-parse --show-toplevel)\\n{^}
TKPWUB                      :  GitHub
TKPWUB/TKPWUB               :  https://github.com/{^}
TKPWUB/TKPWUB/TKPWUB        :  "git@github.com:{^}"
TKPWHRAB                    :  GitLab
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

## Hardware Software Firmware Items

```yaml
TPRAEUR   : firmware
SWAEUR    : software
TKRAEUR   : hardware
S*UP      : software update
TP*UP     : firmware update
TKR*UP    : hardware update
TPHRAO*ES : firmware release
SHRAO*ES  : software release
TKHRAOES  : hardware release
PHA*      : mA # Milliamp
PHAO*EU   : uA # Microamp
```
