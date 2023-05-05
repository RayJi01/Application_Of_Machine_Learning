# Rui Ji
# ITP 449
# Exam 2
# Question 2

import pandas as pd

# 1. Create a DataFrame “ccDefaults” to store the credit card default data and set option to display all columns
# without any restrictions on the number of columns displayed. (2)
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

pd.set_option('display.max_columns', None)
ccDefaults = pd.read_csv('ccDefaults(1).csv')

# 2. Determine the number of non-null samples and feature data types. (3)
print(ccDefaults.info())  # So as the info shows, there are no 30000 non-null samples, and all the feature datatypes
# is int

# 3. Display the first 5 rows of ccDefaults. (1)
print(ccDefaults.head(5))

# 4. Determine the dimensions of ccDefaults. (2)
print(ccDefaults.shape)  # So the dimemsion of the datasetr is 30000 * 25

# 5. Drop the ‘ID’ column from ccDefaults. (3)
ccDefaults.drop(columns='ID', inplace=True)

# 6. Drop duplicates records from ccDefaults and identify if any duplicate records are dropped
# by printing out the dimensions of ccDefaults. (2)
ccDefaults.drop_duplicates(keep='first', inplace=True)
print(ccDefaults.shape)  # So that the total row being deducted is 30000-29965 as shown in the terminal.

# 7. Print the correlation between all variable pairs. (3)
print(ccDefaults.corr())

# 8. Create a Feature Matrix, including only the 4 most correlated variables with the target, and the Target Vector.
# (4) Hint: Look at the column of the target in the correlation matrix and
# see which features have the highest correlation with the target.
top_5_related_feature_including_dpnm = ccDefaults.corr().sort_values(by='dpnm',ascending=False).head(5).index
X = ccDefaults[top_5_related_feature_including_dpnm]
X = X.drop(columns='dpnm')  # features without dpnm
y = ccDefaults.iloc[:, -1]  # the target vector.

# 9. Partition the data 70/30. (2) random_state=2023, stratify=y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2023, stratify=y)

# 10. Develop Decision Tree Classifier model. (4)  criterion=‘entropy', max_depth=4, random_state=2023
Tree = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=2023)
Tree.fit(X_train, y_train)

# 11. Display the accuracy of the model on the Test partition. (2)
print("Accuracy on test partition of the model given:", Tree.score(X_test, y_test))

# 12. Plot the confusion matrix. (3)
y_pred = Tree.predict(X_test)
print(metrics.confusion_matrix(y_test, y_pred))
metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.show()

# 13. Plot the Decision Tree.
cn = list(map(str, Tree.classes_.tolist()))
plot_tree(Tree, feature_names=X.columns, class_names=cn, filled=True)
plt.show()

