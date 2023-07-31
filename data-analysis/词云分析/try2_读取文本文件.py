import jieba
from wordcloud import WordCloud
with open("tmp/baixin.txt", encoding="utf-8") as file:
    # 数据文件
    txt = file.read()
    #结巴分词为是list类型
    words = jieba.lcut(txt)     #精确分词
    #将list类型拼接成string类型
    newtxt = ''.join(words)    #空格拼接
    print(type(words))
    # 如果数据文件中包含的有中文的话，font_path必须指定字体，否则中文会乱码
    # collocations：是否包括两个词的搭配，默认为True，如果为true的时候会有
    # 重复的数据，这里我不需要重复数据，所以设置为False
    # width 幕布的宽度，height 幕布的高度
    # max_words 要显示的词的最大个数
    # generate 读取文本文件
    wordcloud = WordCloud(font_path="C:/Windows/Fonts/simfang.ttf",
                          collocations=False,
                          background_color="black",
                          width=800,
                          height=600,
                          max_words=100).generate(newtxt) #这里需要String类型或者byte类型
    # 生成图片
    image = wordcloud.to_image()
    # 展示图片
    image.show()
    # 写入文件
    wordcloud.to_file("tmp/baixin.jpg")