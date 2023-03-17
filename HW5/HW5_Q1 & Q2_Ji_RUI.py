# Tommy Trojan
# ITP 449
# HW 5
# Question 1 & 2

import pandas as pd

# --------------------------------------------Read in the CSV and print ----------------------------------------------#
df = pd.read_csv('mtcars.csv')
print(df)

# ---------------------------------------------Set Index to Car Name --------------------------------------------------#
df.set_index('Car Name', inplace=True)
print(df)

# -------------------------------------------Slice on part of Dataframe and rename-------------------------------------#
new_df = df[['cyl', 'gear', 'hp', 'mpg']]
new_df_rename = new_df.rename(
    columns={'cyl': 'Cylinders', 'gear': 'Gear', 'hp': 'Horsepower', 'mpg': 'Miles per Gallon'})
print(new_df_rename)

# ----------------------------------------Added a powerful col and delete horsepower-----------------------------------#
new_df_rename['Powerful'] = new_df_rename['Horsepower'] >= 110
print(new_df_rename)
new_deletedhp = new_df_rename.drop('Horsepower', axis=1)
print(new_deletedhp)

# -----------------------------------Sort the subset of mpg > 25 and select the powerful-------------------------------#
new_subset = new_df_rename[new_df_rename['Miles per Gallon'] > 25.0]
sorted_new = new_subset.sort_values('Horsepower', ascending=False)
print(sorted_new)
filtered = sorted_new[sorted_new['Powerful'] == True]
print(filtered)
