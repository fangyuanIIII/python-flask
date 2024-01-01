"""
面向切面
又叫钩子函数
"""
from flask import Blueprint
bp = Blueprint('aop', __name__,url_prefix='/aop')

@bp.route('/hello')
def hello_world():
    print('hello_world')
    return 'hello world'

#钩子函数也加中间件
@bp.before_request
def index():
    print('before_request')

    #不要  return  会终止当前aop路由地址的函数方法执行
    # return 'ok'    return后  后面的代码不执行 打印不出hello函数的print('hello_world')