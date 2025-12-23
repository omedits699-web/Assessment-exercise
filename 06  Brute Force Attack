Correct_password = "admin"
attempts = 5                                                                      # maximum of 5 password attempts                                                                      

while attempts >0:                                       #If the user enters the wrong password, inform them of the remaining attempts
    password = input("Enter the password:")                        #user to input password

    if password == Correct_password:                          #if password will be correct user will get access.
        print("Access granted")
        break
    else:

        attempts = attempts - 1                              # on each wrong passsword user will lost his attempt numbers which are maximum 5.
        if attempts> 0:
            print("Wrong password.  Attempts remaining:",attempts)
        else:
            print("authorities have been alerted.")                                    # if the maximum number of attempts is reached
