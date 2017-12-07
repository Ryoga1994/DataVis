# plot related incidents network with location specified on map
import plotly.plotly as py
from plotly.graph_objs import *
from plotly.offline import plot

import networkx as nx
import pandas as pd

import colorlover as cl

# load data
df = pd.read_csv("TerrorismDATA_Real_1970_2016.csv",encoding = "ISO-8859-1")
df = df[['eventid','longitude','latitude','success','related']]

print(list(df.columns))
print(df.head())

#df = df.dropna(axis=0, how='any')
print(len(df))
# print(df['success'])

# create network data
# events = node
# edge = multiple

# network vis
edge_trace = Scatter(
    x=[],
    y=[],
    line=Line(width=0.5,color='#888'),
    hoverinfo='none',
    mode='lines')

#print(cl.scales['11'].keys())
color_pal = (cl.scales['12']['qual']['Paired'][1],cl.scales['12']['qual']['Paired'][5])
print(color_pal)

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
        #colorscale=color_pal,
        reversescale=True,
        color=[],
        size=0.5,
        opacity= 0.5,
        # colorbar=dict(
        #     thickness=15,
        #     title='Incidents Affiliation Network',
        #     xanchor='left',
        #     titleside='right',

        # ),
        line=dict(width=2)))

node_pos = {}



# node
for i in range(len(df)):
    node_trace['x'].append(df.ix[i, 'longitude'])
    node_trace['y'].append(df.ix[i, 'latitude'])
    node_trace['marker']['color'].append(color_pal[df.ix[i, 'success']])

    node_pos[df.ix[i,'eventid']] = (df.ix[i, 'longitude'], df.ix[i, 'latitude'])

#print(node_trace['marker']['color'])

for i in range(len(df)):
    node0 = df.ix[i, 'eventid']

    if not pd.isnull(df.ix[i, 'related']):
        neighbors = df.ix[i, 'related'].split(",")
        for n in neighbors:
            if n not in node_pos.keys():
                continue
            x0, y0 = node_pos[node0]
            x1, y1 = node_pos[n]

            edge_trace['x'] += [x0, x1, None]
            edge_trace['y'] += [y0, y1, None]

# vis
fig = Figure(data=Data([edge_trace, node_trace]),
             layout=Layout(
                title='<br><b>World Terrorism Map</b>',
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

plot(fig, filename='plotly_world_terrorism_map.html')