names = ["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"] # making list 

search_name = input("Enter name to find:") # Using input to find the name from list.

found = False                      #if name will not be in the list
for name in names:                #if name is in the names.
    if name == search_name:
        found = True
        break                  # break will stop the loop
if found:
    print("Found the name")
else:
    print("No name found")
