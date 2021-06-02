
# Calculate the available disk space
import shutil
import psutil

# Function to Convert Bytes to GigaBytes
toGigaBytes = lambda x: int(x / (1024 ** 3))

# Calculate the available disk space (C:/) in bytes
C_Usage = shutil.disk_usage("C:/")
C_Total_Space = C_Usage.total  # C:/ Total Space
C_Total_Space_GB = toGigaBytes(C_Total_Space)  # Convert to GigaBytes
C_used_space = C_Usage.used  # C:/ Used Space
C_used_space_GB = toGigaBytes(C_used_space)  # Convert to GigaBytes
C_free_space = C_Usage.free  # C:/ Free Space
C_free_space_GB = toGigaBytes(C_free_space)  # Convert to GigaBytes
free_space_percent_C = (C_free_space / C_Total_Space) * 100  # The percentage of free C disk_space
used_space_percent_C = (C_used_space / C_Total_Space) * 100  # The percentage of used C disk_space

print("The Total disk space in C: {} GB".format(C_Total_Space_GB))
print("The used disk space in C: {} GB".format(C_used_space_GB))
print("The available disk space in C: {} GB".format(C_free_space_GB))
print("The percentage of free C disk space: {:.2F}%".format(free_space_percent_C))
print("The percentage of used C disk space: {:.2F}%".format(used_space_percent_C))
print("-" * 50)

# Calculate the available disk space (D:/) in bytes
D_usage = shutil.disk_usage("D:/")
D_total_space = D_usage.total  # D:/ Total Space
D_total_space_GB = toGigaBytes(D_total_space)  # Convert to GigaBytes
D_used_space = D_usage.used  # D:/ Used Space
D_used_space_GB = toGigaBytes(D_used_space)  # Convert to GigaBytes
D_free_space = D_usage.free  # D:/ Free Space
D_free_space_GB = toGigaBytes(D_free_space)  # Convert to GigaBytes
free_space_percent_D = (D_free_space / D_total_space) * 100  # The percentage of free D disk space
used_space_percent_D = (D_used_space / D_total_space) * 100  # The percentage of used D disk space

print("The Total disk space in D: {} GB".format(D_total_space_GB))
print("The used disk space in D: {} GB".format(D_used_space_GB))
print("The available disk space in D: {} GB".format(D_free_space_GB))
print("The percentage of free D disk space: {:.2F}%".format(free_space_percent_D))
print("The percentage of used D disk space: {:.2F}%".format(used_space_percent_D))
print("-" * 50)

# Battery usage details
battery = psutil.sensors_battery()
if battery.power_plugged:
    print("The battery is Charging")
else:
    print("The Battery isn't Charging")
    print((int(battery.secsleft/60)), "Minutes Remaining")
print("Battery Percentage {}%".format(battery.percent))
print("-" * 50)

# Check Memory (Ram) usage
ram_info = [toGigaBytes(i) for i in psutil.virtual_memory()]
print("Total Ram Space: {} GB".format(ram_info[0]))
print("Used Ram Space Percentage: {}%".format(psutil.virtual_memory().percent))
print("Available Ram Space: {} GB".format(ram_info[1]))
print("Used Ram Space: {} GB".format(ram_info[3]))
print("-" * 50)

# Check Cpu usage

# If the usage of cpu less than 75 that is meanings every thing is ok .
# The 1 is the time it take to give you the average you can change it .
print("Cpu Usage Percentage: {}%".format(psutil.cpu_percent(1)))
