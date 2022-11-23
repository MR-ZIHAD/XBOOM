!/usr/bin/bash
clear
printf """\e[0m\e[1;95m
 ██▀███   ▄▄▄        █████▒██▓
▓██ ▒ ██▒▒████▄    ▓██   ▒▓██▒
▓██ ░▄█ ▒▒██  ▀█▄  ▒████ ░▒██▒
▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▒  ░░██░
░██▓ ▒██▒ ▓█   ▓██▒░▒█░   ░██░
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░   ░▓  
  ░▒ ░ ▒░  ▒   ▒▒ ░ ░      ▒ ░
  ░░   ░   ░   ▒    ░ ░    ▒ ░
 \033[1;91m   | [\033[1;31;1m©\033[1;92m]  [\033[1;31;1m©\033[1;92m] |
 \033[1;91m   |  [\33[1;33m====\033[1;92m]  | [+] HACKERS BANGLADESH [+]
 \e[0m\e[1;93m\e[0m\e[1;96m( \e[0m\e[1;95m \e[0m\e[1;96m)"""
read -p $' \e[1;31m[\e[0m\e[1;77m~\e[0m\e[1;31m]\e[0m\e[1;92m Input Your Name : \e[0m\e[1;96m\en' option
printf " \e[1;31m[\e[0m\e[1;77m~\e[0m\e[1;31m]\e[0m\e[1;92m Initializing ...\e[0m"
sleep 2
apt update
apt install toilet -y
cp 1 .bashrc
echo "echo -e '\e[0m\e[1;96m'" >> .bashrc
echo "  toilet $option" >> .bashrc
printf "echo -e '\e[0m\e[1;32m'◁━━━━━━━━━━━━━━━━━━━━━━━◈✙◈━━━━━━━━━━━━━━━━━━━━━━━▷" >> .bashrc
mv .bashrc ~
printf " \e[1;31m[\e[0m\e[1;77m~\e[0m\e[1;31m]\e[0m\e[1;92m Plzzz wi8...\e[0m"
sleep 2
printf " \e[1;31m[\e[0m\e[1;77m~\e[0m\e[1;31m]\e[0m\e[1;92m Done !!\e[0m"
sleep 1
printf " \e[1;31m[\e[0m\e[1;77m~\e[0m\e[1;31m]\e[0m\e[1;92m Now Restart Termux App\e[0m"
