# PowerShell Dictionary

I have decided to use exclusively powershell on every OS when ever possible.
So far I've used it as my primary shell on Windows 11, and Arch Linux.

Powershell commands love using Verb-Noun type commands.

This dictionary will help writing powershell commands even faster.

## Quickly Reload My Dotfiles Powershell Module

```yaml
TKO*TS : Import-Module -Force -Name Dots\\n
```

## Powershell File Extensions

| File Type                         | Extension | Description                                                       |
| --------------------------------- | --------- | ----------------------------------------------------------------- |
| PowerShell Script File            | `.ps1`    | Contains PowerShell commands and scripts.                         |
| PowerShell Module Manifest File   | `.psd1`   | Contains metadata about a PowerShell module.                      |
| PowerShell Module File            | `.psm1`   | Contains the functions and code that make up a PowerShell module. |
| PowerShell Data File              | `.psd1`   | Used for localization and other data purposes.                    |
| PowerShell Workflow File          | `.psw1`   | Contains PowerShell workflow definitions.                         |
| PowerShell Cmdlet Definition File | `.cdxml`  | XML-based cmdlet definitions.                                     |
| PowerShell Types File             | `.ps1xml` | Type extension definitions for PowerShell.                        |
| PowerShell Format File            | `.ps1xml` | Formatting definitions for displaying objects.                    |
| PowerShell Configuration File     | `.pssc`   | Configuration for Just Enough Administration (JEA).               |
| PowerShell Role Capability File   | `.psrc`   | Defines role capabilities for JEA.                                |

Most important ones to have quick commands for

```yaml
#1P-S: ps1
#1P*S: {^}.ps1
#1P-PL: psm1
#1P*PL: {^}.psm1
#1P-D: psd1
#1P*D: {^}.psd1
```

## Powershell Terms That Are Not Commands

```yaml
PW-RB              :  powershell
AO*EF               : env
```

## Fast Commands

```yaml
TPROB : ForEach-Object \\{{$_
TPROB/TPROB : %\\{{$_
WOB : Where-Object \\{{$_
WOB/WOB : ?\\{{$_
SHROB : Select-Object -{^}{-|}
TKPWROB : Group-Object \\{{$_
PHO*B : Measure-Object
SOB : Sort-Object \\{{$_
-RPBL : $_
-RPBLS : $_.{^}
SPWEL : $(){\#Left}{^} # Easy subshell. Used for doing things like this echo "$(ls)"
KOFB : [PSCustomObject]@\\{\\}{\#Left}{^}
```

## Other Powershell Items

```yaml
SKREUPT/RAOT : $PSScriptRoot
```

## PowerShell/Pwsh Cmdlets

```yaml
R*PL                : {^}Remove-Item{^ ^}
R*PL/R*PL           : {^}Remove-Item -Recurse -Force {^ ^}
AUPT                : {^}APPDATA{^}
A*UPT               : {^}LOCALAPPDATA{^}
AOEF                : {^}$env:{^}
AOEF/AOEF           : {^}$env:APPDATA{^}
AOEF/AOEF/AOEF      : {^}$env:LOCALAPPDATA{^}
AOEF/AOEF/AOEF/AOEF : {^}$env:USERPROFILE{^}
KR-LG : "C:{#Backslash}{^}"
TK-LG : "D:{#Backslash}{^}"
AOELG : "E:{#Backslash}{^}"
TP-LG : "F:{#Backslash}{^}"
TKPW-LG : "G:{#Backslash}{^}"
P*URB/KAOE          : cat ~/.ssh/id_rsa.pub | ssh root@192.168.1.57 \"mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys\"
WEUPB/TKPWET : winget
```

## Main Verb Helpers

TODO: (Derek Lomax) 5/22/2024 3:26:15 PM, finish adding the rest of important verbs here

