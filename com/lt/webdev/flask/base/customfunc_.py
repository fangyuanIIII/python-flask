"""
注册自定义函数需要在app.py中
定义一个函数
1.def step(data :list)-> list:
    return data[::2]
2.app.add_template_filter(step_,"step_")  添加过滤器
"""
from flask import Blueprint,render_template

bp = Blueprint("customfunc_",__name__,url_prefix="/")

@bp.route("/customfunc_")
def customfunc_():
    return render_template("com/lt/customfunc/func.html",list = [1,2,3,4,5,6,7])
