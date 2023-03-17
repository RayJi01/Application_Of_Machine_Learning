# Tommy Trojan
# ITP 449
# HW6
# Q2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot

commuteStLouis = pd.read_csv("CommuteStLouis.csv")

# print the stats of a dataframe and create a hist for the dataframe:
print(commuteStLouis.describe())
commuteStLouis['Age'].hist()

# print the correlation of matrix
print(commuteStLouis.corr())
# Based on the result, I believe that the Time and Distance are mostly correlated with corr = 0.83

# plot the scatter matrix
pd.plotting.scatter_matrix(commuteStLouis, alpha=1, figsize=(10, 10), diagonal='hist')
# So the histogram is skew to the right, which means mean is always greater than median, which means the dataset tends
# to show that the participants are mostly younger people, have smaller distance, and spend less time generally in
# commuting.

# plot side by side boxplot with gender
sn.boxplot(x='Sex', y='Distance', data=commuteStLouis)
# Based on the side by side boxplot, the genders differences seems not present in commute distance.

# impose a time and distance plot with regression value.
model = LinearRegression(fit_intercept=True)

X = commuteStLouis[['Distance']]
y = commuteStLouis['Time']
model.fit(X, y)

myFig = plt.figure(figsize=(12, 5))
xLine = np.linspace(0, 80, num=2).reshape(-1, 1)
yLine = model.predict(xLine)

myAx1 = myFig.add_subplot(1, 2, 1)  # Subplot 1 Scatter Regression
myAx1.scatter(X, y)
myAx1.plot(xLine, yLine, "-")
myAx1.set_xlabel("Distance")
myAx1.set_ylabel("Time")
myAx1.set_title("Scatter plot and Linear Regression of Time vs Distance")

# Print the Residue distribution of the data.
myAx2 = myFig.add_subplot(1, 2, 2)  # Subplot 2, residuals
viz = ResidualsPlot(model)
viz.fit(X, y)
plt.subplots_adjust(wspace=0.3)
viz.show()

plt.show()



