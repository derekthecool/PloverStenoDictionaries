#/usr/bin/env bash

if [[ -z $1 ]]; then
  echo "No Plover path provided, run the script again with the path to the plover******.AppImage"
fi

PloverAppImagePath=$1
echo "Checking provided Plover path: $PloverAppImagePath"

if [[ -x $PloverAppImagePath ]]; then
  printf "Plover path is executable and ready for use\n\n"
else
  echo "Plover path provided either does not exist or is not executable"
  echo "Exiting!"
  exit 1
fi

PluginInstallFile=~/.config/plover/LinuxPloverPluginsToInstall.txt
if [[ -e $PluginInstallFile ]]; then
  echo "Plugins found in file LinuxPloverPluginsToInstall.txt"
  cat "$PluginInstallFile"
else
  echo "File $PluginInstallFile is not found, nothing to install"
  exit 2
fi

printf "\n\nDo you want to install the plugins listed? [y/n]"
read install

if [[ $install == "y" ]]; then
  echo "Installing all plugins"

  while read p; do
    command="$PloverAppImagePath -s plover_plugins install git+$p"
    $command
  done < $PluginInstallFile
else
  echo "Interpreting option '$install' as no...exiting"
   exit 3
fi
