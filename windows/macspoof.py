import os

# Get the network interface
interface = input("Enter the network interface (e.g. Ethernet): ")

# Get the new MAC address
new_mac = input("Enter the new MAC address (e.g. 00-11-22-33-44-55): ")

# Bring the interface down
os.system(f"Disable-NetAdapter -Name '{interface}'")

# Change the MAC address
os.system(f"Set-NetAdapter -Name '{interface}' -MacAddress '{new_mac}'")

# Bring the interface up
os.system(f"Enable-NetAdapter -Name '{interface}'")

# Print the new MAC address
print(f"MAC address of {interface} changed to {new_mac}")
