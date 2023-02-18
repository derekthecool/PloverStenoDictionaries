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
TPHEUT: init
TPEG: ffmpeg
RA*EU : array
ARG : arg
TKOEURBG : docker
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

## Programming Terms

```yaml
TAOUPL : tuple
```

## Numbers

```yaml
H*EBGS : {^}0x{^}
```

## Units

```yaml
H*ERTS : Hz
HERTS : Mz
PHERTS : MHz
TKPWRERTS : GHz
```

## Common File Names

```yaml
RA*ED: README.md
KHOG: CHANGELOG.md
TPH*EUT/TPH*EUT : {^}init.lua
```

## File Extensions

This list contains pairs of file extensions. The first is a without a period,
the second does have a period. I use the `#` key to add the period, this may
cause some conflicts with my number dictionary.

```yaml
SKWR-FPB: json # over writes uppercase version of JSON
#SKWR-FPB: {^}.json{^}
KWRA*PL: {^}yaml{^}
#KWRA*PL: {^}.yaml{^}
KR*S: {^}cs{^}
#KR*S: {^}.cs{^}
TP*S : {^}fs{^}
#TP*S : {^}.fs{^}
TP*BGS : {^}fsx{^}
#TP*BGS : {^}.fsx{^}
PH*D : {^}md{^}
#PH*D : {^}.md{^}
TK*L : {^}dll{^}
#TK*L : {^}.dll{^}
KAO*UBL : {^}exe{^}
#KAO*UBL : {^}.exe{^}
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
PHAEUPBS           :  {^}main.c{^}
PRAG/PHA           :  {^}\#pragma once
```

### Microcontroller Specific

#### ESP32

```yaml
23EUS : {^}ESP32{^}
*EUFD : {^}idf.py
```

## Databases

```yaml
PHEU/SKW-L : MySQL
SKW*L : sql
```

## Dotnet

There are 3 main languages here which all share some similar items.

- PowerShell
- Csharp
- Fsharp

```yaml
AFP : asp
AFP/TPHET : asp.net
AFP/TKOT/TPHET : asp.net
```

### Dotnet

```yaml
TPHAOUGT : nuget
TPHU/TKPWET : nuget
```

### Dotnet Cli Commands

```yaml
TPH*ET                : dotnet
TPH*ET/TPHU           : dotnet new
TPH*ET/RUPB           : dotnet run\\n
TPH*ET/PWEULD         : dotnet build\\n
TPH*ET/KOPBLS         : dotnet new console --framework net6.0
TPH*ET/KHRAS          : dotnet new classlib --framework net6.0
TKOT/TPHET            : dotnet
TKOT/TPHET/TPHU       : dotnet new
TKRUPB                : dotnet run\\n
TKOT/TPHET/TPHU/KOPBS : dotnet new console --framework net6.0
TKOT/TPHET/TPHU/HREUB : dotnet new classlib --framework net6.0
TKOFP                 : dotnet watch run
```

### Dotnet Functions

```yaml
RAED/HRAOEUPB : ReadLine
```

## C#

```yaml
PR-PLS                : {^}Program.cs
SHA*RP                : csharp
SHA*RP/SHA*RP         : C\#
SPROPBLG              : {^}.csproj{^}
KA*UPBT               : const
TPHAOEBG: {^ ^}!={^ ^}
TPHAEUS: namespace
TPHAOEBLG: {^ ^} != null{^}
KOPBLS                : console
HRAO*EPBG             : Linq
TPAUR                 : {^ ^}=>{^ ^} # fat arrow
O/STR*EUPBG           : {^}.ToString()
AF/HROEPB/KWRA        : Avalonia
```

## F#

```yaml
TPA*RP  : fsharp
TPA*RP/TPA*RP  : F\#
SAO*EBG : Seq.{^}
TP*TS : fst # keyword for first item in a tuple
S*PBD : snd # keyword for second item in a tuple
TPHAOEFBG : {^ ^}<>{^ ^} # "neeq" not equal for fsharp which is very weird looking (add the f to the sound for fsharp)
```

## Lua

```yaml
HRAOU: lua
TPHAO*EBG: {^ ^}~={^ ^}
TPHAO*EBLG: {^ ^}~= nil{^}
```

## Go

### Hugo

```yaml
HAO*UG : hugo
HAO*UG/HAO*UG : {^}hugo server -D
HAO*UG/HAO*UG/HAO*UG : hugo server --bind $(hostname -I | tr -d \' \') --baseURL=http://$(hostname -I | tr -d \' \') -D
```

## Terminal

### General

