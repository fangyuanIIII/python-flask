import datetime

from flask import Flask
app = Flask(__name__)
#更改app的template 和static路径
# app = Flask(__name__,static_folder="",template_folder="")

#后台转入前台json数据时有中文，需要显示    并且使用jsonify显示可以配置
app.config["JSON_AS_ASCII"] = False
#使用wtforms需要配置SECRET_KEY
app.config["SECRET_KEY"] = "wtforms"
#设置session过期时间
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(days=8)

#当其他py文件需要使用路由需要先自己注册蓝图   然后在app.py  将蓝图注册到app    可以使用路由跳转页面
from com.lt.webdev.flask.echarts.echarts_ import bp as echartsbp
from com.lt.webdev.flask.base.base_ import bp as basebp
from com.lt.webdev.flask.base.customfunc_ import bp as customfuncbp
from com.lt.webdev.flask.base.wtforms_ import bp as wtformsbp
from com.lt.webdev.flask.flaskdbmodel.flaskdb_ import bp as flaskdbbp,initconfig
from com.lt.webdev.flask.flaskdbmodel.flaskdbassociation_ import bp as flaskdbassociation,initconfig
from com.lt.webdev.flask.cache.caching_ import bp as cachebp,init
from com.lt.webdev.flask.aop.aop_ import bp as aopbp
from com.lt.back_web_split.restful.restful_ import init as restfulinit
app.register_blueprint(echartsbp)
app.register_blueprint(basebp)
app.register_blueprint(customfuncbp)
app.register_blueprint(wtformsbp)
# app.register_blueprint(flaskdbbp)
# initconfig(app)
app.register_blueprint(flaskdbassociation)
initconfig(app)
app.register_blueprint(cachebp)
init(app)
app.register_blueprint(aopbp)
restfulinit(app)

#自定义类型转换器
from com.lt.webdev.flask.base.converter_ import regex
app.url_map.converters['regex'] = regex
@app.route("/converter/<regex('converter.{2}'):username>")
def user_info(username):
    return "hello %s" % username

#自定义函数
def step_(data :list)-> list:
    """
    跳过一个
    :param data:
    :return:
    """
    return data[::2]
#                       函数          在html中使用的名称
app.add_template_filter(step_,"step_")


if __name__ == '__main__':
    #app.run()
    app.debug = True
    # 开启debug=True  可以不重启就自动运行修改后的代码
    app.run(debug=True,host='192.168.1.6',port=5000)



