import random
from pyecharts import options as opts
from pyecharts.charts import Line

# 生成数据
x_data = list(range(1, 11))
y_data = [random.randint(1, 10) for _ in range(10)]

# 创建折线图对象
line_chart = (
    Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
        series_name="数据示例",
        y_axis=y_data,
        linestyle_opts=opts.LineStyleOpts(width=3),  # 设置线条宽度
        label_opts=opts.LabelOpts(is_show=False),  # 不显示标签
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="折线图示例"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),  # 设置鼠标悬停时的提示信息
        xaxis_opts=opts.AxisOpts(name="X 轴"),
        yaxis_opts=opts.AxisOpts(name="Y 轴"),
    )
)

# 生成 HTML 文件并在浏览器中打开
line_chart.render("pic/line_chart.html")
