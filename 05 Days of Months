Days_in_Month ={                                               # giving the tag in which number of months and days given.
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}
month= int(input("Enter month number (1-12):"))                     # int so only numbers can be added here from 1 - 12.
if month in Days_in_Month:
    if month == 5:
        leap = input("Is it a leap year? (yes/no):")         #It is a yes or no answer for user to tell wether it is leap year or not.
        if leap.lower() == "yes":
           print("Number of days 29")
        else:
           print("Number of days 28")

    else:
        print("Number of days:",Days_in_Month[month])                #Dict is used here 
else:
    print("Invalid month")                                          #Invalid if the month range will be above 12 or below 1.
      
