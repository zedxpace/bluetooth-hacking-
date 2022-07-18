import bluetooth

bluetooth_devices = bluetooth.discover_devices(lookup_names=True ,lookup_class=True)

for device in bluetooth_devices:
    print("[+] " + device[0] + " " + device[1])