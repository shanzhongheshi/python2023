import requests
import time
from pyecharts import options as opts
from pyecharts.charts import Line

# 创建折线图对象
line_chart = Line()

# 设置全局配置项
line_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="动态折线图示例"),
    tooltip_opts=opts.TooltipOpts(trigger="axis"),  # 设置鼠标悬停时的提示信息
    xaxis_opts=opts.AxisOpts(name="X 轴"),
    yaxis_opts=opts.AxisOpts(name="Y 轴"),
)

# 定义更新数据的函数
def update_data():
    # 调用接口获取数据
    response = requests.get('https://api.example.com/data')  # 替换为实际的接口地址
    data = response.json()

    # 解析数据
    x_data = []
    y_data = []
    for item in data:
        x_data.append(item['x'])
        y_data.append(item['y'])

    # 清空折线图数据
    line_chart.clear()

    # 添加新数据到折线图
    line_chart.add_xaxis(xaxis_data=x_data)
    line_chart.add_yaxis(
        series_name="数据示例",
        y_axis=y_data,
        linestyle_opts=opts.LineStyleOpts(width=3),  # 设置线条宽度
        label_opts=opts.LabelOpts(is_show=False),  # 不显示标签
    )

    # 渲染图表
    line_chart.render("dynamic_line_chart.html")

# 循环调用更新数据的函数
while True:
    update_data()

    # 暂停5秒钟
    time.sleep(5)
