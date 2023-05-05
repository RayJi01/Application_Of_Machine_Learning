# Rui Ji
# ITP 449
# Exam 2
# Question 2

import pandas as pd
import seaborn as sn
from matplotlib import pyplot as plt

# 1. Load the file and read the dataset into a dataframe. (1)
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

raw_data = pd.read_csv('Breast_Cancer(1).csv')

# 2. Make sure there are no missing values. (2)
print(raw_data.info())  # As we see from the information, there is no missing data in the dataframe.

# 3. Explore the dataset and determine what the target variable is.
# Define the features based on all remaining columns (4)
print('Based on the research, the target variable is the first column, diagnosis')
X = raw_data.iloc[:, 1:]  # this is the feature set
y = raw_data.iloc[:, 0]  # this is the target vector.

# 4. Get a countplot of the target. (4)
sn.countplot(data=raw_data, x='diagnosis')
plt.show()

# 5. Partition the data into train and test sets (75/25). Use random_state = 2023, startify = y (3)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2023, stratify=y)

# 6. Fit the training data to a logistic regression model. (3)
model = LogisticRegression()
model.fit(X_train, y_train)

# 7. Display the accuracy, precision and recall of your predictions for diagnosis. (4)
y_pred = model.predict(X_test)
print(metrics.classification_report(y_test, y_pred))

# 8. Print and plot the confusion matrix for the test set.(4)
print(metrics.confusion_matrix(y_test, y_pred))
metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.show()

