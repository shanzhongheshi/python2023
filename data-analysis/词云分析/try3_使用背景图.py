from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
mask = np.array(Image.open("tmp/Alice.png"))


f = open('tmp/Alice.txt','r',encoding = 'utf-8')
txt = f.read()
f.close
wordcloud = WordCloud(
                      background_color="white", \
                      width = 800, \
                      height = 600, \
                      max_words = 200, \
                      max_font_size = 80, \
                      mask = mask, \
                      contour_width = 3, \
                      contour_color = 'steelblue'
                      ).generate(txt)
wordcloud.to_file('tmp/try3.png')
