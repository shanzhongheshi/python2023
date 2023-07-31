import random
import time
from pyecharts import options as opts
from pyecharts.charts import Animao

# 创建折线图对象
line_chart = AnimationLine()

# 设置全局配置项
line_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="动态折线图示例"),
    tooltip_opts=opts.TooltipOpts(trigger="axis"),  # 设置鼠标悬停时的提示信息
    xaxis_opts=opts.AxisOpts(name="X 轴"),
    yaxis_opts=opts.AxisOpts(name="Y 轴"),
)

# 生成初始数据
x_data = list(range(1, 11))
y_data = [random.randint(1, 10) for _ in range(10)]

# 添加初始数据到折线图
line_chart.add_xaxis(xaxis_data=x_data)
line_chart.add_yaxis(series_name="数据示例", y_axis=y_data)

# 模拟数据更新
for _ in range(10):
    # 生成新的数据
    y_data = [random.randint(1, 10) for _ in range(10)]

    # 更新折线图数据
    line_chart.add_yaxis(series_name="数据示例", y_axis=y_data)

    # 渲染图表
    line_chart.render("dynamic_line_chart.html")

    # 暂停一段时间，模拟数据的动态变化
    time.sleep(1)
