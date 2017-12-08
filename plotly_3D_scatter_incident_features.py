# 3D scatter plot

# data
import plotly
import plotly.graph_objs as go
from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, plot
import pandas as pd
import colorlover as cl


# load data
dt = pd.read_csv("TerrorismDATA_Real_1970_2016.csv",encoding = "ISO-8859-1")

lons = dt['longitude']
lats = dt['latitude']

attacktypes = dt['attacktype1_txt']
attacktypes1 =dt['attacktype1']

weaptypes1 = dt['weaptype1']
weaptypes = dt['weaptype1_txt']

gnames = dt['gname']
countries = dt['country_txt']

targtype = dt['targtype1_txt']
targtype1 = dt['targtype1']

success = dt['success']

popups = ['Country: ' + ele[0] +
          '<br>Perpetrator Group Name: '+ ele[1] +
          '<br>Type of attack: '+ ele[2] +
          '<br>Type of weapon: ' + ele[3]
          for ele in zip(countries, gnames, attacktypes, weaptypes)]

# 3D Scatterplot

color_pal = cl.scales['11']['qual']['Paired']
color_pal = [color_pal[0], color_pal[3]]

cols = [color_pal[int(ele)] for ele in success]


trace1 = go.Scatter3d(
    x=attacktypes,
    y=weaptypes,
    z=targtype,
    mode="markers",
    marker=dict(
        size=5,
        color=cols,
        opacity=0.8),
    text=popups,

)

data = [trace1]

annos = "To see whether the attack type / weapon type / target type could be significant influential factors on incident's success"

layout = go.Layout(
	title= '<br><b>Influential Factors on Incidence Success</b>',
    titlefont=dict(size=16),
    hovermode='closest',
	scene = dict(
        xaxis = dict(
             showgrid=False,
             zeroline=False,
             showticklabels=False,
             title="Attack Type"),
        yaxis = dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            title = "Weapon Type"),
        zaxis = dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            title="Target Type"),),
    annotations=[dict(
        text="",
        showarrow=False,
        xref="paper", yref="paper",
        x=0.005, y=-0.001, align='left')],

)

fig = Figure(data=Data(data),
             layout=layout)

plot(fig, filename='plotly_3D_scatter_incident_features.html')

