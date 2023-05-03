# JI RUI
# ITP 449
# Final Project
# Question 4

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

raw_data = pd.read_csv('mushrooms(1).csv')
myDF2 = pd.get_dummies(raw_data, columns=raw_data.columns[1:], drop_first=True)

X = myDF2.iloc[:-1, 1:]
y = myDF2.iloc[:-1, 0]

print(X)
print(y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2022, stratify=y)

Tree = DecisionTreeClassifier(max_depth=6, random_state=2022)
Tree.fit(X_train, y_train)

# 1. Print the confusion matrix. Also visualize the confusion matrix using ConfusionMatrixDisplay from sklearn.metrics
y_pred = Tree.predict(X_test)
print(metrics.confusion_matrix(y_test, y_pred))
metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.show()

# 2. What was the accuracy on the training partition?
y_pred_2 = Tree.predict(X_train)
print(metrics.accuracy_score(y_train, y_pred_2))

# 3. What was the accuracy on the test partition?
print(metrics.accuracy_score(y_test, y_pred))

# 4. Show the classification tree.
plt.figure(figsize=(14, 8))
plot_tree(Tree, feature_names=X.columns, class_names=y.unique(), filled=True, fontsize=6)
plt.show()

# 5. List the top three most important features in your decision tree for determining toxicity.
print(pd.Series(Tree.feature_importances_, index=X.columns).sort_values(ascending=False).head(3).index)

# 6. Classify the following mushroom.
sample = {'class': '', 'cap-shape': 'x', 'cap-surface': 's', 'cap-color': 'n',
          "bruises": 't',	'odor': 'y',	'gill-attachment': 'f',
          'gill-spacing': 'c',	'gill-size': 'n',
          'gill-color': 'k', 'stalk-shape': 'e', 'stalk-root': 'e', 'stalk-surface-above-ring': 's',
          'stalk-surface-below-ring': 's',	'stalk-color-above-ring': 'w',
          'stalk-color-below-ring': 'w', 'veil-type': 'p', 'veil-color': 'w',	'ring-number': 'o',
          'ring-type': 'p',	'spore-print-color': 'r',	'population': 's',	'habitat': 'u'}

# Turn the sample into a dataframe, and get the dummy value the same as we got before in the dataframe.
index_n = raw_data.shape[0]
sample = pd.DataFrame(sample, index=[0])
myDF1 = pd.concat([raw_data, sample], ignore_index=True)

myDF2 = pd.get_dummies(myDF1, columns=raw_data.columns[1:], drop_first=True)
print(myDF2)

# We have to turn that column into a 1d list of array to predict it.
print("The predicted class for the sample mushroom is " + Tree.predict([X.iloc[-1, :]]))

