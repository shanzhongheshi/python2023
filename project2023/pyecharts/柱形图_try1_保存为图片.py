from pyecharts.charts import Line
from snapshot_selenium import snapshot
from pyecharts.render import make_snapshot

line = Line()
line.add_xaxis(["7/1", "7/2", "7/3", "7/4", "7/5", "7/6"])
line.add_yaxis("BUGS", [5, 20, 36, 10, 75, 90])

if __name__ == "__main__":
    #可以指定图片存放路径，格式
    make_snapshot(snapshot, line.render(), "imgs/chart.jpeg")