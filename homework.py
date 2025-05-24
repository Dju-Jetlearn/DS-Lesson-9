import pandas as pd
import numpy as np
import matplotlib.pyplot as matpat
import plotly
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("C:/Users/diego/JetLearn/Data Science/Lesson 9/covid_data.csv")

data = data[['Province_State', 'Country_Region', 'Last_Update', 'Lat', 'Long_', 'Confirmed', 'Recovered', 'Deaths', 'Active']]

data.columns = ('State', 'Country', 'Last Update', 'Lat', 'Long', 'Confirmed', 'Recovered', 'Deaths', 'Active')

print(data.head())

data['State'].fillna(value = '', inplace = True)

# Scatter Graphs

top10_confirmed = pd.DataFrame(data.groupby('Country') ['Confirmed'].sum().nlargest(10).sort_values(ascending = False))

fig1 = px.scatter(top10_confirmed, x = top10_confirmed.index, y = 'Confirmed', size = 'Confirmed', size_max = 120, 
color = top10_confirmed.index, title = "Top 10 Countries by Confimred Cases")

fig1.write_html('Fig1.html', auto_open = True)

top10_deaths = pd.DataFrame(data.groupby('Country') ['Deaths'].sum().nlargest(10).sort_values(ascending = False))

fig2 = px.scatter(top10_deaths, x = top10_deaths.index, y = 'Deaths', size = 'Deaths', size_max = 120, 
color = top10_deaths.index, title = "Top 10 Countries by Death Cases")

fig2.write_html('Fig2.html', auto_open = True)

top10_recovered = pd.DataFrame(data.groupby('Country') ['Recovered'].sum().nlargest(10).sort_values(ascending = False))

fig3 = px.scatter(top10_recovered, x = top10_recovered.index, y = 'Recovered', size = 'Recovered', size_max = 120, 
color = top10_recovered.index, title = "Top 10 Countries by Recovered Cases")

fig3.write_html('Fig3.html', auto_open = True)

top10_active = pd.DataFrame(data.groupby('Country') ['Active'].sum().nlargest(10).sort_values(ascending = False))

fig4 = px.scatter(top10_active, x = top10_active.index, y = 'Active', size = 'Active', size_max = 120, 
color = top10_active.index, title = "Top 10 Countries by Active Cases")

fig4.write_html('Fig4.html', auto_open = True)

# Bar Graphs

top10_recovered = pd.DataFrame(data.groupby('Country') ['Recovered'].sum().nlargest(10).sort_values(ascending = False))

fig5 = px.bar(top10_recovered, x = 'Recovered', y = top10_recovered.index, height = 600, color = 'Recovered', orientation = 'h', 
color_continuous_scale = ['deepskyblue', 'red'], title = 'Top 10 Countries by Recovered Cases')

fig5.write_html('Fig5.html', auto_open = True)


top10_confirmed = pd.DataFrame(data.groupby('Country') ['Confirmed'].sum().nlargest(10).sort_values(ascending = False))

fig6 = px.bar(top10_confirmed, x = 'Confirmed', y = top10_confirmed.index, height = 600, color = 'Confirmed', orientation = 'h', 
color_continuous_scale = ['deepskyblue', 'red'], title = 'Top 10 Countries by Confirmed Cases')

fig6.write_html('Fig6.html', auto_open = True)


top10_deaths = pd.DataFrame(data.groupby('Country') ['Deaths'].sum().nlargest(10).sort_values(ascending = False))

fig7 = px.bar(top10_deaths, x = 'Deaths', y = top10_deaths.index, height = 600, color = 'Deaths', orientation = 'h', 
color_continuous_scale = ['deepskyblue', 'red'], title = 'Top 10 Countries by Death Cases')

fig7.write_html('Fig7.html', auto_open = True)


top10_active = pd.DataFrame(data.groupby('Country') ['Active'].sum().nlargest(10).sort_values(ascending = False))

fig8 = px.bar(top10_active, x = 'Active', y = top10_active.index, height = 600, color = 'Active', orientation = 'h', 
color_continuous_scale = ['deepskyblue', 'red'], title = 'Top 10 Countries by Active Cases')

fig8.write_html('Fig8.html', auto_open = True)