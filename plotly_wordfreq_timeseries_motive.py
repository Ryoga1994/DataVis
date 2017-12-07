# word freq time series

import pandas as pd
import nltk
import plotly.graph_objs as go

from nltk.corpus import stopwords
from plotly.offline import plot

from nltk.tokenize import RegexpTokenizer

# load and clean data
dt = pd.read_csv("TerrorismDATA_Real_1970_2016.csv",encoding = "ISO-8859-1")

# count word frequency by year

tokenizer = RegexpTokenizer(r'\w+')

dt_year_tokens = [(year,tokenizer.tokenize(ele)) for year,ele in zip(dt['iyear'],dt['motive']) if not pd.isnull(ele) and not ele in stopwords.words('english')]
#print(dt_year_tokens[:5])

# find top 5 key words
cfd = nltk.FreqDist(word
					for doc in dt_year_tokens
                    for word in doc[1])
#print(cfd.most_common()[:50])

keywords = ['responsibility','attack', 'incident', 'targeted','violence','Iraq']

cfd = nltk.ConditionalFreqDist((doc[0], word)
                               for doc in dt_year_tokens
                               for word in doc[1]
                               if word in keywords)

years = sorted(cfd.keys())

# create trace for each keywords
data = []
for word in keywords:
	x = []
	y = []

	for year in years:
		x.append(year)
		y.append(cfd[year][word])

	new_trace = go.Scatter(
		x = x,
		y = y,
		mode = 'lines+markers',
		name = word
		)
	data.append(new_trace)


layout = dict(title = 'Timeseries - Motive\'s keywords frequency',
              xaxis = dict(title = 'Year'),
              yaxis = dict(title = 'Frequency'),
              )

fig = dict(data=data, layout=layout)
plot(fig, filename="plotly_wordfreq_timeseries_motive.html")



