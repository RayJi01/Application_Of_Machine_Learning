userInput = int(input("Enter a positive integer:"))

while userInput <= 0:
    print("The input should be a positive integer!")
    userInput = int(input("Enter a positive integer:"))

steps = 0
print(userInput)
while userInput > 1:
    if userInput % 2 == 0:                 #divided by two
        userInput = userInput/2
        print(int(userInput))
    else:
        userInput = userInput * 3 + 1
        print(int(userInput))
    steps += 1


print()
print("It took " + str(steps) + " steps to reach 1")