```yaml
TKPW*ET : Get-{^}{-|}{MODE:TITLE}{MODE:SET_SPACE:}
S*ET : Set-{^}{-|}{MODE:TITLE}{MODE:SET_SPACE:}
SRO*EBG : Invoke-{^}{-|}{MODE:TITLE}{MODE:SET_SPACE:}
KHRAO*ER : Clear-{^}{-|}{MODE:TITLE}{MODE:SET_SPACE:}
KHRO*ES : Close-{^}{-|}{MODE:TITLE}{MODE:SET_SPACE:}
TPH*U : New-{^}{-|}{MODE:TITLE}{MODE:SET_SPACE:}
AUPTD/AUPTD : Update-{^}{-|}{MODE:TITLE}{MODE:SET_SPACE:}
```

Copy
Enter
Exit
Find
Format
Get
Hide
Join
Lock
Move
Open
Push
Pop
Redo
Remove
Rename
Reset
Resize
Search
Select
Set
Show
Skip
Split
Step
Switch
Undo
Unlock
Watch
Connect
Disconnect
Read
Receive
Send
Write
Backup
Checkpoint
Compare
Compress
Convert
ConvertFrom
ConvertTo
Dismount
Edit
Expand
Export
Group
Import
Initialize
Limit
Merge
Mount
Out
Publish
Restore
Save
Sync
Unpublish
Debug
Measure
Ping
Repair
Resolve
Test
Trace
Approve
Assert
Build
Complete
Confirm
Deny
Deploy
Disable
Enable
Install
Invoke
Register
Request
Restart
Resume
Start
Stop
Submit
Uninstall
Unregister
Wait
Use
Block
Grant
Protect
Revoke

Full list of powershell approved verbs

- Add
- Clear
- Close
- Copy
- Enter
- Exit
- Find
- Format
- Get
- Hide
- Join
- Lock
- Move
- New
- Open
- Optimize
- Push
- Pop
- Redo
- Remove
- Rename
- Reset
- Resize
- Search
- Select
- Set
- Show
- Skip
- Split
- Step
- Switch
- Undo
- Unlock
- Watch
- Connect
- Disconnect
- Read
- Receive
- Send
- Write
- Backup
- Checkpoint
- Compare
- Compress
- Convert
- ConvertFrom
- ConvertTo
- Dismount
- Edit
- Expand
- Export
- Group
- Import
- Initialize
- Limit
- Merge
- Mount
- Out
- Publish
- Restore
- Save
- Sync
- Unpublish
- Update
- Debug
- Measure
- Ping
- Repair
- Resolve
- Test
- Trace
- Approve
- Assert
- Build
- Complete
- Confirm
- Deny
- Deploy
- Disable
- Enable
- Install
- Invoke
- Register
- Request
- Restart
- Resume
- Start
- Stop
- Submit
- Suspend
- Uninstall
- Unregister
- Wait
- Use
- Block
- Grant
- Protect
- Revoke
- Unblock
- Unprotect

## Main Commands

