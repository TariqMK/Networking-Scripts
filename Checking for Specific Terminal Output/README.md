# Checking for Specific Terminal Output

## Intent
This script is used to return the IP Address of a Cisco Router/Switch that returns specific output on the terminal in response to a user-defined IOS Command.

## Usage
1. Ensure you have a file named `devices.txt` in the same directory as the script containing a list of all the Router/Switch IP Addresses that you wish to query. 1 entry per line.
2. The Script will open the file and iterate through each IP Address, connecting via SSH using the credentials you enter
3. The Script will then enter the command you specify by replacing the text labelled: `[COMMAND]`
4. Should the script encounter the user-provided text in the output (entered by replacing `[]`), it will print the IP Address of the Router/Switch
5. Once the Script has iterated through each device in the list, it will disconnect the SSH session
