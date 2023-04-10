# Rui Ji
# ITP 449
# HW7
# Q2

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn import metrics


# 1. read data from the csv:
raw_data = pd.read_csv('Titanic.csv')
print(raw_data)

# 2. We decided that the survived variable is the predicted target
print(raw_data.info())

# 3. The passenger number seems to be unlikely to logistic regression, so we drop it.
raw_data.drop(columns='Passenger', inplace=True)

# 4. Making sure that there is no missing data at this case.
print(raw_data.isnull().sum())

# 5. plot the count plots of the remaining columns:
plt.figure("Class column count plot")
sn.countplot(data=raw_data, x='Class')  # Count plot about Class

plt.figure("Sex column count plot")
sn.countplot(data=raw_data, x='Sex')  # Count plot about Sex

plt.figure("Age column count plot")
sn.countplot(data=raw_data, x='Age')  # Count plot about Age
plt.show()

# 6. Convert all categorical variables into dummy variables, drop first to prevent redundant feature columns.
dummied_data = pd.get_dummies(raw_data, columns=['Class', 'Sex', 'Age'], drop_first=True)
print(dummied_data.head())

# 7. Split the test set into Training and Testing (75/25), by using random state = 2023
X = dummied_data.iloc[:, 1:]   # last five are feature columns
y = dummied_data.iloc[:, 0]    # the first column is survived, which is the target column.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2023)

# 8. fit the data into a logistic models.
LogReg = LogisticRegression()
LogReg.fit(X_train, y_train)
print(LogReg.classes_)

# 9. Display the accuracy, precision and recall of your predictions for survivability
y_predict = LogReg.predict(X_test)
print(metrics.accuracy_score(y_test, y_predict))
print(classification_report(y_test, y_predict))

# 10. Display the confusion matrix along with the labels (Yes, No).
ConfusionMatrixDisplay.from_predictions(y_test, y_predict)
plt.show()

# 11. Display the predicted value of the survivability of an adult female passenger traveling 2nd class.
# for the table, the adult female passenger of 2nd class with survived yes is 1, 0, 0, 0, 0
predict_point = [[1, 0, 0, 0, 0]]
result = LogReg.predict(predict_point)
print(result)
# So the answer would be yes, she will survive










