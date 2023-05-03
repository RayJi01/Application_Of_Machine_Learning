# JI RUI
# ITP 449
# Final Project
# Question 2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sn

# 1. Perform the necessary data preparation for the stores dataframe: Extract 'Store' column and save it in a separate
# variable, then drop it from the dataframe. Standardize the dataset (use StandardScalar).

raw_data = pd.read_csv('Stores.csv')
Store_info = raw_data['Store']
raw_data.drop(columns='Store', inplace=True)
myScaler = StandardScaler()
myScaler.fit(raw_data)
standardized = pd.DataFrame(myScaler.transform(raw_data), columns=raw_data.columns)

# 2. Run k-means for k ranging from 1 to 10.  random_state = 2023, n_init='auto'
neighbours = np.arange(1, 11)
inertiaList = []
for k in neighbours:
    model = KMeans(n_clusters=k, random_state=2023)
    model.fit(standardized)
    inertiaList.append(model.inertia_)

# 3. Plot the inertias vs k.
plt.plot(neighbours, inertiaList, '.-')
plt.show()

# 4. The best k will be yield when K is 5.

# 5. What cluster does this store belong to?
model = KMeans(n_clusters=6, random_state=2023)  # Use the best k means to regenerate the model.
model.fit(standardized)

sample = [[6.3, 3.5, 2.4, 0.5]]  # the sample attributes we have.
sampleScaled = pd.DataFrame(myScaler.transform(sample), columns=standardized.columns)
print('The store belongs to ', model.predict(sampleScaled), 'cluster')

# 6. Now add the 'Store' and 'Cluster' columns to the original dataframe. Display the dataframe.
raw_data['Store'] = Store_info
raw_data['Cluster'] = model.labels_
print(raw_data)

# 7. G. Plot a histogram of cluster number.
# We can use count plot to print the histogram.
sn.countplot(data=raw_data, x='Cluster')
plt.xticks(raw_data['Cluster'])
plt.title("Cluster Number Histogram")
plt.show()


