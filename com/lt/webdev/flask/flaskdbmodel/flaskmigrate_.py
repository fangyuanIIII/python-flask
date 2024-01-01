"""
flask 数据库  数据模型
SQLAlchemy
可以管理数据表结构生成数据库迁移的扩展工具。当Model出现变更的时候，通过migrate去管理数据库变更。


1.安装数据库驱动
2.pip install flask-sqlalchemy  数据orm操作
3.pip install flask-migrate  数据迁移
4.在当前工程的terminal执行命令  并且migrate需要在app.py执行（app.py在项目工程的第一级子目录）
flask db --help 帮助命令
初始化时(第一次需要)
flask db init   #生成迁移文件夹migeations   会在 项目工程的第一级子目录生成

#将模型刷进去
flask db migrate  #生成数据迁移文件   并且在数据库创建表ALEMBIC_VERSION(数据为空)

升级时 将刷进的模型创建表  并且增加版本号   一般配合flask db migrate使用
如果 使用了db.drop_all()会删除全部表
flask db upgrade

降级时 看是否有模型更改的迁移文件，没有就执行flask db migrate生成更改后的迁移文件
flask db downgrade


#1初始化生成表
flask db init
flask db migrate
flask db upgrade

#2.升级就是模型属性改变
flask db migrate   #当执行这个会将数据库所有表预删除
flask db upgrade   #会将预删除的表删除

#3.降级就是模型属性改变
flask db migrate
flask db downgrade
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

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
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app=app)
migrate = Migrate(app=app,db=db)

#当数据存在该表时 ，不会覆盖原有的   会按照传参名称对应数据字段名称
class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.String(100), primary_key = True)#db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100))
    code = db.Column(db.String(100))
    count = db.Column(db.Float)

if __name__ == '__main__':
    app.run(debug=True)

    #没有明白什么时候生效
    # db.drop_all()
    # db.create_all()