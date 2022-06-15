#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('D:\\Desktop\\Education\\Udemy\\python_dash\\Plotly-Dashboards-with-Dash\\Data\\2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']
print(df.head())

# Use a for loop (or list comprehension to create traces for the data list)
data = []

for day in days:
    df2 = df[df['DAY'] == day]
    # What should go inside this Scatter call?
    trace = go.Scatter(
        x = df2['LST_TIME'],
        y = df2['T_HR_AVG'],
        mode = 'markers+lines',
        name = day
    )
    data.append(trace)

# Define the layout
layout = go.Layout(
    title = 'Daily temperature avgs'
)

# Create a fig from data and layout, and plot the fig

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='exercise_linechart.html')
