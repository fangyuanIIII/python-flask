"""
flask  orm数据库
只能操作已有的数据库表
1.安装数据库驱动
2.pip install flask-sqlalchemy  安装数据orm操作
"""

###查询过滤器（符合条件取出）
"""
过滤器 说明
filter()    把过滤器添加到原查询上，返回一个新查询
filter_by() 把等值过滤器添加到原查询上，返回一个新查询
limit   使用指定的值限定原查询返回的结果
offset()    偏移原查询返回的结果，返回一个新查询
order_by()  根据指定条件对原查询结果进行排序，返回一个新查询
group_by()  根据指定条件对原查询结果进行分组，返回一个新查询

all()   以列表形式返回查询的所有结果
first() 返回查询的第一个结果，如果未查到，返回None
first_or_404()  返回查询的第一个结果，如果未查到，返回404
get()   返回指定主键对应的行，如不存在，返回None
get_or_404()    返回指定主键对应的行，如不存在，返回404
count() 返回查询结果的数量
paginate()  返回一个Paginate对象，它包含指定范围内的结果
"""

from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, and_, not_

bp = Blueprint('flaskdb',__name__,url_prefix='/flask')

db = SQLAlchemy()
def initconfig(app ):
    #1.配置参数
    # class Config(object):
    #     """配置参数"""
    #     # sqlalchemy的配置参数
    #     # SQLALCHEMY_DATABASE_URI = "mysql://root:199596@127.0.0.1:3306/db_python"
    #     SQLALCHEMY_DATABASE_URI = "oracle://dev:123456@localhost:1521/orcl"
    #
    #     # 设置sqlalchemy自动更跟踪数据库
    #     SQLALCHEMY_TRACK_MODIFICATIONS = True
    #
    # app.config.from_object(Config)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://dev:123456@localhost:1521/orcl'
    #如果设置为True，Flask-SQLAlchemy将跟踪对象的修改并发出信号。
    #默认设置为None，启用跟踪，但会发出警告，默认情况下将来会被禁用。
    #这需要额外的内存，如果不需要应该禁用
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 2.创建数据库sqlalchemy工具对象
    db.init_app(app = app)

"""
db.Integer	整数
db.String(size)	字符串 size 为字符串长度
db.DateTime	日期时间
db.Date	日期
db.Text	长文本，可以存放 CLOB (二进制数据)
db.Float	浮点数字
db.Boolean	布尔值
"""
"""
常用字段选项
primary_key	设置表的主键，默认自增
unique	设置唯一索引
nullable	非空约束
default	设置默认值
index	创建索引
"""
#当数据存在该表时 ，不会覆盖原有的   会按照传参名称对应数据字段名称
class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.String(100), primary_key = True)#db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100))
    code = db.Column(db.String(100))
    count = db.Column(db.Float)

    #重写方法
    def __repr__(self):
        return self.name#f'id{self.id}, name{self.name}, code{self.code}'



@bp.route("/add")
def add():
    test = Test(id="2", name="1", code="1", count=1.0)
    try:
        # session记录对象任务
        db.session.add(test)
        # 提交任务到数据库中
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        db.session.flush()
    return "ok"

@bp.route("/addall")
def add_all_():
    test = Test(id="3", name="1", code="1", count=1.0)
    test1 = Test(id="4", name="1", code="1", count=1.0)
    test2 = Test(id="5", name="1", code="1", count=1.0)
    test3 = Test(id="6", name="1", code="1", count=1.0)
    try:
        db.session.add_all([test,test1, test2, test3])
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        db.session.flush()
    return "ok"

@bp.route("/update")
def update():

    #只能针对查询的记录修改   不能对test = Test(id="3", name="1", code="1", count=1.0)这个修改
    test = Test.query.get(1)
    print(type(test))
    test.name = "2"

    try:
        # db.session.add(test)
        # db.session.commit()

        #方式二
        #或者Test.query.filter(id = "3").update({"name":"2","code":"2"})
        Test.query.filter(Test.id == "4").update({"code":"2"})
        Test.query.filter_by(name = "2").update({"code":"10"})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        db.session.flush()
    return "ok"

@bp.route("/del")
def delete():
    test = Test.query.get(1)
    try:
        db.session.delete(test)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        db.session.flush()
    return "ok"

@bp.route("/queryall")
def queryall():
    try:
        test = Test.query.all()  # flask-sqlalchemy方法
        test2 = db.session.query(Test).all()  # 原始sqlalchemy方法
        test3 = Test.query.filter_by(name="3").all()
        test4 = Test.query.filter(Test.name == "1").all()
        test5 = Test.query.filter(Test.name == "1", Test.code == "1").first()

        #### 引入或者,与,非参数
        # from sqlalchemy import or_, and_, not_
        # 或操作
        test6_1 = Test.query.filter(or_(Test.name.__lt__("25"), Test.code.endswith("1"))).all()
        test6 = Test.query.filter(or_(Test.name == "1", Test.code.endswith("1"))).all()

        # 例：取User表中跳过两个数据后取前两个数据  会取list[0,1,2,3,4,5,6,7...]  offset跳过2个从 list[2]开始
        # limit限制2个  所以得到  [2,3]
        test7 = Test.query.offset(2).limit(2).all()
        # ##排序flask-sqlalchemy写法
        test8 = Test.query.order_by("id").all()
        ##排序flask官方写法,asc升序
        test9 = Test.query.order_by(Test.id.desc()).all()

        ##分组查询(需要的时候在查吧，看着好像也没啥用),前面为显示信息
        # 如果需要求和操作，from sqlalchemy import func中有好多功能，用的时候再查吧
        #     SELECT test.id AS test_id
        # FROM test GROUP BY test.id                必须主键或者外键
        test10 = db.session.query(Test.id).group_by(Test.id).all()
        test11 = Test.query.paginate(page= 2, per_page= 2, error_out=False).items


        print(test)
        print(test2)
        print(test3)
        print(test4)
        print(test5)
        print(test6)
        print(test7)
        print(test8)
        print(test9)
        print(test10)
        print(test11)
    except Exception as e:
        db.session.rollback()
        db.session.flush()
    return "ok"


