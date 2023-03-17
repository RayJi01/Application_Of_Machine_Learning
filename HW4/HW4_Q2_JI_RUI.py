# Rui Ji
# ITP 449
# HW4
# Q2


import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('data.csv')

year_column = df['Year']
Value_column = df['Value']

# to create a dash line connected scatter plot
plt.scatter(year_column, Value_column, color='red')
plt.plot(year_column, Value_column, '--', color='red')

plt.xlabel('Year')
plt.ylabel('Temperature Anomaly')
plt.title('Global Temperature')

plt.show()