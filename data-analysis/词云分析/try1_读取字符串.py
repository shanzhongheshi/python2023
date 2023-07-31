import jieba
from wordcloud import WordCloud
txt = '弱小的人,才习惯,嘲讽和否定，而内心,强大的人,从不吝啬赞美和鼓励！我们就是后浪，奔涌吧！后浪，奔涌吧！'
words = jieba.lcut(txt)     #精确分词
newtxt = ''.join(words)    #空格拼接
wordcloud=WordCloud(font_path =  "C:/Windows/Fonts/simfang.ttf").generate(newtxt)
wordcloud.to_file('tmp/try1.jpg')

