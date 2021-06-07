# First You should run "pip install -r requirements.txt" in your shell
import os
from requests import get

# Get External IP address / Public IP

# WAY 1
print(os.popen('curl ifconfig.me').read())

# WAY 2
print(os.popen('curl ifconfig.me/ip').read())

# WAY 3
print(os.popen('curl ifconfig.me/all').read().split("\n")[0].split(" ")[1])

# WAY 4
print(os.popen('curl "http://myexternalip.com/raw"').read())

# WAY 5
print(os.popen('nslookup myip.opendns.com resolver1.opendns.com').read().split("\n")[-3].split(" ")[-1])

# WAY 6
print('My public IP address is:', get('https://api.ipify.org').text)

# WAY 7
print('My public IP address is:', get('https://icanhazip.com/').text.strip())
