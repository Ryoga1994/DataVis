# plot related incidents network with location specified on map
# colored by attacktype /  weapon type

import plotly.plotly as py
from plotly.graph_objs import *
from plotly.offline import plot

import networkx as nx
import pandas as pd

import colorlover as cl

# load data
dt = pd.read_csv("TerrorismDATA_Real_1970_2016.csv",encoding = "ISO-8859-1", float_precision='high')

# variables

# read event id seperately
df = dt

lons = dt['longitude']
lats = dt['latitude']

multiple = dt['multiple']
related = dt['related']

attacktypes = dt['attacktype1_txt']
attacktypes1 =dt['attacktype1']

weaptypes = dt['weaptype1_txt']
weaptypes1 = dt['weaptype1']

gnames = dt['gname']
countries = dt['country_txt']

popups = ['Country: ' + ele[0] + '<br>Perpetrator Group Name: '+ ele[1] + '<br>Type of attack: '+ ele[2]
          for ele in zip(countries, gnames, attacktypes)]

dt['popup'] = popups

print(dt.columns)
print(dt.head())
print(len(dt))
#df.dropna(axis=0, how='any')

# create network data
# events = node
# edge = multiple

# network vis
edge_trace = Scatter(
    x=[],
    y=[],
    line=Line(width=1,color='grey'),
    hoverinfo='none',
    mode='lines')

color_pal = cl.scales['11']['qual']['Paired']
cols = [color_pal[int(ele)]for ele in attacktypes1]

node_trace = Scatter(
    x=[],
    y=[],
    text=[],
    mode='markers',
    hoverinfo='text',
    marker=Marker(
        showscale=False,
        # colorscale options
        # 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' |
        # Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
        #colorscale='YIGnBu',
        reversescale=True,
        color=[],
        size=3,
        colorbar=dict(
            thickness=15,
            title='Incidents Affiliation Network',
            xanchor='left',
            titleside='right'
        ),
        #line=dict(width=2)
        ))

node_pos = {}

# event positions
# for i in range(len(dt)):
#     #node_trace['x'].append(df.ix[i, 'Lon'])
#     #node_trace['y'].append(df.ix[i, 'Lat'])
#     #node_trace['marker']['color'].append(int(df.ix[i, 'weaptype1']))
#     node_pos[dt.ix[i,'eventid']] = (dt.ix[i, 'longitude'], dt.ix[i, 'latitude'])
#

# create node with only series events
df = dt
nodelist = []
for i in range(1,len(dt)):
    #node0 = df.ix[i, 'eventid']
    if not pd.isnull(df.ix[i, 'related']):
        # print(df.ix[i, 'related'])
        if(df.ix[i-1,'related']==df.ix[i, 'related']):
            x0, y0 = df.ix[i-1, 'longitude'], df.ix[i-1, 'latitude']
            x1, y1 = df.ix[i, 'longitude'], df.ix[i, 'latitude']

            # edge list
            edge_trace['x'] += [x0, x1, None]
            edge_trace['y'] += [y0, y1, None]

            # node list
            node_trace['x'].append(x0)
            node_trace['y'].append(y0)
            node_trace['marker']['color'].append(int(df.ix[i-1, 'attacktype1']))
            node_trace['text'].append(df.ix[i-1, 'popup'])

            node_trace['x'].append(x1)
            node_trace['y'].append(y1)
            node_trace['marker']['color'].append(int(df.ix[i, 'attacktype1']))
            node_trace['text'].append(df.ix[i, 'popup'])

#
# for node in nodelist:
#     node_trace['x'].append(node_pos[node][0])
#     node_trace['y'].append(node_pos[node][1])

print(node_trace['x'][:5])
print(edge_trace['x'][:5])

# vis
fig = Figure(data=Data([edge_trace, node_trace]),
             layout=Layout(
                title='<br><b>Incidents Affiliation Network</b>',
                titlefont=dict(size=16),
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.001, align='left' ) ],
                xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))

plot(fig, filename='plotly_related_incidents_network_by_loc.html')








