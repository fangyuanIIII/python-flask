"""
flask四大内置对象
request
session
g   #全局对象保存用户数据
current_app  #app配置信息


当flask 不在与html的根路径templates同一目录级别时需要加Blueprint
Blueprint蓝图是一种组织项目中文件或代码的方式
蓝图方式是把先它们注册到蓝图，然后在工厂函数中把蓝图注册到app。进而实现了路由分发、静态文件的管理等功能。减少了代码之间的耦合。

redirect重定向路由    重定向页面或者链接

json数据传入前端方法
1.make_response返回response  配合 json
2.直接使用jsonify

异常：
1.raise是主动抛出异常
2.abort是自定义抛出异常
"""
from flask import (Blueprint,
                   render_template,redirect,make_response,
                   json,jsonify,
                   abort,
                   Response,url_for,
                   request,session,g,current_app)

#蓝图将路由注册到蓝图
bp = Blueprint("base_",__name__,url_prefix='/')

@bp.before_request
def fourclass():
    g.star = "张三"

@bp.route("/four")
def getfourclass():
    print(g.star)

    print(current_app,current_app.config)
    return "ok"


#http://127.0.0.1:5000/html?page=
#page传参
@bp.route('/request_')
def request_():  # put application's code here
    # request.args
    # request.form
    # request.cookies
    # request.path  #/html/
    # request.url  #http://127.0.0.1:5000/html?page=
    # request.base_url  #http://127.0.0.1:5000/html/
    # request.host_url  #http://127.0.0.1:5000/
    # request.files  #文件内容
    # request.headers  #请求头
    # request.user_agent  # 用户代理，包括游览器和操作系统信息时   识别是否是爬虫

    params = request.args.get("page",default=1,type=int)
    return render_template("html.html" ,args = params)

@bp.route('/response_')
def response_():  # put application's code here
    #返回字符串
    return ""
    #返回页面啊
    # return render_template("")

    #前后端分离
    #返回 json
    # return  jsonify()
    # return make_response(json.dumps())
    #
    # res = make_response(render_template("html.html"))
    # 或者
    # res = Response(render_template("html.html"))






#http://127.0.0.1:5000/html/*
#路径传参
@bp.route('/html1/<args>')
def html1(args):  # put application's code here
    return render_template("html.html",args = args)

@bp.route('/template_')
def template_():  # put application's code here
    return render_template("com/lt/template/base_child.html")

@bp.route('/')
def hello_worlds():  # put application's code here
    return 'Hello World!'

#跳转方式 get  post
@bp.route('/get',methods=['GET'])
def get_():  # put application's code here
    return 'get'
@bp.route('/post',methods=['POST'])
def post_():  # put application's code here
    return 'post'

@bp.route('/getpost',methods=['GET','POST'],endpoint='getpost')
def post_():  # put application's code here
    return 'post'

#跳转页面
@bp.route('/index')
def hello_world():  # put application's code here
    return render_template("com/lt/index.html")

@bp.route('/html2/<int:args>')
def html2(args):  # put application's code here
    return render_template("html.html",args = args)

@bp.route('/form',methods=['GET','POST'])
def form():  # put application's code here
    if request.method == 'POST':
        name = request.form['name']
        password = request.form.get('password')
        return f"{name}%%%{password}"

    elif request.method == 'GET':
        return render_template("com/lt/base/form.html")







#重定向页面或者链接
@bp.route('/redirect_')
def redirect_():  # put application's code here
    # return redirect("https://www.baidu.com")
    #              url_for("蓝图name.函数名")实现跳转
    #              url_for("蓝图name.函数名",name=1)传参
    # ret = url_for("base_.hello_worlds")
    # return redirect(ret)
    return redirect("/")


@bp.route('/data_')
def data_():
    return render_template("com/lt/base/data.html",data = [{"a":1,"b":"s"},2,"a"])


@bp.route('/json_')
def json_():
    response =  make_response(json.dumps([{"a":1,"b":"s"},2,"a"],ensure_ascii=False))
    response.mimetype = "application/json"
    return response


@bp.route('/jsonify_')
def jsonify_():
    # jsonify([{"a": 1, "b": "s"}, 2, "a"])  可以配合app.config["JSON_AS_ASCII"] = False  显示中文
    return jsonify(json.dumps([{"a":1,"b":"s"},2,"a"],ensure_ascii=False))

@bp.route('/abort_')
def abort_():
    return abort(405)

#配合abort使用   返回后续文字
#err 必须绑定一个参数
@bp.errorhandler(405)
def abort_handle(err):
    # return "出现错误，需要改正"
    # return render_template("com/lt/base/form.html")
    return redirect("/")

#cookie
@bp.route("/cookie_")
def cookie_():

    #登录成功存储cookie 跳转页面
    if True:
        response = redirect("/form")
        # response.set_cookie("user","信息")
        #持久化
        #在app.py设置session过期时间
        # #app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(days=8)
        session.permanent = True
        session["name"] = ""
        session.get("name",default="")
        element = session.pop("name")
        session.clear()
        return response
