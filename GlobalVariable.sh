#!/bin/bash
echo "Enter variable name: "
read variable_name
echo "Enter variable value: "
read variable_value
echo "Export "$variable_name"="$variable_value>>~/.bashrc
echo $variable_name"="$variable_value>>~/.profile
echo $variable_name"="$variable_value>>/etc/environment
source ~/.bashrc
source ~/.profile
echo "Reboot to apply changes in /etc/environment file? y/n"
read restart
case $restart in
    y) sudo shutdown -r 0;;
    n) echo "Don't forget to restart your computer manually";;
esac
exit
