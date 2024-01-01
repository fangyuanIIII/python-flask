"""
使用apis
"""
from flask_restful import Resource, fields, marshal_with, reqparse
from com.lt.webdev.flask.flaskdbmodel.flaskdbassociation_ import *


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world get'}
    def post(self):
        return {'hello': 'world post'}

"""
marshal_with
字段格式化
"""
ret_field = {
    'status': fields.Integer,
    'message': fields.String,
    'message1': fields.String(default="aa"),  #带默认值
    'data': fields.String,
    'data2': fields.String(attribute='data1')  #使用json中data1的值
}
class User1(Resource):

    @marshal_with(ret_field)
    def get(self):
        return {'data': "ok",'data1':'data1111'}

#数据库字段全
ret_modelfields = {
    'id': fields.Integer,
    'name': fields.String
}
ret_field2 = {
    'status': fields.Integer,
    'message': fields.String,
    'message1': fields.String(default="aa"),  #带默认值
    'data': fields.Nested(ret_modelfields),  #显示数据库单个对象
    'datalist': fields.List(fields.Nested(ret_modelfields)) ,  #显示数据库单个对象
    'url': fields.Url(endpoint='u1'),
    'url2': fields.Url(endpoint='h1',absolute=True)  #绝对路径
}
class User2(Resource):


    @marshal_with(ret_field2)
    def get(self):
        ##数据模型查询
        users = User.query.all()
        movie1 = Movie.query.get(4)
        print(users[0].name)
        print(movie1.name)
        # return {'data':user,
        #         'datalist':users}
        return {'message': 'ok','data': movie1, 'datalist': users }

"""
参数格式化

"""
#response = requests.get('http://127.0.0.1:5000/users3',
                        # json={'name':"lisi"},
                        # headers={'content-type': 'application/json'})
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True,help="name参数是必须")
# response = requests.get('http://127.0.0.1:5000/users3',
#                         json={'name':"lisi","age":[22,33]},
#                         headers={'content-type': 'application/json'})
# 或者response = requests.get('http://127.0.0.1:5000/users3',
#                         json={'name':"lisi","age":22},
#                         headers={'content-type': 'application/json'})
parser.add_argument('age', type=int, action="append")  # action="append"   age参数可以有多个
# response = requests.get('http://127.0.0.1:5000/users3',
#                         json={'name':"lisi","age":[22,33]},
#                         headers={'content-type': 'application/json',
#                                  'Cookie': 'ck=7C98C109F3BCE8F8F30478678BC8F0ED'})
parser.add_argument('ck', type=str, location="cookies")  # 获取cookie内容

class User3(Resource):

    def get(self):
        # parser.parse_args()   参数格式话生效
        args = parser.parse_args()
        name = args.get('name')    #args['name']
        age = args.get('age')
        ck = args.get('ck')
        return {'name':name,'age':age,'ck':ck}