import os

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
