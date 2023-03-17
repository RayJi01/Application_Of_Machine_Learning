# Rui Ji
# ITP 449
# HW3
# Question 1

import pandas as pd
import numpy as np

# create the dataframe required.
data = {'Attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'Name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'Qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
        'Score': [12.5, 9.0, 16.6, np.nan, 9.0, 20.0, 14.5, np.nan, 8.0, 19.0]}

df = pd.DataFrame(data)

# Write a single-line code in Python to print the name and the attempts of qualified contestants.
print(df[['Name', 'Attempts']])

# Write a single-line code in Python to print the name and the score of those contestants, who qualified with a
# single attempt.
selected_rows = df.loc[(df['Qualify'] == 'yes') & (df['Attempts'] == 1)]
print(selected_rows[['Name', 'Score']])

# Write a single-line code in Python to replace all the NaN values with Zero's in the score column of a dataframe.
# Then print the dataframe to confirm the change.
df = df.fillna(0)
print(df)

# Write a single-line code in Python to print the dataframe such that it is sorted the by attempts in ascending order
# (and score in descending order if 2 contestants have the same number of attempts.)
df_sorted = df.sort_values(by = ['Attempts', 'Score'], ascending = [True, False], inplace=False)
print(df_sorted)




