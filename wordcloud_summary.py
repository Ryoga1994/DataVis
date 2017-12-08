# word cloud of events summary

from wordcloud import WordCloud, STOPWORDS
import pandas as pd 
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# load and clean data

dt = pd.read_csv("TerrorismDATA_Real_1970_2016.csv",encoding = "ISO-8859-1")
dt['summary']

#print(pd.isnull(dt['summary'][0]))

# remove punctuation
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
dt_tokens = [" ".join(tokenizer.tokenize(ele)) for ele in dt['summary'] if not pd.isnull(ele)]
print(dt_tokens[:5])

#word_mask = np.array(Image.open('love.png'))

text = " ".join(dt_tokens)

# wordcloud
stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, # mask=word_mask,
               stopwords=stopwords)

wc.generate(text)

# save / show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
#plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
#plt.savefig('wordcloud_summary.jpg')

