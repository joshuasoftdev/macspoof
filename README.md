# Mac Spoof

This project provides a simple Python script to spoof the MAC address of a network interface on a Windows machine. MAC address spoofing is a technique used to change the Media Access Control (MAC) address of a network interface, allowing the user to impersonate a different device on a network.

## Usage

To use this script, follow these steps:

1. Open a command prompt or terminal window.
2. Navigate to the directory containing the `macspoof.py` script.
3. Run the script by typing `python macspoof.py`.
4. When prompted, enter the name of the network interface you wish to spoof (e.g., Ethernet).
5. Enter the new MAC address you wish to assign to the network interface (e.g., 00-11-22-33-44-55).

The script will then disable the specified network interface, change its MAC address, re-enable the interface, and print out the new MAC address.

## Note

This script uses the `os.system()` function to execute PowerShell commands. Therefore, it requires administrative privileges to run successfully. Also, please ensure that the MAC address you enter is valid and follows the correct format (XX-XX-XX-XX-XX-XX).

## Reminder

remember to change the mac address back to the original one after you are done with your work. SO TAKE NOTE OF THE ORIGINAL MAC ADDRESS BEFORE YOU CHANGE IT.

## Disclaimer

While this tool can be used for legitimate purposes such as bypassing network restrictions or enhancing privacy, it can also be misused for malicious activities. Please use it responsibly and in accordance with all applicable laws and regulations.
