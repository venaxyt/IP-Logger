from colorama import Fore, init
import requests
import json
import os

init()
os.system("title 𝙏𝙀𝙍𝘼𝙓 𝙄𝙋 𝙇𝙊𝙂𝙂𝙀𝙍")
os.system("cls")
banner = (Fore.MAGENTA + """
  ██▓ ██▓███     ▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███
 ▓██▒▓██░  ██▒   ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓██  ▀ ▓██ ▒ ██▒
 ▒██▒▓██░ ██▓▒   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒█████ ▓██ ░▄█ ▒
 ░██░▒██▄██▓▒ ▒   ░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ █▓  ▄ ▒██▀▀█▄
 ░██░▒██ ░  ░       ▒▓█▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
 ░▓  ▒▓▒░ ░  ░     ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ▒ ░░▒ ░            ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
  ▒ ░░░            ░        ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░
  ░                          ░           ░  ░░ ░      ░  ░      ░  ░   ░
                                             ░
""" + Fore.LIGHTCYAN_EX)

print(banner); print(" [SERVER] discord.gg/terax\n")
ip = input(" [INPUT] IP ADDRESS : "); ip.replace(" ", "")
r = requests.get(f"http://ip-api.com/json/{ip}")
r2 = requests.get(f"https://ipinfo.io/{ip}")
values = json.loads(r.text)
data = r2.json()
city = data["city"]
location = data["loc"].split(",")
latitude = location[0]
longitude = location[1]

print("\n [1] : " + values["country"] + f" [{values['countryCode']}]")
print(" [2] : " + values["regionName"] + f" [{values['region']}]")
print(" [3] : " + city)
print(" [4] : " + values["timezone"])
print(" [5] : " + values["isp"])
print(" [6] : " + latitude, "|", longitude)
os.system("pause >nul")  # Pause command in Batch (press any key to exit the code)