```yaml
T*ERPL             :  terminal
KWOEUBG            :  {^}qmk
KHRAO*EU           :  CLI
PW-RB              :  powershell
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
PROBGS : Proxmox
```

### Linux Shell Scripting

#### Main terminal commands

```yaml
EBG                                                               :  {^}echo {^ ^}
KR*D/TKPW*EUT                                                     :  {^}cd $(git rev-parse --show-toplevel)\\n{^}
KR*D                                                              :  {^}cd {^ ^}
KR*D/KR*D                                                         :  {^}cd ../{^}
KR*D/KR*D/KR*D                                                    :  {^}cd ../../{^}
KR*D/KR*D/KR*D/KR*D                                               :  {^}cd ../../../{^}
KR*D/KR*D/KR*D/KR*D/KR*D                                          :  {^}cd ../../../../{^}
KR*D/KR*D/KR*D/KR*D/KR*D/KR*D                                     :  {^}cd ../../../../../{^}
KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D                                :  {^}cd ../../../../../../{^}
KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D                           :  {^}cd ../../../../../../../{^}
KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D                      :  {^}cd ../../../../../../../../{^}
KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D                 :  {^}cd ../../../../../../../../../{^}
KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D            :  {^}cd ../../../../../../../../../../{^}
KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D       :  {^}cd ../../../../../../../../../../../{^}
KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D/KR*D  :  {^}cd ../../../../../../../../../../../../{^}
PH*F                                                              :  {^}mv {^ ^}
R-PL                                                              :  {^}rm {^ ^}
R-PL/R-PL                                                         :  {^}rm -rf{^ ^}
PH-BG/TKEUR                                                       :  {^}mkdir {^ ^}
TP*EU                                                             :  {^}fi{^ ^}
HR-PT                                                             :  {^}lftp {^ ^}
TP-PLT                                                            :  {^}lftp {^ ^} # TP-PT (FTP) + L = TP-PLT = lftp
S-PL/KR-LT : systemctl
S-PL/KR-LT/ST*TS : systemctl status
S-PL/KR-LT/TPHAEUBL : systemctl enable
S-PL/KR-LT/START : systemctl start
S-PL/KR-LT/STOP : systemctl stop
KPHR-R : {^}xplr # Awesome terminal file manager
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
TKPWEUT/PWAEUR/RE/PO        :  git bare repo
TKPW*EUT/HO*EPL             :  {^}cd $(git rev-parse --show-toplevel)\\n{^}
TKPWUB                      :  GitHub
AZ/SHUR                     :  Azure
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
SPOET     : SpO2
SPAO*EU   : spi
AOEUBG/AOEUBG : I2C
ROEUT : resistor
KOEUP : capacitor
TKOEUR : inductor
SKR-L : SCL
STKA : SDA
AOEUBG/AOEUBG/AOEUBG : IIC
TK*B: dB
A*FPLT/TK*FPLT/KR*FPLT : ADC
AOEU/OE : IO
```

## Clash Of Code

[Clash of code](https://www.codingame.com/multiplayer/clashofcode) is an online
multiplayer coding game.

From there own description

> Clash of Code is a game to improve your coding efficiency by solving short
> programming problems with other people, at the same time. Players share their
> solution at the end of a game to help other players improve their coding skills.

They provide a pretty good web editor complete three editor modes

1. Default mode which is akin to VSCode
2. Vim mode
3. Emacs mode

In the past I've been okay with using their vim mode. But in my journey to make
things even more comfortable I've made my own special vim mode.

My special vim mode includes me using my own personal vim setup then copying the
text to the web editor and running it.
I've broken the commands needed to do this into two steps. Possibly using the
Plover delay plugin could help me get down to one stoke but two is fine for now.

```yaml
KHRA*RB : {\#Alt(a)}{\#Escape}:%y+\\n # Select my first monitor is input keys to copy my entire buffer
KHRA*RB/KHRA*RB : {\#Alt(o)}{\#Control(a)}{\#Control(v)}
KHRA*RB/KHRA*RB/KHRA*RB : {\#Control(Shift(return))}{\#Alt(a)} # Select second monitor and replace old text with new and run the tests
```

## Added by Plover

```yaml
HROEFT: localhost
PW*RB: pwsh
APT/APT: {^}sudo apt update && sudo apt upgrade -y
A*PT/A*PT: {^}apt update && apt upgrade -y
APT/APT/APT: {^}sudo apt upgrade -y
A*PT/A*PT/A*PT: {^}apt upgrade -y
APT/APT/APT/APT: {^}sudo apt update
A*PT/A*PT/A*PT/A*PT: {^}apt update
AO*URS: {^}usr
```
