#Simple script to install and mine monero thru XMRig on Arch Linux. Some parts of the code were created by chatgpt

import time
import json
from time import sleep
import os
import subprocess
from contextlib import chdir
import sys

def ask_c():
	answer = input("Continue? (y/n): ").strip().lower()
	if answer not in ("y", ""):
		print ("Stopped by user")
		exit(0)

def distro():
	answer = input ("1. Arch; 2. Debian; 3. Fedora/RedHat- based distro with DNF; 4. Windows: ")
	if answer in ("1"):
		print ("Installing depencies for Arch Linux")
		print ("Please, type your root password if it's needed. If you don't want to continue, press Ctrl + C")
		subprocess.call(["sudo", "pacman", "-Syu", "cmake", "make", "gcc", "git", "hwloc", "libuv", "openssl", "--noconfirm"])
	elif answer in ("2"):
		print ("Installing depencies for Debian")
		print ("Please, type your root password if it's needed. If you don't want to continue, press Ctrl + C")
		subprocess.call(["sudo","apt", "update", "&&", "sudo", "apt", "install", "git", "build-essential", "cmake", "libuv1-dev", "uuid-dev", "libssl-dev", "--noconfirm"])
	elif answer in ("3"):
		print ("Installing depencies for RPM- based distro")
		print ("Please, type your root passsword if it's needed. If you don't want to continue, press Ctrl + C")
		subprocess.call(["sudo", "dnf", "system-upgrade", "&&", "sudo", "dnf", "install", "git", "make", "cmake", "gcc", "gcc-c++", "libstdc++-static", "libuv-static", "hwloc-devel", "openssl-devel", "--noconfirm"])
	elif answer in ("4"):
		print ("Not supported yet")
		exit(0)
	else:
		print ("Please choose existing variant.")
		exit(0)

def depencies():
	answer = input ("Do you want to install Depencies? (y/n): ").strip().lower()
	if answer in ("y", ""):
		print ("Choose your operating system")
		distro()
	else:
		print ("Skipping installing depencies, user input")

usr = os.path.expanduser("~")
xmrig = os.path.expanduser("xmrig")
build = os.path.expanduser("build")
config_path = os.path.expanduser("~/xmrig/build/config.json")

for i in range(3, 0, -1): 
    for symbol in f"{i}...": 
        sys.stdout.write(symbol)
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(0.5)

print()

depencies()

os.chdir(usr)
print("Current directory:", os.getcwd(),"NOTE! IF ITS NOT /home/your_username BETTER DO NOT CONTIUE!") 
ask_c()


if not os.path.exists(xmrig):
    print("Cloning XMRig repository...")
    subprocess.call(["git", "clone", "https://github.com/xmrig/xmrig.git"])
else:
    print("XMRig directory already exists. Skipping cloning.")

for i in range(3, 0, -1):              
    for symbol in f"{i}...":  
        sys.stdout.write(symbol)       
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(0.5) 
print()  


os.chdir(xmrig)
subprocess.call(["mkdir", "build"])

os.chdir(build)
print(f"Current directory: {os.getcwd()} NOTE! IF ITS NOT /home/username/xmrig/build BETTER DO NOT CONTINUE!")
ask_c()

wallet_address = input("Write your Monero wallet address: ") #Wallet

if os.path.exists(config_path):
    with open(config_path, "r") as file:
        config = json.load(file)
else:
    config = {}

config["pools"] = [{
    "url": "pool.supportxmr.com:443", 
    "user": wallet_address,
    "tls": True
}]



# Saving the config file
with open(config_path, "w") as file:
    json.dump(config, file, indent=4)


subprocess.call (["cmake", ".."])
subprocess.call(["make", f"-j{os.cpu_count()}"])

print ("Succesfully installed XMRig! Now, type 'cd ~/xmrig/build', and then './xmrig'!")
print ("Closing the program")

for i in range(3, 0, -1):
    for symbol in f"{i}...":
        sys.stdout.write(symbol)
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(0.5)
print ()
