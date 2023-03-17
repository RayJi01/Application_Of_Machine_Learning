# Tommy Trojan
# ITP 449
# HW 5
# Question 3

import pandas as pd
import matplotlib.pyplot as plt

OCT_02 = pd.read_csv('10-02-2022.csv')
COVID_Comfirmed = pd.read_csv('time_series_covid19_confirmed_US(1).csv')
COVID_Death = pd.read_csv('time_series_covid19_deaths_US(1).csv')

print(COVID_Death)
print(COVID_Comfirmed)
print(OCT_02)

OCT_02_sorted = OCT_02.sort_values('Deaths', ascending=False)
most_death = OCT_02.iloc[[0]]
print('The state with most death')
print(most_death['Province_State'])
# Answer for Question 1: The State with the most death is the Alabama

COVID_Incident = OCT_02.sort_values('Incident_Rate', ascending=True)
COVID_Incident_top = COVID_Incident.iloc[[1]]  # get the top 2 lowest state
print('The state with second lowest incident')
print(COVID_Incident_top['Province_State'])
# Answer for Question 2: The State with the second lowest incident rate is Maryland

COVID_Fatal_most = OCT_02.sort_values('Case_Fatality_Ratio', ascending=False)
COVID_Fatal_least = OCT_02.sort_values('Case_Fatality_Ratio', ascending=True)
print('The state with the most fatal')
print(COVID_Fatal_most.iloc[[0]]['Province_State'])
print('The state with the least fatal')
print(COVID_Fatal_least.iloc[[0]]['Province_State'])
# Answer for Question 3: The state with the most case fatality ratio is Grand Princess,
# and the lowest is the Diamond Princess

COVID_Comfirmed = COVID_Comfirmed.groupby('Province_State').sum(numeric_only=True)
# using groupby sum will automatically set to the groupby column
COVID_Death = COVID_Death.groupby('Province_State').sum(numeric_only=True)

df_new_case = COVID_Comfirmed.sort_values('10/4/2022', ascending=False).iloc[:5, ]
df_death = COVID_Death.sort_values('10/4/2022', ascending=False).iloc[:5, ]
print(df_death)

# Since we want the date to be on x coordinate, we have to transpose the dataframe.
df_plot_newcase = df_new_case.loc[:, '3/1/2020':].T
df_plot_death = df_death.loc[:, '3/1/2020':].T
print(df_plot_death)

# change the datetime format string to datetime object to make it better for formatting
df_plot_death.index = pd.to_datetime(df_plot_death.index)
df_plot_newcase.index = pd.to_datetime(df_plot_newcase.index)

fig, axis = plt.subplots(ncols=2, figsize=(15, 5))

# This is the datetime versus total cases based on the highest daily new cases.
axis[0].plot(df_plot_newcase)
axis[0].set_xlabel('Date')
axis[0].set_ylabel('Total Cases')
axis[0].set_title('Top 5 highest daily new cases')

# This is the datetime versus total cases based on the highest daily death cases.
axis[1].plot(df_plot_death)
axis[1].set_xlabel('Date')
axis[1].set_ylabel('Total Death')
axis[1].set_title('Top 5 highest daily death cases')

# auto format the datetime index for our x coordinate.
fig.autofmt_xdate()
plt.show()

print('highest confirmed')
print(df_plot_newcase)
print('highest death')
print(df_plot_death)
