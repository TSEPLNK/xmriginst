#Simple script to install and mine monero thru XMRig on Linux. Some parts of the code were created by chatgpt

import time
import json
from time import sleep
import os
import subprocess
import sys
import platform

def threetwoone():
        for i in range(3, 0, -1):
                sys.stdout.write(f"\r{i}... ")
                sys.stdout.flush()
                time.sleep(1)
        print()

def ask_c():
    answer = input("Continue? (y/n): ").strip().lower()
    if answer not in ("y", ""):
        print ("\033[91mStopped by user!\033[0m")
        sys.exit(0)

def config():
    config_path = os.path.expanduser("~/xmrig/build/config.json")
    print("Updating the config")
    pool = choose()
    wallet_address=input("Enter your Monero Wallet address: ")
    print()
    config = {}
    config["pools"] = [{
    "url": pool,
    "user": wallet_address,
    "tls": True
    }]
    with open(config_path, "w") as file:
        json.dump(config, file, indent=4)

def choose():
    answer = input("1. supportxmr.com; 2. xmrpool.eu; 3. xmrfast.com; 4. monerohash.com; 5. herominers.com; 6. Your own variant: ")
    if answer == "1":
        print("Using supportxmr")
        print("\033[31m\033[44mAfter installation, you can still change your pool in config.json file.\033[0m")
        pool = "pool.supportxmr.com:443"
    elif answer == "2":
        print("Using xmrpool.eu")
        print("After installation, you can still change your pool in config.json file.")
        pool = "xmrpool.eu:9999"
    elif answer == "3":
        print("Using xmrfast")
        print("After installation, you can still change your pool in config.json file.")
        pool = "pool.xmrfast.com:9000" 
    elif answer == "4":
        print("Using monerohash")
        print("After installation, you can still change your pool in config.json file.")
        pool = "monerohash.com:9999"
    elif answer == "5":
        print("Using herominers's (Central European server)")
        print("After installation, you can still change your pool in config.json file.")
        pool = "monero.herominers.com:10191" 
    elif answer == "6":                                                                                                                                              
        pool = input("Enter your own pool (include the port): ")
        print("After installation, you can still change your pool in config.json file.")   
    elif answer == "7":
        print ("Glory to Ukraine!")
        pool = ("Glory to Heroes!")
    else:
        print("Invalid choice. Please, choose an existing variant.")
        sys.exit(0)
        return None
    return pool


def distro():
    answer = input ("1. Arch; 2. Debian; 3. RedHat- based distro with DNF: ")
    if answer in ("1", ""):
        print ("Installing depencies for Arch Linux")
        print ("Please, type your root password if it's needed. If you don't want to continue, press Ctrl + C")
        subprocess.call(["sudo", "pacman", "-Sy", "cmake", "make", "gcc", "git", "hwloc", "libuv", "openssl", "--noconfirm"])
    elif answer in ("2"):
        print ("Installing depencies for Debian")
        print ("Please, type your root password if it's needed. If you don't want to continue, press Ctrl + C")
        subprocess.call(["sudo", "apt", "update"])
        subprocess.call(["sudo", "apt", "install", "git", "build-essential", "cmake", "libuv1-dev", "uuid-dev", "libssl-dev"])
    elif answer in ("3"):
        print ("Installing depencies for RPM- based distro")
        print ("Please, type your root passsword if it's needed. If you don't want to continue, press Ctrl + C")
        subprocess.call(["sudo", "dnf", "update"])
        subprocess.call(["sudo", "dnf", "install", "-y", "git"," make", "cmake", "gcc", "gcc-c++", "libstdc++-static", "libuv-static", "hwloc-devel", "openssl-devel", "--skip-unavailable"])
    else:
        print ("'\033[31mPlease choose existing variant.\033[0m")
        sys.exit(0)

def depencies():
    answer = input ("Do you want to install Depencies? (y/n): ").strip().lower()
    if answer in ("y", ""):
        print("Choose your operating system")
        distro()
    else:
        print("Skipping installing depencies, user input")

usr = os.path.expanduser("~")
xmrig = os.path.expanduser("xmrig")
build = os.path.expanduser("build")
config_path = os.path.expanduser("~/xmrig/build/config.json")

threetwoone()

update = input("1. Install XMRig; 2. Update already existing config (~/xmrig/build): ")
if update in "1" or "":
    pass
elif update in "2":
    if os.path.exists(build):
        config()
        sys.exit(0)
    else:
        print("XMRig directory doesn't exist. Please, install it.")
        sys.exit(0)
else:
    print("Choose existing variant.")
    sys.exit(0)

print(f"Current directory:", os.getcwd())
depencies()

os.chdir(usr)
print(f"Current directory:", os.getcwd()) 
ask_c()


if not os.path.exists(xmrig):
    print("Cloning XMRig repository...")
    subprocess.call(["git", "clone", "https://github.com/xmrig/xmrig.git"])
else:
    print("\033[31mXMRig directory already exists. Please, delete it.\033[0m")
    sys.exit(0)

threetwoone()


os.chdir(xmrig)
subprocess.call(["mkdir", "build"])

os.chdir(build)
print(f"Current directory:", os.getcwd())
ask_c()

config()

subprocess.call (["cmake", ".."])
subprocess.call(["make", f"-j{os.cpu_count()}"])

print("\033[44mSuccesfully installed XMRig! Now, type 'cd ~/xmrig/build', and then 'sudo ./xmrig'!\033[0m")
print("Closing program.")

threetwoone()
