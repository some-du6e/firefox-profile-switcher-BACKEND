import os
from time import sleep

print("give me the password")
os.system("sudo echo password works")
print("setting execute permission files")
os.system("sudo chmod +x ./main.py > /dev/null")
print("done")
sleep(1)
print("moving file to /etc/")
os.system("sudo mkdir /etc/firefox-profile-switcher > /dev/null 2>&1")
os.system("sudo cp ./main.py /etc/firefox-profile-switcher/main.py > /dev/null 2>&1")
print("done")
