class PloverDictionary
{
    [bool]$enabled
    [string]$path

    [string]ToString()
    {
        $fileName = ($this.Path -split '[/\\]' | Select-Object -Last 1)
        return "$($this.Enabled) : $fileName"
    }
}

class PloverConfiguration
{
    [string]$Path
    [PloverDictionary[]]$Dictionaries
}

function Get-PloverConfiguration
{
    param (
        [Parameter()]
        [string]$Path
    )

    $config = [PloverConfiguration]::new()
    $config.Dictionaries = Get-Content -Path $Path
    | Select-String 'dictionaries = (\[.*\])' -AllMatches
    | ForEach-Object { $_.Matches.Groups[1].Value | ConvertFrom-Json }

    $config.Path = $Path

    return $config
}

function Sync-PloverConfiguration
{
    $LinuxConfig = Get-PloverConfiguration -Path $PSScriptRoot/../plover.cfg
    $WindowsConfig = Get-PloverConfiguration -Path $PSScriptRoot/../plover/plover.cfg

    $LinuxConfig
    $WindowsConfig

    if($LinuxConfig.Dictionaries -ne $WindowsConfig.Dictionaries)
    {
        Write-Host "Configurations are out of sync"
    } else
    {
        Write-Host "Configurations are in sync!"
    }
}

Sync-PloverConfiguration
