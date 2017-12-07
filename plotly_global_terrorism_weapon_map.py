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
weaptypes1 = dt['weaptype1']
weaptypes = dt['weaptype1_txt']
gnames = dt['gname']
countries = dt['country_txt']

print(countries[:2],gnames[:3],weaptypes[:2])

popups = ['Country: ' + ele[0] + '<br>Perpetrator Group Name: '+ ele[1] + '<br>Type of Weapon: '+ ele[2]
          for ele in zip(countries, gnames, weaptypes)]

print(attacktypes[:5])
print(weaptypes[:5])

color_pal = cl.scales['11']['qual']['Paired']
color_pal = color_pal.append(cl.scales['11']['qual']['Set3'])

# visualization
cities = [ dict(
    type='scattergeo',
    lon=lons,
    lat=lats,
    text=popups,
    mode='markers',
    marker=dict(
        color= weaptypes1
    ))]

layout = dict(
        title = '<br><b>Global Terrorism Weapon Map</b>',
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
plotly.offline.plot(fig, filename='plotly_global_terrorism_weapon_map.html')