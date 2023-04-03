# Tommy Trojan
# ITP 449
# HW6
# Q1

import pandas as pd
import matplotlib.pyplot as plt

# Preparation:
df = pd.read_csv("avocado.csv")
avocado = df[['Date', 'AveragePrice', 'Total Volume']]
avocado['Date'] = pd.to_datetime(df['Date'])
print(avocado)

# Plotting
fig, axis = plt.subplots(nrows=2, ncols=2, figsize=(30, 30))
avocado.sort_values(by='Date', ascending=True, inplace=True)

axis[0][0].scatter(avocado['Date'], avocado['AveragePrice'], s=10)
axis[0][0].set_ylabel('AveragePrice')

axis[0][1].scatter(avocado['Date'], avocado['Total Volume'], s=10)
axis[0][1].set_ylabel('Total Volume')


avocado_new = avocado.copy()
avocado_new['TotalRevenue'] = avocado['AveragePrice'] * avocado['Total Volume']
avocado1 = avocado_new.groupby('Date').sum()
avocado1['AveragePrice'] = avocado1['TotalRevenue']/avocado1['Total Volume']


axis[1][0].plot(avocado1.index, avocado1['AveragePrice'])
axis[1][0].set_ylabel('AveragePrice')

axis[1][1].plot(avocado1.index, avocado1['Total Volume'])
axis[1][1].set_ylabel('Total Volume')

smoothed = avocado1['AveragePrice'].rolling(window=20).mean()
smoothed2 = avocado1['Total Volume'].rolling(window=20).mean()
fig, axis2 = plt.subplots(ncols=2, figsize=(15,10))
axis2[0].plot(smoothed, '-o', markersize=4)
axis2[0].set_ylabel("Average Price")
axis2[1].plot(smoothed2, '-o', markersize=4)
axis2[1].set_ylabel("Total Volume")
fig.suptitle("Avocado Price and Volume Time Series")

plt.subplots_adjust(hspace=0.5)
for ax in axis.flat:
    ax.set_xticklabels(ax.get_xticklabels(), fontsize=8, rotation='vertical')

for ax2 in axis2.flat:
    ax2.set_xticklabels(ax2.get_xticklabels(), fontsize=8, rotation='vertical')

plt.show()

