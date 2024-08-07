function Test-PloverPath {
    param (
        [Parameter(Mandatory = $true)]
        [string]$Path
    )
    return Test-Path $Path -PathType Leaf
}

function Read-PluginInstallFile {
    param (
        [Parameter(Mandatory = $true)]
        [string]$FilePath
    )
    if (Test-Path $FilePath) {
        Get-Content $FilePath
    } else {
        throw "File $FilePath is not found, nothing to install"
    }
}

function Install-Plugins {
    param (
        [Parameter(Mandatory = $true)]
        [string]$PloverAppImagePath,
        [string[]]$Plugins
    )
    foreach ($plugin in $Plugins) {
        $command = "$PloverAppImagePath -s plover_plugins install $plugin"
        Invoke-Expression $command
    }
}

function Install-PloverPlugins {
    param (
        [Parameter(Mandatory = $true)]
        [string]$PloverAppImagePath
    )

    Write-Host "Checking provided Plover path: $PloverAppImagePath"

    if (-not (Test-PloverPath -Path $PloverAppImagePath)) {
        Write-Host 'Plover path provided either does not exist or is not executable'
        Write-Host 'Exiting!'
        return 1
    }

    $PluginInstallFile = "$PSScriptRoot/plugins_list.txt"

    try {
        $plugins = Read-PluginInstallFile -FilePath $PluginInstallFile
    } catch {
        Write-Host $_.Exception.Message
        return 2
    }

    Write-Host "plugins to install:"
    $plugins -split '`n'

    $install = Read-Host 'Do you want to install the plugins listed? [y/n]'

    if ($install -eq 'y') {
        Write-Host 'Installing all plugins'
        Install-Plugins -PloverAppImagePath $PloverAppImagePath -Plugins $plugins
    } else {
        Write-Host "Interpreting option '$install' as no...returning"
        return 3
    }
}

 Write-Host "Run the function Install-PloverPlugins to begin"
