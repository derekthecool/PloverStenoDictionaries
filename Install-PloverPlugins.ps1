function Test-PloverPath {
    param (
        [Parameter(Mandatory = $true)]
        [string]$Path
    )
    return Test-Path $Path -PathType Leaf -and (Get-Item $Path).Attributes.ToString().Split(',').Contains('Archive')
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
        exit 1
    }

    $PluginInstallFile = ./LinuxPloverPluginsToInstall.txt

    try {
        $plugins = Read-PluginInstallFile -FilePath $PluginInstallFile
    } catch {
        Write-Host $_.Exception.Message
        exit 2
    }

    $install = Read-Host 'Do you want to install the plugins listed? [y/n]'

    if ($install -eq 'y') {
        Write-Host 'Installing all plugins'
        Install-Plugins -PloverAppImagePath $PloverAppImagePath -Plugins $plugins
    } else {
        Write-Host "Interpreting option '$install' as no...exiting"
        exit 3
    }
}

 Write-Host "Run the function Install-PloverPlugins to begin"
