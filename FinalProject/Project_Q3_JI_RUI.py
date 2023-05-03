# JI RUI
# ITP 449
# Final Project
# Question 3

import pandas as pd

# 1. What is the target variable?
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

raw_data = pd.read_csv('UniversalBank(1).csv')
print("According to the goals we want to achieve, the personal loan is our target value.")

# 2. Ignore the variables Row and Zip code.
raw_data.drop(columns=['Row', 'ZIP Code'], inplace=True)
print(raw_data)

# 3. Partition the data 75/25, random_state = 2023, stratify = y
target_label = raw_data['Personal Loan']
X = raw_data.drop(columns='Personal Loan')
X_train, X_test, y_train, y_test = train_test_split(X, target_label, test_size=0.25,
                                                    random_state=2023, stratify=target_label)

# 4. How many of the cases in the training partition represented people who accepted offer of a personal loan?
print("Cases in training that accepted personal loan:", sum(y_train == 1))

# 5. Plot the classification tree Use entropy criterion. max_depth = 5, random_state = 2023
ClassficationTree = DecisionTreeClassifier(criterion='entropy', random_state=2023, max_depth=5)
ClassficationTree.fit(X_train, y_train)

plt.figure(figsize=(14, 8))
plot_tree(ClassficationTree, feature_names=X.columns,
          class_names=list(map(str, ClassficationTree.classes_.tolist())), filled=True, fontsize=6)
plt.show()

# 6. On the testing partition, how many acceptors did the model classify as non-acceptors?
# 7. On the testing partition, how many non-acceptors did the model classify as acceptors?
y_pred = ClassficationTree.predict(X_test)
print(metrics.confusion_matrix(y_test, y_pred))
print('11 acceptors classified as non-acceptors.')
print('4 non-acceptors misclassified as acceptors')

# 8. What was the accuracy on the training partition?
score = ClassficationTree.score(X_train, y_train)
print("The training accuracy is " + str(score))

# 9. What was the accuracy on the test partition?
score2 = ClassficationTree.score(X_test, y_test)
print("The test accuracy is " + str(score2))


