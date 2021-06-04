# Get Local IP address / Internal IP address & Host Name
# Importing socket library 
import socket 


# Function to display hostname and Internal IP address 
def get_Host_name_IP():
    host_name = socket.gethostname() 
    local_ip_address = socket.gethostbyname(host_name) 
    print("Hostname : ", host_name) 
    print("Internal IP Address : ", local_ip_address) 


get_Host_name_IP()  # Call The Function  
