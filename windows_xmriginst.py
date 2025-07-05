#Simple script to install and mine monero thru XMRig on Windows. Some parts of the code were created by chatgpt
import requests
import shutil
import zipfile
import time
import json
from time import sleep
import os
import sys
from pathlib import Path

usr = os.path.expanduser("~")
xmrig = os.path.join(usr, "xmrig")
config_path = os.path.join(xmrig, "config.json")


def threetwoone():
        for i in range(3, 0, -1):
                sys.stdout.write(f"\r{i}... ")
                sys.stdout.flush()
                time.sleep(1)
        print()

def config():
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

def ask_c():
    answer = input("Continue? (y/n): ").strip().lower()
    if answer not in ("y", ""):
        print ("\033[91mStopped by user!\033[0m")
        sys.exit(0)

def choose():
    answer = input ("1. supportxmr.com; 2. xmrpool.eu; 3. xmrfast.com; 4. monerohash.com; 5. herominers.com; 6. Your own variant: ")
    if answer == ("1"):
        print("Using supportxmr")
        print("\033[31m\033[44mAfter installation, you can still change your pool in config.json file.\033[0m")
        pool = "pool.supportxmr.com:443"
    elif answer == ("2"):
        print("Using xmrpool.eu")
        print("After installation, you can still change your pool in config.json file.")
        pool = "xmrpool.eu:9999"
    elif answer == ("3"):
        print("Using xmrfast")
        print("After installation, you can still change your pool in config.json file.")
        pool = "pool.xmrfast.com:9000" 
    elif answer == ("4"):
        print ("Using monerohash")
        print("After installation, you can still change your pool in config.json file.")
        pool = "monerohash.com:9999"
    elif answer == ("5"):
        print ("Using herominers (Central European server)")
        print("After installation, you can still change your pool in config.json file.")
        pool = "monero.herominers.com:10191" 
    elif answer == ("6"):
        pool = input("Enter your own pool (include the port): ")
        print("After installation, you can still change your pool in config.json file.")
    elif answer == ("7"):
        print("Glory to Ukraine!")
        pool = "Glory to Heroes!"
    else:
        print("Invalid choice. Please, choose existing variant. Also, delete the xmrig folder in C:Users/yourusername/")
        sys.exit(0)
    return pool

def dxmrig():
    url = "https://github.com/xmrig/xmrig/releases/download/v6.22.2/xmrig-6.22.2-msvc-win64.zip"
    usr = os.path.expanduser("~")
    install_folder = ("xmrig")
    xmrig_path = os.path.join(usr, install_folder)  
    zip_path = os.path.join(usr, "xmrig.zip")  

    print("Downloading XMRig...")
    response = requests.get(url, stream=True)
    with open(zip_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    print("Extracting...")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        temp_extract_path = os.path.join(usr, "xmrig_temp") 
        zip_ref.extractall(temp_extract_path)

        
        extracted_folder = os.path.join(temp_extract_path, os.listdir(temp_extract_path)[0])
        if not os.path.exists(xmrig_path):
            os.makedirs(xmrig_path)

        for item in os.listdir(extracted_folder):
            shutil.move(os.path.join(extracted_folder, item), xmrig_path)

        shutil.rmtree(temp_extract_path)  

    os.remove(zip_path)  

    print(f"XMRig Succesully downloaded in {xmrig_path}")

threetwoone()

update = input("1. Install XMRig; 2. Update already existing config (YourUsername/xmrig/): ")
if update in "1":
    pass
elif update in "2":
    if os.path.exists(xmrig):
        config()
        sys.exit(0)
    if not os.path.exists(xmrig):
        print ("XMRig directory doesn't exist. Please, install it")
        sys.exit(0)
else:
    print ("Please, choose an existing variant.")
    sys.exit(0)

os.chdir(usr)
print(f"Current directory:", os.getcwd()) 
 
ask_c()
if not os.path.exists(xmrig):
    dxmrig()
else:
    print("XMRig directory already exists.")
    sys.exit(0)
threetwoone()
os.chdir(xmrig)

print(f"Current directory:", os.getcwd())
ask_c()

config()

print("Succesfully installed XMRig! Now, open 'xmrig.exe' in 'C:/Users/YourUsername/xmrig/' Enjoy this and please, support my project with a star!")
print("Closing program.")

threetwoone()