```yaml
PH*ERB/OBT: Measure-Object
AD/KAUPBT :Add-Content
AD/KAUPB/TEPBT :Add-Content
AD/HEUFT/REU :Add-History
AD/PHEB :Add-Member
AD/TAOEUP :Add-Type
KHRAOER/KAUPBT : Clear-Content
KHRAOER/KAUPB/TEPBT : Clear-Content
KHRAOER/HEUFT/REU : Clear-History
KHRAOER/AOEUPLT : Clear-Item
KHRAOER/RE/SAOEUBG/-L : Clear-RecycleBin
KHRAOER/SRAEURBL : Clear-Variable
KPAEUR/OBT : Compare-Object
KWERT/PA*T : Convert-Path
TPR/SKR-F : ConvertFrom-Csv
TPR/SKWR-FPB : ConvertFrom-Json
TPR/SKUR : ConvertFrom-SecureString
TPR/KPOEPL : ConvertFrom-Xml
TPR/KPAOEPL : ConvertFrom-Xml
O/SKR-F : ConvertTo-Csv
O/HAOEPLT : ConvertTo-Html
O/SKWR-FPB : ConvertTo-Json
O/SKEUR : ConvertTo-SecureString
O/KPAOEPL : ConvertTo-Xml
O/KPOEPL : ConvertTo-Xml
KO*EP/AOEUPLT : Copy-Item
*EPBT/SEGS : Enter-PSSession
KPEUT/SEGS : Exit-PSSession
EBGS/PAPBD/AR/KAOEUF : Expand-Archive
KPAPBD/KRAOEUF : Expand-Archive
EBGS/PORT/HREUS : Export-Alias
EBGS/PORT/SKR-F : Export-Csv
EBGS/PORT/TPORPLT/TKAET : Export-FormatData
TPOR/AOEFP/OBT : ForEach-Object
TPORPLT/KUFT/TOPL : Format-Custom
TPORPLT/HEBGS : Format-Hex
TPORPLT/HR*EUS : Format-List
TPORPLT/TAEUBL : Format-Table
TPORPLT/WAOEUD : Format-Wide
TKPWET/HREUS : Get-Alias
TKPWET/KHAOEULD : Get-ChildItem
TKPWET/KHREUP : Get-Clipboard
TKPWET/KPHAPBD : Get-Command
TKPWET/KPAOURT : Get-ComputerInfo
TKPWET/KAUPBT : Get-Content
TKPWET/KAUPB/TEPBT : Get-Content
TKPWET/KRERBL : Get-Credential
TKPWET/TKAEUT : Get-Date
TKPWET/ROEUR : Get-Error
TKPWET/AOEPBT : Get-Event
TKPWET/TPAOEUL : Get-FileHash
TKPWET/TPORPLT : Get-FormatData
AUPTD/TPORPLT : Update-FormatData
TKPWET/HEP : Get-Help
TKPWET/HEUFT/REU : Get-History
TKPWET/HOEFT : Get-Host
TKPWET/AOEUPLT : Get-Item
TKPWET/AOEUPLT/PROPT : Get-ItemProperty
TKPWET/SKWROB : Get-Job
TKPWET/HROEBGS : Get-Location
TKPWET/PHEB : Get-Member
TKPWET/PHAOULD : Get-Module
TKPWET/PROEUS : Get-Process
TKPWET/TKRAOEUF : Get-PSDrive
TKPWET/SEGS : Get-PSSession
TKPWET/RAPBD : Get-Random
TKPWET/SKRET : Get-Secret
TKPWET/S-FRS : Get-Service
TKPWET/S-PL : Get-SystemDriver
TKPWET/TAOEUP : Get-TypeData
TKPWET/AOUPBG : Get-Unique
TKPWET/UP/TAOEUPL : Get-Uptime
TKPWET/SRAEURBL : Get-Variable
TKPWET/SRERB : Get-Verb
TKPWET/WEUPB : Get-WinEvent
TKPWRAOUP/OBT : Group-Object
EUPL/PORT/HREUS : Import-Alias
EUPL/PORT/SKR-F : Import-Csv
EUPL/PORT/PHAOULD : Import-Module
STPHAUL/PHAOULD : Install-Module
EUPB/SROEBG/KPHAPBD : Invoke-Command
SROEBG/KPHAPBD : Invoke-Command
EUPB/SROEBG/KPR*EGS : Invoke-Expression
SROEBG/KPR*EGS : Invoke-Expression
EUPB/SROEBG/AOEUPLT : Invoke-Item
SROEBG/AOEUPLT : Invoke-Item
EUPB/SROEBG/REFT : Invoke-RestMethod
SROEBG/REFT : Invoke-RestMethod
EUPB/SROEBG/WEB : Invoke-WebRequest
SROEBG/WEB : Invoke-WebRequest
SKWROEUPB/PA*T : Join-Path
SKWROEUPB/STREUPBG : Join-String
PH*ERB/KPHAPBD : Measure-Command
PH*ERB/OBT : Measure-Object
PHOF/AOEUPLT : Move-Item
TPHU/HREUS : New-Alias
TPHU/TKPWAOUD : New-Guid
TPHU/AOEUPLT : New-Item
TPHU/PHAOULD : New-Module
TPHU/PHAOULD/PHAPB/TPEFT : New-ModuleManifest
TPHU/OBT : New-Object
TPHU/TKRAOEUF : New-PSDrive
TPHU/T*EPL : New-TemporaryFile
TPHU/TAOEUPL : New-TimeSpan
TPHU/SRAEURBL : New-Variable
OUT/TKEFLT : Out-Default
OUT/TPAOEUL : Out-File
OUT/TKPWREUD : Out-GridView
OUT/HOEFT : Out-Host
OUT/TPHUL : Out-Null
OUT/PREURPBT : Out-Printer
OUT/STREUPBG : Out-String
POP/HROEBGS : Pop-Location
PURB/HROEBGS : Push-Location
RAED/HOEFT : Read-Host
RE/PHOF/HREUS : Remove-Alias
RE/PHOF/AOEUPLT : Remove-Item
RE/PHOF/PHAOULD : Remove-Module
RE/PHOF/TKRAOEUF : Remove-PSDrive
RE/PHOF/SKRET : Remove-Secret
RE/PHOF/S-FRS : Remove-Service
RE/PHOF/TAOEUP : Remove-TypeData
RE/PHOF/SRAEURBL : Remove-Variable
RE/START/KPAOURT : Restart-Computer
RE/START/S-FRS : Restart-Service
SHREBGT/OBT : Select-Object
SHREBGT/STREUPBG : Select-String
SHREBGT/KPOEPL : Select-Xml
SHREBGT/KPAOEPL : Select-Xml
SET/HREUS : Set-Alias
SET/KHREUP : Set-Clipboard
SET/KAUPBT : Set-Content
SET/KAUPB/TEPBT : Set-Content
SET/HROEBGS : Set-Location
SET/S-FRS : Set-Service
SET/SRAEURBL : Set-Variable
SORT/OBT : Sort-Object
SPHREUT/PA*T : Split-Path
START/SKWROB : Start-Job
START/PROEUS : Start-Process
START/S-FRS : Start-Service
START/SHRAOEP : Start-Sleep
STOP/KPAOURT : Stop-Computer
STOP/PROEUS : Stop-Process
STOP/S-FRS : Stop-Service
TAOE/OBT : Tee-Object
TEFT/KEBGS : Test-Connection
TEFT/SKWR-FPB : Test-Json
TEFT/PA*T : Test-Path
AUPTD/HEP : Update-Help
AUPTD/TAOEUP/TKAET : Update-TypeData
WAEUT/PROEUS : Wait-Process
W-R/OBT : Where-Object
WRAOEUT/TKPWUG : Write-Debug
WRAOEUT/ROEUR : Write-Error
WRAOEUT/HOEFT : Write-Host
WRAOEUT/TPH-FGS : Write-Information
WRAOEUT/O*UPT : Write-Output
WRAOEUT/PROG : Write-Progress
WRAOEUT/SRER/PWOES : Write-Verbose
WRAOEUT/SROES : Write-Verbose
WRAOEUT/WARPBG : Write-Warning
```

