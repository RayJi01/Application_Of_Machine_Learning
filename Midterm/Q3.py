import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

df = pd.read_csv("iris(3).csv")
print(df)

Setosa = df.loc[df['Species'] == "I. setosa"]
Virginica = df.loc[df['Species'] == "I. virginica"]
VersiColor = df.loc[df['Species'] == "I. versicolor"]

fig, axis = fig, axis = plt.subplots(ncols=2, figsize=(10, 5))
axis[0].scatter(Setosa['Petal length'], Setosa['Petal width'], color='b', label='I. setosa')
axis[0].scatter(Virginica['Petal length'], Virginica['Petal width'], color='g', label='I. Virginica')
axis[0].scatter(VersiColor['Petal length'], VersiColor['Petal width'], color='y', label='I. Versicolor')
axis[0].set_xlabel('Petal Length')
axis[0].set_ylabel('Petal Width')
axis[0].legend(loc ='upper left')

axis[1] = sn.boxplot(data=df, x='Species', y='Petal width')


plt.show()