# Rui Ji
# ITP 449
# HW1
# Question 3

# Write a program that prompts the user to enter a month (as a number), then prints the name of the month and the
# number of days in that month.
# Enter the month number: 9
# September has 30 days

monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
             "November", "December"]
userInput = int(input("Enter the month number:"))

# assume the user will never enter month such as 13 or bigger or 0 or lower
# assume that there is no 29 days case since there is no
# years variable been input

if userInput == 2:
    print(monthList[1] + "has 28 days")
elif userInput <= 7:
    if userInput % 2 == 0:
        print(monthList[userInput - 1] + " has 30 days")
    else:
        print(monthList[userInput - 1] + " has 31 days")
else:
    if userInput % 2 == 0:
        print(monthList[userInput - 1] + " has 31 days")
    else:
        print(monthList[userInput - 1] + " has 30 days")
