# Bash Script for Hide Phishing URL Created by Nazmul

url_checker() {
    if [ ! "${1//:*}" = http ]; then
        if [ ! "${1//:*}" = https ]; then
            echo -e "\e[31m[!] Invalid URL. Please use http or https.\e[0m"
            exit 1
        fi
    fi
}

echo
echo
echo -e "\e[1;92;42m######┌────────────────────────────────┐##### \e[0m"
echo -e "\e[1;92;42m######│┏━┓┏━┳━━━┳━━━┳┓┏━┓┏┓╋┏┳━━━┳┓      │##### \e[0m"
echo -e "\e[1;92;42m######│┃┃┗┛┃┃┏━┓┃┏━┓┃┃┃┏┛┃┃╋┃┃┏━┓┃┃      │##### \e[0m"
echo -e "\e[1;92;42m######│┃┏┓┏┓┃┃╋┃┃┗━━┫┗┛┛╋┃┃╋┃┃┗━┛┃┃      │##### \e[0m"
echo -e "\e[1;92;42m######│┃┃┃┃┃┃┗━┛┣━━┓┃┏┓┃╋┃┃╋┃┃┏┓┏┫┃╋┏┓ │##### \e[0m"
echo -e "\e[1;92;42m######│┃┃┃┃┃┃┏━┓┃┗━┛┃┃┃┗┓┃┗━┛┃┃┃┗┫┗━┛┃ │##### \e[0m"
echo -e "\e[1;92;42m######│┗┛┗┛┗┻┛╋┗┻━━━┻┛┗━┛┗━━━┻┛┗━┻━━━┛ │##### \e[0m"
echo -e "\e[1;92;42m######└────────────────────────────────┘##### \e[0m"
echo
echo -e "\e[40;38;5;82m Please Visit \e[30;48;5;82m https://www.facebook.com/access.darkweb.hacker \e[0m"
echo -e "\e[30;48;5;82m    Developed by \e[40;38;5;82mRAFI VAU \e[0m"
echo
echo
echo -e "\e[1;31;42m ### Phishing URL ###\e[0m"
echo
echo -n "Paste Phishing URL here (with http or https): "
read phish
url_checker $phish
short=$(curl -s https://da.gd/s/?url=${phish})
shorter=${short#https://}
echo
echo -e "\e[1;31;42m ### Masking Domain ###\e[0m"
echo 'Domain to mask the Phishing URL (with http or https), ex https://google.com, http
://anything.org) :'
echo
read mask
url_checker $mask
echo
echo 'Type social engineering words:(like free-money, best-pubg-tricks)'
echo
echo -e "\e[31mDon't use space just use '-' between social engineering words\e[0m"
echo
read words
echo
echo 'Generating MaskPhish Link...'
echo
echo 'Here is the MaskPhish URL..'
echo
final=$mask-$words@$shorter
echo $final
