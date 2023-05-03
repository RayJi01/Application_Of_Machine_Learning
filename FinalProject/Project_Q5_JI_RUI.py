# JI RUI
# ITP 449
# Final Project
# Question 5

import pandas as pd

# 1. Create a DataFrame “diabetes_knn” to store the diabetes data and set option to display all columns without any
# restrictions on the number of columns displayed.
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

pd.set_option('display.max_columns', None)
diabetes_knn = pd.read_csv('diabetes(3).csv')
print(diabetes_knn)

# 2. Determine the dimensions of the “diabetes_knn” dataframe.
print(diabetes_knn.shape)
# So the dimension is a 769 * 9 dataframe.

# 3. Update the DataFrame to account for missing values if needed.
diabetes_knn.fillna(0, inplace=True)

# 4. Create the Feature Matrix and Target Vector
X = diabetes_knn.iloc[:, 0:-1]
y = diabetes_knn.iloc[:, -1]

# 5. Standardize the attributes of Feature Matrix
# (https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
scaler = StandardScaler()
scaler.fit(X)
Scaled = pd.DataFrame(scaler.transform(X), columns=X.columns)

# 6. Split the Feature Matrix and Target Vector into train A (70%) and train B sets (30%).
# Use random_state=2023, and stratify based on Target vector.
X_train, X_test, y_train, y_test = train_test_split(Scaled, y, test_size=0.3, random_state=2022, stratify=y)

# 7. Develop a KNN based model and obtain KNN score (accuracy) for train A and train B
# data for k’s values ranging between 1 to 8.
KRange = range(1, 9)
accuraciesA = []
accuraciesB = []
for k in KRange:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    y_predA = model.predict(X_train)
    y_predB = model.predict(X_test)
    accuraciesA.append(metrics.accuracy_score(y_train, y_predA))
    accuraciesB.append(metrics.accuracy_score(y_test, y_predB))
print(accuraciesA)
print(accuraciesB)

# 8. Plot a graph of train A and train B score and determine the best value of k.
plt.plot(KRange, accuraciesA, label='TrainA')
plt.plot(KRange, accuraciesB, label='TrainB')
plt.legend()
plt.show()

# 9.
# Display the score of the model with best value of k. 
# Also print and plot the confusion matrix for Train B, using Train A set as the reference set for training.
k_opt = 6
model = KNeighborsClassifier(n_neighbors=k_opt)
model.fit(X_train, y_train)
print("The score of the model is ", model.score(X_train, y_train))

# 10. Predict the Outcome for a person with pregnancies=6, glucose=140, blood pressure=60,
# skin thickness=12, insulin=300, BMI=24, diabetes pedigree=0.4, age=45.
sample = pd.DataFrame([[6, 140, 60, 12, 300, 24, 0.4, 45]], columns=X.columns)
sampleScaled = pd.DataFrame(scaler.transform(sample), columns=X.columns)
print("The predicted result would be: " + str(model.predict(sampleScaled)))
