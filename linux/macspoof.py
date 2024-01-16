#!/usr/bin/env python3

# Import the necessary modules
import os

# Get the network interface
interface = input("Enter the network interface (e.g. eth0): ")

# Get the new MAC address
new_mac = input("Enter the new MAC address (e.g. 00:11:22:33:44:55): ")

# Change the MAC address
os.system(f"sudo ifconfig {interface} down")
os.system(f"sudo ifconfig {interface} hw ether {new_mac}")
os.system(f"sudo ifconfig {interface} up")

# Print the new MAC address
print(f"MAC address of {interface} changed to {new_mac}")
