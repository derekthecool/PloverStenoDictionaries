# PowerShell Dictionary

I have decided to use exclusively powershell on every OS when ever possible.
So far I've used it as my primary shell on Windows 11, and Arch Linux.

Powershell commands love using Verb-Noun type commands.

This dictionary will help writing powershell commands even faster.

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
SHROB : Select-Object \\{{$_
TKPWROB : Group-Object \\{{$_
PHO*B : Measure-Object
SOB : Sort-Object \\{{$_
```

### PowerShell/Pwsh Scripting

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