# Rui Ji
# ITP 449
# Exam 2
# Question 1

import pandas as pd
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# 1. Create a DataFrame “wineDf” to store the wine data. (2)
wineDF = pd.read_csv('wineQualityReds(2).csv')

# 2. Determine the dimensions of the “wineDf” dataframe. (2)
print(wineDF.shape)

# 3. Check (and Update) the DataFrame to account for missing values. (2)
print(wineDF.info())  # As we see from the terminal, there is no missing value.

# 4. Create the Feature Matrix and Target Vector. (2)
wineDF.drop(columns='Wine', inplace=True)  # drop the useless first column.
X = wineDF.iloc[:, :-1]  # feature
y = wineDF.iloc[:, -1]  # target

# 5. Standardize the attributes of Feature Matrix (use StandardScaler) (2)
scaler = StandardScaler()
scaler.fit(X)
scaled = pd.DataFrame(scaler.transform(X), columns=X.columns)

# 6. Split the Feature Matrix and Target Vector into three partitions.
# Train A, Train B, and Test with the ratio of 50-25-25. (4)  random_state=2023, stratify=y
X_train, X_test, y_train, y_test = train_test_split(scaled, y, test_size=0.25, random_state=2023, stratify=y)
X_trainA, X_trainB, y_trainA, y_trainB = \
    train_test_split(X_train, y_train, test_size=1 / 3, random_state=2023, stratify=y_train)

# 7. How many cases are in the Train partition? (2)
print('There are ' + str(len(X_train)) + '  in Train Partition')

# 8. How many cases are in the Test partition? (2)
print('There are ' + str(len(X_test)) + ' cases in Train Partition')

# 9. Develop a kNN model based on Train A for various ks. k should range between 1 and 30. (4)
# 10. Compute the kNN score (accuracy) for Train A and Train B data for those ks. (2)
krange = range(1, 31)
accuracy_TrainA = []
accuracy_TrainB = []
for k in krange:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_trainA, y_trainA)
    y_predA = model.predict(X_trainA)
    y_predB = model.predict(X_trainB)
    accuracy_TrainA.append(metrics.accuracy_score(y_trainA, y_predA))
    accuracy_TrainB.append(metrics.accuracy_score(y_trainB, y_predB))

# 11. Plot a graph of Train A and Train B accuracy and determine the best value of k. Label the plot. (4)
plt.plot(krange, accuracy_TrainA, label='Train A')
plt.plot(krange, accuracy_TrainB, label='Train B')
plt.xlabel('# of Neighbors (k)')
plt.ylabel('Accuracy')
plt.legend()
plt.xticks(krange)
plt.show()  # From the graph, we can determine that the best k shall be 23

# 12. Now, using the selected value of k, score the Test data set (2)
best = 23
model = KNeighborsClassifier(n_neighbors=best)
model.fit(X_trainA, y_trainA)
print("Score of the test set:", model.score(X_test, y_test))

# 13. plot the confusion matrix
y_pred = model.predict(X_test)
print(metrics.confusion_matrix(y_test, y_pred))
metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.show()

# 14. Accuracy on the Train A partition
print("Accuracy on the Train A partition:", metrics.accuracy_score(y_trainA, y_predA))
print("")

# 15. Accuracy on the Train B partition
print("Accuracy on the Train B partition:", metrics.accuracy_score(y_trainB, y_predB))
print("")

# 16. Predict the wine quality of this wine
sample = pd.DataFrame([[8, .6, 0, 2, .067, 10, 30, .9978, 3.2, .5, 10]], columns=X.columns)
sampleScaled = pd.DataFrame(scaler.transform(sample), columns=X.columns)
print("Predicted quality of this wine:", model.predict(sampleScaled))

