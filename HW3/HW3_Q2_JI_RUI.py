# Rui Ji
# ITP 449
# HW3
# Question 2

import pandas as pd
import numpy as np

# Read the csv file using Pandas. Store the output into a dataframe named DF. Then print DF
df = pd.read_csv("Trojans_roster.csv")
print(df)

# You notice that the index is 0 ... 109. There is a column #. Set the index of the dataframe to #. In other words,
# make the player’s number column the index of DF. Print DF to make sure that the change happened.
df.set_index('#', inplace=True)
print(df)

# Remove the ‘LAST SCHOOL’ and ‘MAJOR’ columns from the dataframe. Print DF to make sure that the change happened.
df.drop(['LAST SCHOOL', 'MAJOR'], axis=1, inplace=True)
print(df)

# Write a single-line code in Python to print the names of all the Quarterbacks in the team.
print(df.loc[(df['POS.'] == 'QB')])

# Write a single-line code in Python to print the name, position, height, and weight of the tallest player in the team.
print(df.loc[(df['HT.'] == df['HT.'].max())][['NAME', 'POS.', 'HT.', 'WT.']])

# Write a single-line code in Python to print how many players are local (i.e., their hometown is ‘LOS ANGELES, CA’).
# Note that the answer is a number.
print((df['HOMETOWN'] == "Los Angeles, CA").sum())

# Write a single-line code in Python to print the info of 3 heaviest players.
print(df.nlargest(3, 'WT.'))

# Define a new column for DF named BMI, which contains the BMI of the players. Print DF to make sure that the change
# happened.
df['BMI'] = (703 * df['WT.']) / (df['HT.'] * df['HT.'])
print(df)

# Write single-line codes in Python to print the mean and median of players’ height, weight, and BMI.
print("mean: ")
print(df[['HT.', 'WT.', 'BMI']].mean())
print("median: ")
print(df[['HT.', 'WT.', 'BMI']].median())

# Write single-line codes in Python to print the mean and median of players’ height, weight, and BMI for each position.
print("mean: ")
print(df.groupby('POS.')[['HT.', 'WT.', 'BMI']].mean())
print("median: ")
print(df.groupby('POS.')[['HT.', 'WT.', 'BMI']].median())

# Write a single-line code in Python to print the number of players in each position.
print(df.groupby('POS.')['NAME'].count())

# Write a single-line code in Python to print the names of the players whose BMI is below the team average (mean)
print(df.loc[(df['BMI'] <= df['BMI'].mean())][['NAME']])

# Write a single-line code in Python to print all the unique players’ numbers. (unique numbers in DF index)
print(df.index.unique())  # this return a array of unique number.
