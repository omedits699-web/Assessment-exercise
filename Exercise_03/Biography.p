#step1: user input:
name = input("Enter your full name: ")        #str.
hometown = input("Enter your hometown: ")     #str.

# using loop for user age:
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)                  #covert to int.
        break
    else:
        print("Enter a valid number.")

# Storing data in Dict:
user_info = { "Name": name, "Hometown": hometown, "Age": age}

# using single print statement 
print(
    user_info["Name"],
    user_info["Hometown"],
    user_info["Age"])
