# Speed Test Program
# First You should run "pip install -r requirements.txt" in your shell
import os

output = os.popen("speedtest-cli").read().split("\n")
if len(output) == 2:
    print("Warning")
    print("No Internet Connection, Make Sure There Is An Internet Connection And Try Again.")
    
else:
    isp = output[1][13:output[1].find("(") - 1]  # Isp
    ip = output[1].split("(")[1][:-4]  # Ip
    host = output[4].split(": ")[0]  # Host
    ping = output[4].split(": ")[1]  # Ping
    down_speed = output[6]  # Download Speed
    upload_speed = output[8]  # Upload Speed

    print("Test Completed")
    print("ISP: " + isp, "IP: " + ip, host, "Ping: " + ping, down_speed, upload_speed, sep='\n')
