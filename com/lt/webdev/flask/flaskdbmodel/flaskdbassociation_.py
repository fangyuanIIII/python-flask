"""
表关联查询
一对多
多对多 （有中间表）
flask db init
flask db migrate
flask db upgrade
"""
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

bp = Blueprint('flaskassociationdb',__name__,url_prefix='/flaskassociation')

db = SQLAlchemy()
migrate = Migrate();
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
    migrate.init_app(app=app, db=db)

"""
1.一对多 
"""
# class Person(db.Model):
#     __tablename__ = 'person'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#
#     #只有man表才能查到  backref='person'  person字段
#     #mans = db.relationship("man", backref='person', lazy='dynamic')
#     mans = db.relationship("Man", backref='person', lazy=True)
#
# class Man(db.Model):
#     __tablename__ = 'man'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     #外键  gradeid = db.Column(db.Integer, db.ForeignKey('peson.id'))
#     gradeid = db.Column(db.Integer, db.ForeignKey(Person.id))

"""
2.多对多
"""
collect = db.Table(
    'collects',
    db.Column('user_id', db.Integer,db.ForeignKey("user.id"), primary_key=True),
    db.Column('movie_id', db.Integer,db.ForeignKey("movie.id"), primary_key=True))

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    #secondary 设置中间表
    users = db.relationship("User",backref='movie', lazy='dynamic',secondary=collect)


@bp.route('/queryall')
def query_():
    #一对多查询
    # man = Man.query.all() #list列表  list[man{id,name},man]
    #
    # for key in man:
    #         print(key.name,key.person.name)
    #
    #
    # person = Person.query.all()



    #多对多
    users = User.query.all()
    movie1 = Movie.query.get(4)
    print(users[0].name)
    print(movie1.name)
    users[0].movie.append(movie1)
    db.session.commit()
    return "ok"

