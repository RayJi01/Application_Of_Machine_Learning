# Rui Ji
# ITP 449
# HW2
# Question 1

# Write a program to compute and print all possible combinations of change for $1.
# Denominations to be considered – quarter, dime, nickel, penny
# Hint: Use nested loops (loops within loops for the various denominations of coins)
# Change for $1 0 quarters, 0 dimes, 0 nickels, 100 pennies … 4 quarters, 0 dimes, 0 nickels, 0 pennies

def recursive_searching_helper(money_selections, current_cent, collections, temp_combination, v):
    if current_cent > 100:  # exceed a hundred
        return

    if current_cent == 100:
        final = temp_combination.copy()  # always remember to make a copy for the collection part.
        collections.append(final)
        return

    for i in range(len(money_selections)):
        curr = temp_combination.copy()
        curr[i] += 1
        if curr not in v:
            v.append(curr)
            recursive_searching_helper(money_selections, current_cent + money_selections[i][0], collections,
                                       curr, v)
        curr[i] -= 1

    return


money = [(1, 'pennies'), (5, 'nickels'), (10, 'dimes'), (25, 'quarters')]
c, temp_c, visited = [], [0, 0, 0, 0], [[0, 0, 0, 0]]
recursive_searching_helper(money, 0, c, temp_c, visited)

print("change for $1 are following: ")
for j in range(len(c)):
    for k in range(len(c[j])):
        print(str(c[j][k]) + " " + money[k][1], end=' ')
    print()

# all the results of combination to 100 shall be shown in the terminal and please scroll down to the bottom.
