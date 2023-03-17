import pandas as pd
import matplotlib.pyplot as plt


# 1 Load the dataframe
df = pd.read_csv("BTC_USD.csv")
print(df)

# 2 Convert date to datetime and then set index
df['Date'] = pd.to_datetime(df['Date'])
df_edited = df.set_index('Date', inplace=False)
print(df_edited)

# 3 What is the difference between the highest and lowest price of a Bitcoin in 2022?
highest = df_edited['High'].max()  # since the highest price must been retain when high price recorded.
lowest = df_edited['Low'].min()  # since the lowest price must be obtained when low price is recorded
differences = highest - lowest
print("The differences between highest and lowest price is " + str(differences))

# 4 How many days it took for Bitcoin to reach its lowest value since it hit its highest value in 2022?
highestpos = df.sort_values(by = ['High'], ascending=False).head(1)
after2022 = df.loc[df['Date'] > '2022-11-10']
lowestpos = after2022.sort_values(by = ['Low'], ascending=True).head(1)
dateHighest = highestpos.iat[0, 0]
dateLowest = lowestpos.iat[0, 0]
print("date used: ")
print(dateLowest - dateHighest)
print()
# use 376 days to reach the lowest after it reach the maximum.

# 5 How many Bitcoins were traded during the day that it hit its highest price (Sep 2014 - present)?
volume = highestpos.iat[0, -1]
print("Bitcoins traded at the highest value: " + str(volume))
print()

# 6 Plot the price of Bitcoin vs time (Note: Use Close price) and its 50-Day-Moving-Average on the same figure (Sep
# 2014 - present). (Note: Use Close price to calculate moving average. Add legend to the plot)
movingAverage = df_edited.Close.rolling(50).mean()
plt.plot(df_edited.index, df_edited["Close"], label="Everyday Graph")
plt.plot(df_edited.index, movingAverage, label="Average 50 days Graph")
plt.xlabel("Time")
plt.ylabel("Close Price of Bitcoin")
plt.legend()
plt.show()


