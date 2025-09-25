import os

FILE = "/data/misc/wifi/wpa_supplicant.conf"

def check_root():
    return os.geteuid() == 0

def read_wifi_passwords():
    if not os.path.isfile(FILE):
        print(f"{FILE} not found or inaccessible.")
        return

    with open(FILE, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    networks = []
    network = {}
    inside_network = False

    for line in lines:
        line = line.strip()
        if line.startswith("network={"):
            inside_network = True
            network = {}
        elif line.startswith("}"):
            inside_network = False
            if "ssid" in network:
                networks.append(network)
        elif inside_network:
            if line.startswith("ssid="):
                network["ssid"] = line.split("=",1)[1].strip().strip('"')
            elif line.startswith("psk="):
                network["psk"] = line.split("=",1)[1].strip().strip('"')

    for net in networks:
        ssid = net.get("ssid", "Unknown")
        psk = net.get("psk", "Open/No Password")
        print(f"SSID: {ssid}  -->  Password: {psk}")

if _name_ == "_main_":
    if not check_root():
        print("Please run this script as root!")
    else:
        read_wifi_passwords()
