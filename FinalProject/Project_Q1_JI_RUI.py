# JI RUI
# ITP 449
# Final Project
# Question 1
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# 1. Create a DataFrame “diabetes_knn” to store the diabetes data and set option
# to display all columns without any restrictions on the number of columns displayed.
raw_data = pd.read_csv('winequality(1).csv')
print(raw_data.head())

# 2. Standardize all the column instead of the Quality column:
standardScaler = StandardScaler()
# Extract the data that needed to be transform.
X = raw_data.iloc[:, :-1]
label = raw_data.iloc[:, -1]
standardScaler.fit(X)
scaled_data = pd.DataFrame(standardScaler.transform(X), columns=X.columns)
print(scaled_data)

# 3. Partition the DataSet:
X_train, X_test, y_train, y_test = train_test_split(scaled_data, label, test_size=0.20, random_state=2023, stratify=label)
x_trainA, x_trainB, y_trainA, y_trainB = train_test_split(X_train, y_train, test_size=0.25, random_state=2023,
                                                          stratify=y_train)

# 4. Build a KNN classification model to predict Quality based on all the remaining numeric variables.
# 5. Iterate on K ranging from 1 to 30. Plot the accuracy for the train A and train B datasets.
trainA_Accuracy = []
trainB_Accuracy = []
neighbors = np.arange(1, 31)
for k in neighbors:
    model1 = KNeighborsClassifier(n_neighbors=k)
    model1.fit(x_trainA, y_trainA)
    y_predA = model1.predict(x_trainA)
    y_predB = model1.predict(x_trainB)
    trainA_Accuracy.append(metrics.accuracy_score(y_trainA, y_predA))
    trainB_Accuracy.append(metrics.accuracy_score(y_trainB, y_predB))

# 6. Which value of k produced the best accuracy in the train A and train B data sets? Generate predictions for the test
# partition with the chosen value of k. Print and plot the confusion matrix of the actual vs predicted wine quality.
print(trainB_Accuracy)
print(trainA_Accuracy)
plt.plot(neighbors, trainA_Accuracy, "--r", label="Train A")
plt.plot(neighbors, trainB_Accuracy, '--b', label="Train B")
plt.xlabel("number of neighbors (k)")
plt.ylabel("Accuracy")
plt.legend()
plt.xticks(neighbors)
plt.show()
print('As the graph shows, the best value of K is 27 where the trainB accuracy is the highest.')

# Need to double-check with the exact answers.
k_opt = 27
model = KNeighborsClassifier(n_neighbors=k_opt)
model.fit(x_trainA, y_trainA)

y_pred = model.predict(X_test)
print(metrics.confusion_matrix(y_test, y_pred))
metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.show()


test_DF = X
test_DF['Quality'] = raw_data['Quality']
test_DF['Predicted Quality'] = model.predict(X.iloc[:, :-1])
print(test_DF)

print("Accuracy Score is " + str(metrics.accuracy_score(y_test, y_pred)))


