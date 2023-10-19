# Programming Dictionary

## Common To Most Languages

```yaml
PHRAOEBG : +=
```

## Frequently Used Words

```yaml
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
WAEUS : workspace
WAEURS : workspacer
```

## Containerization Applications

Quick commands for container programs docker and podman.

Wow, getting `\t` to print correctly in the `ps` command below was hard. Check
it out for reference. I used this [guide](https://stackoverflow.com/questions/50667371/docker-ps-output-formatting-list-only-names-of-running-containers)
for the better `ps` printing.

```yaml
KAEURPB : container # Overwrites Karen
TKPW*ET/TK-BG : curl -sSL https://get.docker.com/ | sh # Easy script to install docker and docker compose
TK-BG : docker{^ ^}
TK-BG/UP : docker-compose up --build
TK-BG/*UP : docker compose up --build
TK-BG/TKOUPB : docker-compose down
TK-BG/TKO*UPB : docker compose down
TK-BG/P : "docker ps --format 'table \\{\\{.ID\\}\\}{#Backslash}{^t^}\\{\\{.Image\\}\\}{#Backslash}{^t^}\\{\\{.Status\\}\\}{#Backslash}{^t^}\\{\\{.Names\\}\\}'\\n{^}"
TK-BG/P-S : "docker ps --format 'table \\{\\{.ID\\}\\}{#Backslash}{^t^}\\{\\{.Image\\}\\}{#Backslash}{^t^}\\{\\{.Status\\}\\}{#Backslash}{^t^}\\{\\{.Names\\}\\}'\\n{^}"
TK-BG/RUPB : docker run -it{^ ^}
TK-BGZ     :  {^}{\#Control(p q)}{^} # Exit container without stopping it - requires starting container with interactive mode (-it)
TKAO*EUL : Dockerfile
KPO*ES : compose.yaml # The official recommended docker compose file name. Not docker-compose.yaml, docker-compose.yml, or compose.yml
P-D : podman{^ ^}
P-D/UP : podman-compose up --build
P-D/*UP : podman compose up --build
P-D/TKOUPB : podman-compose down
P-D/TKO*UPB : podman compose down
P-D/P : "podman ps --format 'table \\{\\{.ID\\}\\}{#Backslash}{^t^}\\{\\{.Image\\}\\}{#Backslash}{^t^}\\{\\{.Status\\}\\}{#Backslash}{^t^}\\{\\{.Names\\}\\}'\\n{^}"
P-D/P-S : "podman ps --format 'table \\{\\{.ID\\}\\}{#Backslash}{^t^}\\{\\{.Image\\}\\}{#Backslash}{^t^}\\{\\{.Status\\}\\}{#Backslash}{^t^}\\{\\{.Names\\}\\}'\\n{^}"
P-D/RUPB : podman run -it{^ ^}
P-DZ     :  {^}{\#Control(p q)}{^} # Exit container without stopping it - requires starting container with interactive mode (-it)
```

## Linux

```yaml
HREUBGS : Linux
PHAPB/SKWRA*R : Manjaro
TPOEUD : Fedora # Replaces "for identification"
SOEUD : {^}sudo
W-LS : wsl
```

## Technical Jargon

```yaml
AOU/ART: uart
KPAP: pcap
PH*BG : mqtt
PH*BG/PH*BG : lwt
PH*BG/PH*BG/PH*BG : QoS
KWOS : qos
TAOEP : tcp
TAOEP/TAOEP : tcp/ip
TAOEP/TK*UPL : tcpdump
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
K-B : KB
KEUB : KiB
PH-B : MB
PHEUB : MiB
TKPW-B : GB
TKPWEUB : GiB
T-B : TB
TEUB : TiB
P-B : PB
PEUB : PiB
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
SPROPBLG              : {^}.csproj{^}
TPROPBLG              : {^}.fsproj{^}
P-S/1 : {^}.ps1
KPR-P : {^}cpp
KPR*P : {^}.cpp
KO*FPB : {^}conf
#KO*FPB : {^}.conf
```

## C Programming

### General

```yaml
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
TPHOEUL            :  NULL
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
PHAEUPBS           :  {^}main.c{^}
PRAG/PHA           :  {^}\#pragma once
S*RS : src
STKEUPBT           : STDINT{^} # Meant to trigger a snippet for uint8_t and family
STK*EUPBT          : USTDINT{^} # Meant to trigger a snippet for uint8_t and family
TOEUF : typedef
TAOEUP/TKEF : typedef
SOF : sizeof
#SO*F : {^}SIZEOF # Meant to trigger a snippet for sizeof
```

### string.h

```yaml
KHR*U/STR*EUPBG    :  {^}\#include <string.h>\\n
STR                :  {^}str
STR/KOP            :  {^}strcpy({^}
STR/HREPB          :  {^}strlen({^}
STR/KOPB           :  {^}strncpy({^}
STR/KPH-P          :  {^}strcmp({^}
STR/TOBG           :  {^}strtok({^}
PHEPL              : mem{^} # Replaces "member", more important as mem
PHEPL/KO*EP        : memcpy
```

### stdlib.h

```yaml
PHOEUBG : malloc
ROEUBG : realloc
KROEUBG : calloc
```

### Microcontroller Specific

#### ESP32

```yaml
23EUS : ESP32
*EUFD : {^}idf.py
```

#### FreeRTOS

```yaml
TROS : RTOS
TROS/TROS : real time operating system
TPROS : FreeRTOS
```

## Databases

```yaml
PHEU/SKW-L : mysql
PHEU/SKW*L : MySQL
PH-S/SKW-L : mssql
PH-S/SKW*L : MSSQL
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
TPH*ET/SHRAOUGS/AD    : dotnet sln add
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
PRUF               :  protobuf
PROEUT             :  proto
TKPWO*             :  {./^}
H-F                :  {^}{\#Control(c)}{^}
```

### Getting Help

This makes using the terminal cheat tool very easy. See
[cht.sh](https://cht.sh/)

```yaml
KHAO*ET                  :  {^}curl cht.sh/{^}{MODE:SET_SPACE:+} # Again Linux but using curl
KHAO*ET/KHAO*ET          :  {^}(Invoke-WebRequest cht.sh/).Content{\#Left}{\#Left}{\#Left}{\#Left}{\#Left}{\#Left}{\#Left}{\#Left}{\#Left}{^}{MODE:SET_SPACE:+} # For use on windows, need to use Invoke-WebRequest instead of the alias curl to work on all PowerShell versions
KHAO*ET/KHAO*ET/KHAO*ET  :  {^}cht.sh {^ ^} # Run script on Linux (must be
T*ERB                    :  {^}nc termbin.com 9999
T*ERB/T*ERB              :  https://termbin.com/{^}
```

### Names Of Programs That Are Not Used In A Shell Command Manner

```yaml
A/HRABG: Alacritty
PROBGS : Proxmox
```

### Linux Shell Scripting

#### Backslash Alphabet

This collection of bashslashed letters is very helpful for these reasons:

- Writing newline chars such as `\r` or `\n`
- Writing regular expressions for pattern groups like `\w`, `\s`, `\d`, and
  their uppercase inverted countparts

Words/translations that I'll be replacing with this alphabet:

- a: apps,As
- b: BPs, bps
- c: cps,Cs
- d: depends,Ds
- e: especially,Es - especially cannot be remapped because it is too important
- f: fps,Fs
- g: GPS, global positioning system - both of these can't be remapped they are too important as well
- h: HPs,Hs
- i: IPs,Is
- j: s,Js
- k: companies,Ks
- l: ...,Ls
- m: PHPs,Ms
- n: /tmp/s, Ns
- o: Ops,Os
- p: .s, Ps
- q: (up arrow + s), Qs
- r: reasons,Rs
- s: , ,
- t: it happens,Ts
- u: ups,Us
- v: VPs,Vs
- w: WordPresses,Ws
- x: XPs,Xs
- y: s,Ys
- z: s,Zs

```yaml
A*PS : {^\\A^}
APS : {^\\a^}
PW*PS : {^\\B^}
PWPS : {^\\b^}
KR*PS : {^\\C^}
KRPS : {^\\c^}
TK*PS : {^\\D^}
TK-PS : {^\\d^}
*EPS : {^\\E^}
TP*PS : {^\\F^}
TP-PS : {^\\f^}
H*PS : {^\\H^}
H-PS : {^\\h^}
*EUPS : {^\\I^}
-EUPS : {^\\i^}
SKWR*PS : {^\\J^}
SKWRPS : {^\\j^}
K*PS : {^\\K^}
K-PS : {^\\k^}
HR*PS : {^\\L^}
HR-PS : {^\\l^}
PH*PS : {^\\M^}
PH-PS : {^\\m^}
TPH*PS : {^\\N^}
TPH-PS : {^}{\#Backslash}n{^} # Special to Plover, need to use this version instead
O*PS : {^\\O^}
O-PS : {^\\o^}
P*PS : {^\\P^}
P-PS : {^\\p^}
KW*PS : {^\\Q^}
KW-PS : {^\\q^}
R*PS : {^\\R^}
R-PS : {^}{\#Backslash}r{^} # Special to Plover, need to use this version instead
S*PS : {^\\S^}
S-PS : {^\\s^}
T*PS : {^\\T^}
T-PS : {^}{\#Backslash}t{^} # Special to Plover, need to use this version instead
*UPS : {^\\U^}
-UPS : {^\\u^}
SR*PS : {^\\V^}
SR-PS : {^\\v^}
W*PS : {^\\W^}
W-PS : {^\\w^}
KP*PS : {^\\X^}
KP-PS : {^\\x^}
KWR*PS : {^\\Y^}
KWR-PS : {^\\y^}
STKPW*PS : {^\\Z^}
STKPW-PS : {^\\z^}
```

#### Command-line Options Alphabet

It is extremely common to use command-line options. Such as `grep -P -u`
or maybe `bash -c`.

Using my normal approach with emily's symbols these kind of things often take
three strokes. For example:

1. `SKWHAPL` for ` -`
2. `P*` for `p`
3. `S-P` to insert a space after (my normal alphabet uses glue endings)

So it is advantageous to create a custom alphabet for this. I use the terminal
for everything on my computer so this is mission critical!

```yaml
A*FPLTD : {^ ^}-A
A*RBGSZ : {^ ^}-a
PW*FPLTD : {^ ^}-B
PW*RBGSZ : {^ ^}-b
KR*FPLTD : {^ ^}-C
KR*RBGSZ : {^ ^}-c
TK*FPLTD : {^ ^}-D
TK*RBGSZ : {^ ^}-d
*EFPLTD : {^ ^}-E
*ERBGSZ : {^ ^}-e
TP*FPLTD : {^ ^}-F
TP*RBGSZ : {^ ^}-f
TKPW*FPLTD : {^ ^}-G
TKPW*RBGSZ : {^ ^}-g
H*FPLTD : {^ ^}-H
H*RBGSZ : {^ ^}-h
*EUFPLTD : {^ ^}-I
*EURBGSZ : {^ ^}-i
SKWR*FPLTD : {^ ^}-J
SKWR*RBGSZ : {^ ^}-j
K*FPLTD : {^ ^}-K
K*RBGSZ : {^ ^}-k
HR*FPLTD : {^ ^}-L
HR*RBGSZ : {^ ^}-l
PH*FPLTD : {^ ^}-M
PH*RBGSZ : {^ ^}-m
TPH*FPLTD : {^ ^}-N
TPH*RBGSZ : {^ ^}-n
O*FPLTD : {^ ^}-O
O*RBGSZ : {^ ^}-o
P*FPLTD : {^ ^}-P
P*RBGSZ : {^ ^}-p
KW*FPLTD : {^ ^}-Q
KW*RBGSZ : {^ ^}-q
R*FPLTD : {^ ^}-R
R*RBGSZ : {^ ^}-r
S*FPLTD : {^ ^}-S
S*RBGSZ : {^ ^}-s
T*FPLTD : {^ ^}-T
T*RBGSZ : {^ ^}-t
*UFPLTD : {^ ^}-U
*URBGSZ : {^ ^}-u
SR*FPLTD : {^ ^}-V
SR*RBGSZ : {^ ^}-v
W*FPLTD : {^ ^}-W
W*RBGSZ : {^ ^}-w
KP*FPLTD : {^ ^}-X
KP*RBGSZ : {^ ^}-x
KWR*FPLTD : {^ ^}-Y
KWR*RBGSZ : {^ ^}-y
STKPW*FPLTD : {^ ^}-Z
STKPW*RBGSZ : {^ ^}-z
```

bash -A -B -C -D -E -F -G -H -I -J -K -L -M -N -O -P -Q -R -S -T -U -V -W -X -Y -Z
grep -a -b -c -d -e -f -g -h -i -j -k -l -m -n -o -p -q -r -s -t -u -v -w -x -y -z

#### Bash Scripting

```yaml
SHEB : \#!/usr/bin/env bash
SHEB/SHEB : \#!/bin/bash
SHEB/SHEB/SHEB : \#!/bin/sh
```

#### Common Directory Names

```yaml
PH-PBT : /mnt/{^}
ETS : /etc/{^}
URS : /usr/{^}
TPH-P : /tmp/{^}
```

#### Main terminal commands

```yaml
S*ED : sed
S*ED/S*ED : "sed 's/'{#Left}"
TKA*EUT : "date '+%F'"
TKA*EUT/TKA*EUT : "date '+%T'"
TKA*EUT/TKA*EUT/TKA*EUT : "date '+%F %T'"
SR*ERGS : --version\\n{^}
H*EP : --help\\n{^}
TP/KEUG : {^}ifconfig{^ ^}
HOEFT/TPHAEUPL : hostname
HAEUPL : hostname
HOEFT/TPHAEUPL/KR-LT : hostnamectl
HAEUPL/KR-LT : hostnamectl
KHOD : chmod +x{^ ^}
KPHOD : chmod +x{^ ^}
HR*S : ls
HR*S/HR*S : ls -la
HR*Z : ls\\n
TAR : tar xzvf
TAR/TAR : tar czvf
TAR/TAR/TAR : tar
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
KR-P                                                              :  {^}cp {^ ^}
PH*F                                                              :  {^}mv {^ ^}
R-PL                                                              :  {^}rm {^ ^}
R-PL/R-PL                                                         :  {^}rm -rf{^ ^}
PH-BG/TKEUR                                                       :  {^}mkdir {^ ^}
KEUR                                                              :  {^}mkdir {^ ^}
TP*EU                                                             :  {^}fi{^ ^}
HR-PT                                                             :  {^}lftp {^ ^}
TP-PLT                                                            :  {^}lftp {^ ^} # TP-PT (FTP) + L = TP-PLT = lftp
S-PL/KR-LT : systemctl
S-PL/KR-LT/ST*TS : systemctl status
S-PL/KR-LT/TPHAEUBL : systemctl enable
S-PL/KR-LT/START : systemctl start
S-PL/KR-LT/STOP : systemctl stop
KPHR-R : {^}xplr # Awesome terminal file manager
ABD : adb
ABD/ABD : adb devices\\n{^}
STKPW-P : {^}7z{^ ^}
```

#### [Wezterm](https://wezfurlong.org/wezterm/)

Wezterm is an amazing terminal emulator.

My configuration `WeztermStimpack` is [here](https://github.com/derekthecool/WeztermStimpack).

The two long commands are an easy way to download the latest stable release
AppImage and install to `/usr/bin` and make the file executable as well.

```yaml
WERPL : wezterm
WERPL/TKOUPBLD : curl -sL https://api.github.com/repos/wez/wezterm/releases/latest | grep -Po \'https://.*AppImage\' | sort -u | xargs -I \\{\\} wget \\{\\} -O /usr/bin/wezterm && chmod +x /usr/bin/wezterm && wezterm --version
TKPWET/WERPL : curl -sL https://api.github.com/repos/wez/wezterm/releases/latest | grep -Po \'https://.*AppImage\' | sort -u | xargs -I \\{\\} wget \\{\\} -O /usr/bin/wezterm && chmod +x /usr/bin/wezterm && wezterm --version
TKPWET/WERPL/SOEUD : curl -sL https://api.github.com/repos/wez/wezterm/releases/latest | grep -Po \'https://.*AppImage\' | sort -u | xargs -I \\{\\} sudo wget \\{\\} -O /usr/bin/wezterm && sudo chmod +x /usr/bin/wezterm && wezterm --version
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
R*PL                : {^}Remove-Item{^ ^}
R*PL/R*PL           : {^}Remove-Item -Recurse -Force {^ ^}
AUPT                : {^}APPDATA{^}
A*UPT               : {^}LOCALAPPDATA{^}
AO*EF               : env
AOEF                : {^}$env:{^}
AOEF/AOEF           : {^}$env:APPDATA{^}
AOEF/AOEF/AOEF      : {^}$env:LOCALAPPDATA{^}
AOEF/AOEF/AOEF/AOEF : {^}$env:USERPROFILE{^}
KR-LG : "C:{#Backslash}{^}"
TK-LG : "D:{#Backslash}{^}"
AOELG : "E:{#Backslash}{^}"
TP-LG : "F:{#Backslash}{^}"
TKPW-LG : "G:{#Backslash}{^}"
RAO*T               : $env:r/\\t{^}
P*URB/KAOE          : cat ~/.ssh/id_rsa.pub | ssh root@192.168.1.57 \"mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys\"
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
TKEUF                       :  diff
TKEUF/H-PBZ/KAERBD          :  diff --cached
KPHEUT/H*PB/SR*             :  commit -v
PURB/O*RPBLG/PHAFRT         :  push origin master
PUL/H-PBZ/RE/PWAEUS         :  pull --rebase
HROG/H*PB/P*                :  log -p
RE/SET/KPA*E/HED/KR-RT      :  reset HEAD ^
```

```yaml
TKPW*EUFT : {^}git fetch upstream
"TKPWEUPLT": "{^git commit --message=\"\"^}{#LEFT}{-|}"                                                                           # GIt coMMiT (message)
"TKPWEUPLTD": "{^git commit --all --message=\"\"^}{#LEFT}{-|}"                                                                    # GIt coMMiT (all, message)
"TKPW*EUPLT": "{^git commit --amend}"                                                                                             # GIt coMMiT (amend)
"TKPW*EUPLTD": "{^git commit --amend --no-edit}"                                                                                  # GIt coMMiT (amend) no-eDit
"TKPWEUP": "{^git push\\n}"                                                                                                          # GIt Push
"TKPWEUT/PURB/PWRAFRPB": "{^git push --force origin $(git symbolic-ref HEAD --short)}"                                   # GIT PUSH (force) ORIGIN (current BRANCH name)
"TKPWEUPL": "{^git pull\\n}"                                                                                                         # GIt PuLL [override]
"TKPW*EUPL": "{^git pull --rebase}"                                                                                               # GIt PuLL (rebase) [override]
"TKPW*EUTD": "{^git add .}"                                                                                                       # GIT aDD (current pathspec)
"TKPWEUTS": "{^git status --short\\n}"                                                                                              # GIT Status (short)
"TKPWEUTD": "{^git add}"                                                                                                          # GIT aDD
"TKPWEUT/KEUG/HR*EUS": "{^git config --list}"                                                                                   # GIT CONFIG LIST
"TKPWEUT/TPH*EUT": "{^git init}"                                                                                                  # GIT iNIT
"TKPWEUTD": "{^git add}"                                                                                                          # GIT aDD
"TKPW*EUFRB": "{^git stash}"                                                                                                      # GIt StaSH
"TKPWO*P": "{^git stash pop}"                                                                                                     # Git stash pOP
"TKPWOP": "{^git stash pop}"                                                                                                      # Git stash pOP
"TKPWEUT/STARB": "{^git stash}"                                                                                                   # GIT STASH
"TKPWEUT/STARB/POP": "{^git stash pop}"                                                                                           # GIT STASH POP
"TKPWEUT/STARB/PURB": "{^git stash push}"                                                                                         # GIT STASH PUSH
"TKPW*EUL": "{^git log --oneline --decorate --all --graph}"                                                                       # GIt Log
"TKPW*EULG": "{^git log --oneline --decorate --all --graph}"                                                                      # GIt LoG
"TKPWEUT/HRO*G": "{^git log --oneline --decorate --all --graph}"                                                                  # GIT LOG (oneline decorate all graph)
"TKPWEUT/HROG": "{^git log}"                                                                                                      # GIT LOG
```

Dot files git commands

```yaml
"TK*EUPLT": "{^dot commit --message=\"\"^}{#LEFT}{-|}"
"TK*EUPLTD": "{^dot commit --all --message=\"\"^}{#LEFT}{-|}"
"TK*EUP": "{^dot push}"                                                                                                          # GIt Push
"TK*EUPL": "{^dot pull}"                                                                                                         # GIt PuLL [override]
"TK*EUTS": "{^dot status}"                                                                                              # GIT Status (short)
"TK*EUL": "{^dot log --oneline --decorate --all --graph}"                                                                       # GIt Log
```

```PaulsGit
"TKPW*EUD": "{^git diff --ignore-all-space}"                                                                                      # GIt Diff
"TKPW*EUFP": "{^git add --patch}"                                                                                                 # GIt add patCH [override]
"TKPW*EUFPT": "{^git checkout --force}"                                                                                           # GIt CHeckouT (force)
"TKPW*EUFRPB": "{^git branch --delete}"                                                                                           # GIt braNCH (delete)
"TKPW*EUL": "{^git log --oneline --decorate --all --graph}"                                                                       # GIt Log
"TKPW*EULG": "{^git log --oneline --decorate --all --graph}"                                                                      # GIt LoG
"TKPW*EUP": "{^git push --force}"                                                                                                 # GIt Push (force) [override]
"TKPW*EUP/O*RPBLG/PWRA*FRPB": "{^git push --force origin $(git symbolic-ref HEAD --short)}"                                       # GIt Push (force) ORIGIN (current BRANCH name)
"TKPW*EUPL": "{^git pull --rebase}"                                                                                               # GIt PuLL (rebase) [override]
"TKPW*EUPL/O*RPBLG/PHAEUPB": "{^git pull --rebase origin main}"                                                                   # GIT PULL (rebase) ORIGIN MAIN
"TKPW*EUPL/O*RPBLG/PHAFRT": "{^git pull --rebase origin master}"                                                                  # GIT PULL (rebase) ORIGIN MASTER
"TKPW*EUPL/O*RPBLG/PWRAFRPB": "{^git pull --rebase origin $(git symbolic-ref HEAD --short)}"                                      # GIT PULL (rebase) ORIGIN (current BRANCH name)
"TKPW*EUPL/STPRAOEPL/PHAEUPB": "{^git pull --rebase upstream main}"                                                               # GIT PULL (rebase) uPSTREAM MAIN
"TKPW*EUPL/STPRAOEPL/PHAFRT": "{^git pull --rebase upstream master}"                                                              # GIT PULL (rebase) uPSTREAM MASTER
"TKPW*EUPL/STPRAOEPL/PWRAFRPB": "{^git pull --rebase upstream $(git symbolic-ref HEAD --short)}"                                  # GIT PULL (rebase) uPSTREAM (current BRANCH name)
"TKPW*EURBS": "{^git rebase --interactive}"                                                                                       # Git ReBaSe (interactive)
"TKPW*EURPL": "{^git rm --force}"                                                                                                 # GIt RM (force)
"TKPW*EURPLT": "{^git remote --verbose}"                                                                                          # GIt ReMoTe (verbose)
"TKPW*EUTD": "{^git add .}"                                                                                                       # GIT aDD (current pathspec)
"TKPW*EUTS": "{^git status --short}"                                                                                              # GIT Status (short)
"TKPW*URB": "{^git stash push}"                                                                                                   # Git stash pUSH
"TKPWA*FP": "{^git add --patch}"                                                                                                  # Git Add patCH
"TKPWAO*EB": "{^git rebase --abort}"                                                                                              # Git rEBase abort
"TKPWAOEB": "{^git rebase}"                                                                                                       # Git rEBase
"TKPWAOEBT": "{^git rebase --continue}"                                                                                           # Git rEBase conTinue
"TKPWEUD": "{^git diff}"                                                                                                          # GIt Diff
"TKPWEUFP": "{^git add --patch}"                                                                                                  # GIt add patCH [override]
"TKPWEUFPT": "{^git checkout}"                                                                                                    # GIt CHeckouT
"TKPWEUFPT/PW*": "{^git checkout -b ^}{MODE:LOWER}{MODE:SET_SPACE:-}}"                                                            # GIt CHeckouT Branch
"TKPWEUFPT/PWRAFRPB": "{^git checkout -b ^}{MODE:LOWER}{MODE:SET_SPACE:-}"                                                        # GIt CHeckouT BRANCH
"TKPWEUFPTD": "{^git checkout -b ^}{MODE:LOWER}{MODE:SET_SPACE:-}"                                                                # GIt CHeckouT (branch)
"TKPWEUFRB": "{^git stash}"                                                                                                       # GIt StaSH
"TKPWEUFRPB": "{^git branch --list --verbose}"                                                                                    # GIt braNCH
"TKPWEUP": "{^git push}"                                                                                                          # GIt Push
"TKPWEUP/O*RPBLG/PWRAFRPB": "{^git push origin $(git symbolic-ref HEAD --short)}"                                                 # GIT PUSH ORIGIN (current BRANCH name)
"TKPWEUPBT": "{^git init}"                                                                                                        # GIt iNiT
"TKPWEUPL": "{^git pull}"                                                                                                         # GIt PuLL [override]
"TKPWEUPL/O*RPBLG/PHAEUPB": "{^git pull origin main}"                                                                             # GIt PuLL ORIGIN MAIN
"TKPWEUPL/O*RPBLG/PHAFRT": "{^git pull origin master}"                                                                            # GIt PuLL ORIGIN MASTER
"TKPWEUPL/O*RPBLG/PWRAFRPB": "{^git pull origin $(git symbolic-ref HEAD --short)}"                                                # GIt PuLL ORIGIN (current BRANCH name)
"TKPWEUPL/STPRAOEPL/PHAEUPB": "{^git pull upstream main}"                                                                         # GIt PuLL uPSTREAM MAIN
"TKPWEUPL/STPRAOEPL/PHAFRT": "{^git pull upstream master}"                                                                        # GIt PuLL uPSTREAM MASTER
"TKPWEUPL/STPRAOEPL/PWRAFRPB": "{^git pull upstream $(git symbolic-ref HEAD --short)}"                                            # GIt PuLL uPSTREAM (current BRANCH name)
"TKPWEUPLT": "{^git commit --message=\"\"^}{#LEFT}{-|}"                                                                           # GIt coMMiT (message)
"TKPWEUPLTD": "{^git commit --all --message=\"\"^}{#LEFT}{-|}"                                                                    # GIt coMMiT (all, message)
"TKPWEURBS": "{^git rebase}"                                                                                                      # Git ReBaSe
"TKPWEURBS/PWORT": "{^git rebase --abort}"                                                                                        # Git ReBaSe ABORT
"TKPWEURBS/T-PB": "{^git rebase --continue}"                                                                                      # Git ReBaSe CONTINUE
"TKPWEURPBLG": "{^git merge}"                                                                                                     # GIt meRGe
"TKPWEURPL": "{^git rm}"                                                                                                          # GIt RM
"TKPWEURPLT": "{^git remote}"                                                                                                     # GIt ReMoTe
"TKPWEUT/A*D": "{^git add .}"                                                                                                     # GIT ADd (current pathspec)
"TKPWEUT/AD/AD": "{^git add .}"                                                                                                   # GIT ADD (current pathspec)
"TKPWEUT/AD/PAFP": "{^git add --patch}"                                                                                           # GIT ADD PATCH
"TKPWEUT/HRO*G": "{^git log --oneline --decorate --all --graph}"                                                                  # GIT LOG (oneline decorate all graph)
"TKPWEUT/HROG": "{^git log}"                                                                                                      # GIT LOG
"TKPWEUT/KHO*UT": "{^git checkout --force}"                                                                                       # GIT CHECKOUT force
"TKPWEUT/KHOUT/PW*": "{^git checkout -b ^}{MODE:LOWER}{MODE:SET_SPACE:-}"                                                         # GIT CHECKOUT Branch
"TKPWEUT/KHOUT/PWRAFRPB": "{^git checkout -b ^}{MODE:LOWER}{MODE:SET_SPACE:-}"                                                    # GIT CHECKOUT BRANCH
"TKPWEUT/KHOUT/TPORS": "{^git checkout --force}"                                                                                  # GIT CHECKOUT FORCE
"TKPWEUT/KHR*UP": "{^git branch --merged | grep --invert-match '\\*\\|master\\|develop\\|main' | xargs -n 1 git branch --delete}" # GIT CLEANUP
"TKPWEUT/KPH*EUPLT": "{^git commit --message=\"\"^}{#LEFT}{-|}"                                                                   # GIT CoMMIT Message
"TKPWEUT/KPH*EUT": "{^git commit --amend}"                                                                                        # GIT CoMMIT (amend)
"TKPWEUT/KPH*EUTD": "{^git commit --amend --no-edit}"                                                                             # GIT CoMMIT (amend) no-eDit
"TKPWEUT/KPHEUFPLT": "{^git commit --message=\"\"^}{#LEFT}{-|}"                                                                   # GIT CoMMIT Message
"TKPWEUT/KPHEUPLT": "{^git commit --message=\"\"^}{#LEFT}{-|}"                                                                    # GIT CoMMIT Message
"TKPWEUT/KPHEUT": "{^git commit}"                                                                                                 # GIT CoMMIT
"TKPWEUT/KPHEUT/APLD": "{^git commit --amend}"                                                                                    # GIT CoMMIT AMEND
"TKPWEUT/KPHEUT/APLD/TPHO*ETD": "{^git commit --amend --no-edit}"                                                                 # GIT CoMMIT AMEND NO EDIT
"TKPWEUT/KPHEUT/APLD/TPHO/ETD": "{^git commit --amend --no-edit}"                                                                 # GIT CoMMIT AMEND NO EDIT
"TKPWEUT/KPHEUT/PHEPBLG": "{^git commit --message=\"\"^}{#LEFT}{-|}"                                                              # GIT CoMMIT MESSAGE
"TKPWEUT/KWREUT": "{^git init}"                                                                                                   # GIT InIT
"TKPWEUT/P*UL": "{^git pull --rebase}"                                                                                            # GIT PULL (rebase)
"TKPWEUT/P*UL/O*RPBLG/PHAEUPB": "{^git pull --rebase origin main}"                                                                # GIT PULL (rebase) ORIGIN MAIN
"TKPWEUT/P*UL/O*RPBLG/PHAFRT": "{^git pull --rebase origin master}"                                                               # GIT PULL (rebase) ORIGIN MASTER
"TKPWEUT/P*UL/O*RPBLG/PWRAFRPB": "{^git pull --rebase origin $(git symbolic-ref HEAD --short)}"                                   # GIT PULL (rebase) ORIGIN (current BRANCH name)
"TKPWEUT/P*UL/STPRAOEPL/PHAEUPB": "{^git pull --rebase upstream main}"                                                            # GIT PULL (rebase) uPSTREAM MAIN
"TKPWEUT/P*UL/STPRAOEPL/PHAFRT": "{^git pull --rebase upstream master}"                                                           # GIT PULL (rebase) uPSTREAM MASTER
"TKPWEUT/P*UL/STPRAOEPL/PWRAFRPB": "{^git pull --rebase upstream $(git symbolic-ref HEAD --short)}"                               # GIT PULL (rebase) uPSTREAM (current BRANCH name)
"TKPWEUT/P*URB": "{^git push --force}"                                                                                            # GIT PUSH (force)
"TKPWEUT/P*URB/O*RPBLG/PWRAFRPB": "{^git push --force origin $(git symbolic-ref HEAD --short)}"                                   # GIT PUSH (force) ORIGIN (current BRANCH name)
"TKPWEUT/PHERPBLG/STPRAOEPL/PHAEUPB": "{^git merge upstream/main}"                                                                # GIT MERGE uPSTREAM MAIN
"TKPWEUT/PHERPBLG/STPRAOEPL/PHAFRT": "{^git merge upstream/master}"                                                               # GIT MERGE uPSTREAM MASTER
"TKPWEUT/PUL": "{^git pull}"                                                                                                      # GIT PULL
"TKPWEUT/PUL/O*RPBLG/PHAEUPB": "{^git pull origin main}"                                                                          # GIT PULL ORIGIN MAIN
"TKPWEUT/PUL/O*RPBLG/PHAFRT": "{^git pull origin master}"                                                                         # GIT PULL ORIGIN MASTER
"TKPWEUT/PUL/O*RPBLG/PWRAFRPB": "{^git pull origin $(git symbolic-ref HEAD --short)}"                                             # GIT PULL ORIGIN (current BRANCH name)
"TKPWEUT/PUL/STPRAOEPL/PHAEUPB": "{^git pull upstream main}"                                                                      # GIT PULL uPSTREAM MAIN
"TKPWEUT/PUL/STPRAOEPL/PHAFRT": "{^git pull upstream master}"                                                                     # GIT PULL uPSTREAM MASTER
"TKPWEUT/PUL/STPRAOEPL/PWRAFRPB": "{^git pull upstream $(git symbolic-ref HEAD --short)}"                                         # GIT PULL uPSTREAM (current BRANCH name)
"TKPWEUT/PURB": "{^git push}"                                                                                                     # GIT PUSH
"TKPWEUT/PURB/O*RPBLG/PWRA*FRPB": "{^git push --force origin $(git symbolic-ref HEAD --short)}"                                   # GIT PUSH (force) ORIGIN (current BRANCH name)
"TKPWEUT/PURB/O*RPBLG/PWRAFRPB": "{^git push origin $(git symbolic-ref HEAD --short)}"                                            # GIT PUSH ORIGIN (current BRANCH name)
"TKPWEUT/PWHRA*EUPL": "{^git blame -wM}"                                                                                          # GIT BLAME (-w ignore whitespace, -M find line movements)
"TKPWEUT/PWRA*FRPB": "{^git branch --verbose}"                                                                                    # GIT BRANCH (verbose)
"TKPWEUT/PWRAFRPB/SROEBS": "{^git branch --verbose}"                                                                              # GIT BRANCH VERBOSE
"TKPWEUT/R*PL": "{^git rm --force}"                                                                                               # GIT RM (force)
"TKPWEUT/R-PL": "{^git rm}"                                                                                                       # GIT RM
"TKPWEUT/RAOEBS": "{^git rebase}"                                                                                                 # GIT REBase
"TKPWEUT/RAOEBS/PWORT": "{^git rebase --abort}"                                                                                   # GIT REBase ABORT
"TKPWEUT/RAOEBS/T-PB": "{^git rebase --continue}"                                                                                 # GIT REBase CONTINUE
"TKPWEUT/RAOEBS/TPHRAF": "{^git rebase --interactive}"                                                                            # GIT REBase INTERACTIVE
"TKPWEUT/RAOEPLT": "{^git remote --verbose}"                                                                                      # GIT REMOTE verbose
"TKPWEUT/ST*TS": "{^git status}"                                                                                                  # GIT STATUS
"TKPWEUT/ST-TS": "{^git status --short}"                                                                                          # GIT STATUS (short)
"TKPWEUT/STARB": "{^git stash}"                                                                                                   # GIT STASH
"TKPWEUT/STARB/POP": "{^git stash pop}"                                                                                           # GIT STASH POP
"TKPWEUT/STARB/PURB": "{^git stash push}"                                                                                         # GIT STASH PUSH
"TKPWEUT/TK*EUF": "{^git diff --ignore-all-space}"                                                                                # GIT DIFF (ignore all space)
"TKPWEUT/TKEUF": "{^git diff}"                                                                                                    # GIT DIFF
"TKPWEUT/TKPEUG/HR*EUS": "{^git config --list}"                                                                                   # GIT CONFIG LIST
"TKPWEUT/TPH*EUT": "{^git init}"                                                                                                  # GIT iNIT
"TKPWEUTD": "{^git add}"                                                                                                          # GIT aDD
"TKPWO*P": "{^git stash pop}"                                                                                                     # Git stash pOP
"TKPWOP": "{^git stash pop}"                                                                                                      # Git stash pOP
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
AO*ERPBT : ethernet
PHAO*U: MCU
KPHRORL : microcontroller
TKAEUPL : daemon
```

## [Exercism](https://exercism.org/)

Exercism is a foss friendly programming platform. There is also a native CLI
that allows you to use your own editor (thanks Paul Fioravanti for the tip).

Being able to use your own editor is huge because it means we can work on
programming in steno much easier. Using web interfaces is fine, but you can't
use any of your custom snippets.

They have 67 programming languages as of 2023-07-10.

```yaml
KPEUFPL : exercism
SKEUFPL : exercism
```

## [Leetcode](https://leetcode.com/)

```yaml
HRAOET : leet
HRAOET/KOED : leetcode
HRAOETD : leetcode
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

## Terminal Presentations

```yaml
HRAOEPL : lookatme
STOP/STOP : <!--stop-->
```

## Web/Protocol

```yaml
TP-PT : FTP
TP-PT/TP-PT : ftp
TP-PT/TP-PT/TP-PT : ftp://
TP-PT/TP-PT/TP-PT/TP-PT : File Transfer Protocol (FTP)
STP-PT : SFTP
STP-PT/STP-PT : sftp
STP-PT/STP-PT/STP-PT : sftp://
STP-PT/STP-PT/STP-PT/STP-PT : Secure File Transfer Protocol (SFTP)
HAO*EPT : HTTP
HAO*EPT/HAO*EPT : http
HAO*EPT/HAO*EPT/HAO*EPT : http://
HAO*EPT/HAO*EPT/HAO*EPT/HAO*EPT : Hypertext Transfer Protocol (HTTP)
HAO*EPTS : HTTPS
HAO*EPTS/HAO*EPTS : https
HAO*EPTS/HAO*EPTS/HAO*EPTS : https://
HAO*EPTS/HAO*EPTS/HAO*EPTS/HAO*EPTS : Hypertext Transfer Protocol (HTTPS)
```

## Wireshark

```yaml
WAOEUR/SHARBG : wireshark
WARBG : wireshark
TARBG : termshark
```

## Reverse Engineering

### Radare2

```yaml
2R : r2
2R/2R : radare2
2R/PWEUPB : rabin2
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
KWRAPL: {^}yaml
RAOUF: remove
```
