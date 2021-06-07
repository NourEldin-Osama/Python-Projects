# First You should run "pip install -r requirements.txt" in your shell
import shutil
import psutil

# Function to Convert Bytes to GigaBytes
toGigaBytes = lambda x: int(x / (1024 ** 3))


# Calculate the available disk space
def Disk_Usage(path):
    Usage = shutil.disk_usage(path)
    Total_Space = Usage.total  # Total Space
    Total_Space_GB = toGigaBytes(Total_Space)  # Convert to GigaBytes
    used_space = Usage.used  # Used Space
    used_space_GB = toGigaBytes(used_space)  # Convert to GigaBytes
    free_space = Usage.free  # Free Space
    free_space_GB = toGigaBytes(free_space)  # Convert to GigaBytes
    free_space_percent = (free_space / Total_Space) * 100  # The percentage of free disk space
    used_space_percent = (used_space / Total_Space) * 100  # The percentage of used disk space

    print("The Total disk space in {}: {} GB".format(path[0], Total_Space_GB))
    print("The used disk space in {}: {} GB".format(path[0], used_space_GB))
    print("The available disk space in {}: {} GB".format(path[0], free_space_GB))
    print("The percentage of free {} disk space: {:.2F}%".format(path[0], free_space_percent))
    print("The percentage of used {} disk space: {:.2F}%".format(path[0], used_space_percent))


# Calculate the available disk space (C:/) in bytes
Disk_Usage("C:/")
print("-" * 50)

# Calculate the available disk space (D:/) in bytes
Disk_Usage("D:/")
print("-" * 50)

# Battery usage details
battery = psutil.sensors_battery()
if battery.power_plugged:
    print("The battery is Charging")
else:
    print("The Battery isn't Charging")
    print((int(battery.secsleft / 60)), "Minutes Remaining")
print("Battery Percentage {}%".format(battery.percent))
print("-" * 50)

# Check Memory (Ram) usage
print("Used Ram Space Percentage: {}%".format(psutil.virtual_memory().percent))
ram_info = [toGigaBytes(i) for i in psutil.virtual_memory()]
print("Total Ram Space: {} GB".format(ram_info[0]))
print("Available Ram Space: {} GB".format(ram_info[1]))
print("Used Ram Space: {} GB".format(ram_info[3]))
print("-" * 50)

# Check Cpu usage

# If the usage of cpu less than 75 that is meanings every thing is ok .
# The 1 is the time(in Seconds) it take to give you the average you can change it .
print("Cpu Usage Percentage: {}%".format(psutil.cpu_percent(1)))
