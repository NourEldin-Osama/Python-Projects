# Image Colorization Program
# First You should run "pip install -r requirements.txt" in your shell
import requests  # we will use requests to call API
import os  # To Get The Path

print("Welcome to Image Colorization Program")
choice = input("Do you want to Colorize a local photo or online photo, Enter L (for local) or O (for Online): ")
if choice.upper() == "L":
    # Take IMAGE Path From User
    print("MAKE SURE YOU PUT THE IMAGE IN THE SAME FOLDER")
    IMAGE_PATH = os.path.join(os.getcwd(), input("Please Enter Your IMAGE NAME: "))

    # send data with API
    Response = requests.post(
        "https://api.deepai.org/api/colorizer", files={'image': open(IMAGE_PATH, 'rb')},
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )

elif choice.upper() == "O":
    # Take IMAGE URL From User
    IMAGE_URL = input("Please Enter Your IMAGE URL : ")
    # send data with API
    Response = requests.post("https://api.deepai.org/api/colorizer", data={'image': IMAGE_URL},
                             headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
                             )

else:
    print("invalid Choice")
    exit(0)

output_url = Response.json()['output_url']
print("The Result Output:", output_url)

answer = input("Do You Want To Download The Image In Your Device? Y (for YES) or N (for NO): ")

if answer.upper() == "Y":
    # Download The Image
    response = requests.get(output_url)
    name = input("Enter The IMAGE NAME: ") + ".png"
    with open(name, "wb") as file:
        file.write(response.content)
    print("The IMAGE " + name + " has been Downloaded")

else:
    print("The IMAGE will not be Downloaded")

print("The Program Finished Successfully")
