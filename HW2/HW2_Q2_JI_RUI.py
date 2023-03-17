# Rui Ji
# ITP 449
# HW2
# Question 2

# Ask the user to enter two positive integers between 1 and 100.
# Read those integers. Then output a multiplication table of the first number times the second number.
# Please enter an integer: 5
# Please enter another integer: 20
# 5 x 1 = 5 5 x 2 = 10 5 x 3 = 15 … 5 x 20 = 100

user_input1 = input("Please enter an integer: ")
user_input2 = input("Please enter another integer: ")

for i in range(int(user_input2)):
    print(str(user_input1) + " x " + str(i+1) + " = " + str(int(user_input1) * (i+1)))
