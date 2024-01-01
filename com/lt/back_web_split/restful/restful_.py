"""
restfull   前后端分离

前端返回页面
html json访问数据

pip install flask-restful
"""

from flask_restful import Api
from .apis import *

api = Api()
def init(app):
    api.init_app(app=app)

api.add_resource(HelloWorld,"/hello",endpoint="h1")
api.add_resource(User1,"/users",endpoint="u1")
api.add_resource(User2,"/users2")
api.add_resource(User3,"/users3")
