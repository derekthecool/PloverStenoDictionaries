BeforeAll {
    . ./Install-PloverPlugins.ps1
}

Describe 'Plover Application Tests' {
    Context 'Testing Plugin File Reading' {
        It 'Throws an error if file does not exist' {
            Mock Test-Path { return $false }
            { Read-PluginInstallFile -FilePath 'fakepath' } | Should -Throw 'File fakepath is not found, nothing to install'
        }

        It 'Reads content if file exists' {
            Mock Test-Path { return $true }
            Mock Get-Content { return @('plugin1', 'plugin2') }
            Read-PluginInstallFile -FilePath 'fakepath' | Should -Be @('plugin1', 'plugin2')
        }
    }

    Context 'Testing Plugin Installation' {
        It 'Should call Invoke-Expression for each plugin' {
            Mock Invoke-Expression {}
            Install-Plugins -PloverAppImagePath 'path' -Plugins @('plugin1', 'plugin2')
            Assert-MockCalled Invoke-Expression -Exactly 2 -Scope It
        }
    }
}
