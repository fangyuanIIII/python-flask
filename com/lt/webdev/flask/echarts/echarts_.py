"""
pyecharts统计图
pip install pyecharts
"""
from pyecharts import charts
from flask import Blueprint,render_template

# url_prefix:127.0.0.1:5000/a/c
bp = Blueprint("echarts", __name__, url_prefix="/echarts")

@bp.route('/chart')
def index():
    line = charts.Line()
    line.add_xaxis(["asd", "aaa", "a"])
    line.add_yaxis("test", [6, 7])
    line.render(path="render.html")
    # 将柱状图转换为HTML格式的代码
    line_html = line.render_embed()
    return render_template("com/lt/echarts/render.html",line_html = line_html)
