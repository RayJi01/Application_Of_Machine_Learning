# Rui Ji
# ITP 449
# HW8
# Q1
import pandas
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# 1. Read in the dataset.
raw_data = pandas.read_csv('wineQualityReds(3).csv')

# 2. Drop the wine column from the dataframe.
raw_data.drop(columns='Wine', inplace=True)

# 3. Extract the quality and store it in the different folders
qualityExtracted = raw_data['quality']

# 4. Drop the quality column from the dataframe.
raw_data.drop(columns='quality', inplace=True)

# 5. print the quality and the dataframe.
print('The whole dataset:')
print(raw_data)
print('The quality variable: ')
print(qualityExtracted)

# 6. Normalized all columns of the dataframe using the MinMaxScaler class.
normalized_model = MinMaxScaler()
normalized_model.fit(raw_data)
normalized_table = pd.DataFrame(normalized_model.transform(raw_data), columns=raw_data.columns)

# 7. Print the normalized table:
print(normalized_table)

# 8. Create a range of k values from 1-20 for k-means clustering.
# Iterate on the k values and store the inertia for each clustering in a list.
# Pass random_state = 2023 and n_init='auto' to KMeans()
ks = range(1, 21)
inertia = []

for k in ks:
    model = KMeans(n_clusters=k, random_state=2023)
    model.fit(normalized_table)
    inertia.append(model.inertia_)

# 9. Plot the chart of inertia vs number of clusters.
plt.plot(ks, inertia, 'o-')
plt.xticks(ks)
plt.xlabel('# of clusters')
plt.ylabel('Inertia')
plt.show()

# 10. What K (number of clusters) would you pick for k-means?
print("I would pick the cluster 6")

# 11. Now cluster the wines into K=6 clusters.
# Use random_state = 2023 and n_init='auto' when you instantiate the k-means model.
# Assign the respective cluster number to each wine.
# Print the dataframe showing the cluster number for each wine.
model2 = KMeans(n_clusters=6, random_state=2023)
model2.fit(normalized_table)
normalized_table['cluster'] = model2.labels_
print(normalized_table)

# 12. Add the quality back to the dataframe.
normalized_table['quality'] = qualityExtracted

# 13. Now print a crosstab (from Pandas) of cluster number vs quality.
# Comment if the clusters represent the quality of wine.
print(pd.crosstab(normalized_table["quality"], normalized_table["cluster"]))
print("the cluster does not represent the quality of wine")


