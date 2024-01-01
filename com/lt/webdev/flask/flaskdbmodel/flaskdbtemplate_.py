"""
flask 数据库  数据模型
SQLAlchemy

安装数据库驱动
pip install flask-sqlalchemy  数据orm操作
pip install flask-migrate  数据迁移

需要在app.py配置配置
"""
# coding:utf-8
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

class Role(db.Model):
    """用户角色/身份表"""
    __tablename__ = "tbl_roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    #设置反向关系，额外为User添加一个role属性（反推属性）
    users = db.relationship("User", backref="role")

    def __repr__(self):
        """定义之后，可以让显示对象的时候更直观"""
        return "Role object: name=%s" % self.name

# 表名的常见规范
# ihome -> ih_user   数据库名缩写_表名
# tbl_user  tbl_表名
# 创建数据库模型类
"""
    常见列选项
    选项名                说明
    primiary_key        如果为True,代表表的主键
    unique              如果为True,代表这列不允许重复
    index               如果为True,为这列创建索引，提高查询效率
    nullable            如果为True,允许有空值，为False，不允许有空值
    default             为这列定义默认值
"""
class User(db.Model):
    """用户表"""
    __tablename__ = "tbl_users"  # 指明数据库的表名

    id = db.Column(db.Integer, primary_key=True)  # 整型的主键，会默认设置为自增主键
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_roles.id"))

    def __repr__(self):
        return "User object: name=%s" % self.name

if __name__ == '__main__':
    # 清除数据库里的所有数据--第一次创建会有脏数据
    db.drop_all()

    # 创建所有的表
    db.create_all()

    #【单条保存】
    # 创建对象
    role1 = Role(name="admin")
    # session记录对象任务
    db.session.add(role1)
    # 提交任务到数据库中
    db.session.commit()

    role2 = Role(name="stuff")
    db.session.add(role2)
    db.session.commit()

    #【多条保存】
    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=role1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=role2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=role2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=role1.id)

    # 一次保存多条数据
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()
    """删除数据"""
    user = User.query.get(3)
    db.session.delete(user)
    db.session.commit()

    """修改数据"""
    # 方法一：
    user = User.query.get(1)
    user.name = "python"
    db.session.add(user)
    db.session.commit()
    # 方法二:
    User.query.filter_by(name="zhou").update({"name": "python", "email": "itcast"})
    db.session.commit()

    """查询数据"""
    ###可以将单个数据当做对象来通过属性来提取数据
    # 例：查询多条数据并将第一条数据的name值取出
    li = Role.query.all()  # flask-sqlalchemy方法
    li2 = db.session.query(Role).all()  # 原始sqlalchemy方法
    r = li[0]
    temp_name = r.name

    # 查询数据库中单条数据，第一条数据
    r = Role.query.first()
    r2 = db.session.query(Role).first()
    temp_name = r.name

    # 通过主键值来获取单条数据
    r = Role.query.get(2)
    r2 = db.session.query(Role).get(2)
    temp_name = r.name

    ##############################################################3
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

    # 不加后面all等操作的时候为一个不会执行的查询
    # 查询不到会返回NoneType
    user1 = User.query.filter_by(name="wang").all()
    user2 = User.query.filter_by(name="wang", role_id=1).first()

    # filter为万能过滤器，filter_by为一个特殊的等值过滤器
    user1 = User.query.filter(User.name == "wang").all()
    user2 = User.query.filter(User.name == "wang", User.role_id == 1).first()

    # 引入或者,与,非参数
    from sqlalchemy import or_, and_, not_

    # 或操作
    user1 = User.query.filter(or_(User.name == "wang", User.email.endswith("163.com"))).all()
    temp_name = user1[0].name

    # 例：取User表中跳过两个数据后取前两个数据
    user = User.query.offset(2).limit(2).all()

    ##排序flask-sqlalchemy写法
    User.query.order_by("-id").all()
    ##排序flask官方写法,asc升序
    User.query.order_by(User.id.desc()).all()

    ##分组查询(需要的时候在查吧，看着好像也没啥用),前面为显示信息
    # 如果需要求和操作，from sqlalchemy import func中有好多功能，用的时候再查吧
    db.session.query(User.role_id).group_by(User.role_id)
    ####################################################################3
    ###关联查询
    # 从Role往User中查询
    ro = Role.query.get(1)
    user_name = ro.users[0].name
    # 从User往Role中查询
    user = User.query.get(1)
    role_name = user.role.name  # role为关系别名