## Nuget Package Manager Commands

```yaml
TPAOEUPBD/PAPBLG : Find-Package
```

## Commands From Powershell Gallery Modules

### [Pester](https://pester.dev/docs/quick-start)

Awesome powershell testing framework

```yaml
SR*EFT : Invoke-Pester
SROEBG/PEFT : Invoke-Pester
```

### [PSScriptTools](https://github.com/jdhitsolutions/PSScriptTools)

#### ConvertFrom-Text

This command struct me with awe. It is the pipable regex function I've always
dreamed of.
It uses named regex capture groups to extract rich objects from text.

Basic usage is like this:

```powershell
1 .. 5 | %{Get-Random | Out-String } | ConvertFrom-Text '(?<FirstNumber>\d).*(?<LastNumber>\d)'

FirstNumber LastNumber
----------- ----------
6           9
1           0
1           4
1           3
5           8
```

```yaml
TPR/TEGT : ConvertFrom-Text
```

## Added by Plover

```yaml
TKPWEP: Get-Help
TPH-PBG: npx
SRERT: convert
SR*ERT: Convert
TP-Z: fzf
TKPWEBGS/TKPWEBGS: regular expression
TKPWEBGS/TKPWEBGS/TKPWEBGS: System.Text.RegularExpressions
TKPWEPL: Get-Member
STKPWUR: Azure
URL: url
KPOEPLT: component
```
