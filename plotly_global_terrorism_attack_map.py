import plotly
import plotly.graph_objs as go
import pandas as pd 
import colorlover as cl

# load data
dt = pd.read_csv("TerrorismDATA_Real_1970_2016.csv",encoding = "ISO-8859-1")

lons = dt['longitude']
lats = dt['latitude']

attacktypes = dt['attacktype1_txt']
attacktypes1 =dt['attacktype1']

weaptypes = dt['weaptype1_txt']
gnames = dt['gname']
countries = dt['country_txt']

popups = ['Country: ' + ele[0] + '<br>Perpetrator Group Name: '+ ele[1] + '<br>Type of attack: '+ ele[2]
          for ele in zip(countries, gnames, attacktypes)]

color_pal = cl.scales['11']['qual']['Paired']

cols = [color_pal[int(ele)]for ele in attacktypes1]

# visualization
cities = [ dict(
    type='scattergeo',
    lon=lons,
    lat=lats,
    text=popups,
    mode='markers',
    marker=dict(
        color= cols
    ))]

layout = dict(
        title = '<br><b>Global Terrorism Attack Map</b>',
        showlegend = False,
        geo = dict(
            scope='world',
            #projection=dict( type='albers world' ),
            showland = True,
            landcolor = 'rgb(217, 217, 217)',
            subunitwidth=1,
            countrywidth=1,
            subunitcolor="rgb(255, 255, 255)",
            countrycolor="rgb(255, 255, 255)"
        )
    )

fig = go.Figure(data=cities, layout=layout)
plotly.offline.plot(fig, filename='plotly_global_terrorism_attack_map.html')