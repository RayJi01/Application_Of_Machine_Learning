# Rui Ji
# ITP 449
# HW7
# Q1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.linear_model import LinearRegression, Ridge
from yellowbrick.regressor import ResidualsPlot

raw_data = pd.read_csv('auto-mpg.csv')

print(raw_data.describe())
# A. based on the summary of the data, the mean of the mpg is 23.51
# B. the median of the mpg is 23

raw_data['mpg'].plot(kind='density')
plt.xlabel('Values')
plt.ylabel('Density')
plt.title(f'Skewness of Column mpg')
plt.show()
# C. from previous two questions, we see the mean is bigger than median, that means the graph is skew to the right
# and the graph plotted above shows the skewness is really point to the right.

# D. Plot the pairplot matrix of all relatable features.
sb.pairplot(raw_data, size=2, aspect=1.5)
plt.show()

new_data_without_No = raw_data.drop('No', axis=1)
df = new_data_without_No.corr()

sorted_pairs = df.abs().unstack().sort_values(ascending=False)
max_corr_features = sorted_pairs[sorted_pairs.index.get_level_values(0) != sorted_pairs.index.get_level_values(1)].head(1)
down_sorted = df.abs().unstack().sort_values(ascending=True)
min_corr_features = down_sorted[down_sorted.index.get_level_values(0) != down_sorted.index.get_level_values(1)].head(1)
# E. according to the matrix, the displacement and cylinders seems to be most correlated, even though there are other
# features such as displacement and horsepower are also having very strong correlations.
print(max_corr_features)
# F. according to the matrix, the accleration and the model year seems to be the least correlated. Model year also
# has small correlation with features like horsepower.
print(min_corr_features)


# G. produce a scatter plot of displacement and mpg
plt.scatter(raw_data['displacement'], raw_data['mpg'], s=10)
plt.xlabel('displacement')
plt.ylabel('mpg')
plt.title('mpg vs. displacement')
plt.show()

# H. Build a linear regression model where displacement is predictor as x and mpg is target as y
model = LinearRegression()
x = np.array(raw_data['displacement'], dtype=np.float64)
X = np.array(x[:, np.newaxis], dtype=np.float64)
y = raw_data['mpg']
model.fit(X, y)

y_predicted = model.predict(X)
plt.plot(x, y_predicted)
plt.show()

coefficients = model.coef_
intercept = model.intercept_
print(coefficients)
print(intercept)

# H.a For my Linear Model, the coefficient of that Model is -0.06028241
# H.b For my Linear Model, the intercept of that Model is 35.174750
# H.c so that based on Y = coe * X + intercept --> My function shall be Y = -0.0603* X + 35.175 where Y stands for mpg
# and X stands for displacement.
# H.d Since the coefficient is smaller than 0, then as displacement increase, the mpg will decrease.
# H.e By the function of Y = -0.0603 * X + 35.175, if x = 200, then mpg = Y = 23.115
# Note: for H.e, if see directly from the graph, it should be around 23.07.

# H.f display a scatter plot of mpg vs. displacement and superimpose the regression line.
plt.scatter(x, y)
plt.plot(x, y_predicted)
plt.show()

# H.g Plot the residuals
ridge = Ridge()
visualizer = ResidualsPlot(ridge)
visualizer.fit(X, y)
visualizer.show()

