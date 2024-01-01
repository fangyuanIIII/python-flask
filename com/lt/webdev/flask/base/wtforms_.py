"""
Flask-WTF
定义表单模型
能快速定义表单模板；
验证表单数据；
全局的csrf保护，能够保护所有表单免受跨站请求伪造(CSRF)的攻击；
与 Flask-Uploads 一起支持文件上传；
国际化集成。
pip install flask-wtf
"""
from flask import Flask,Blueprint,render_template,request
bp = Blueprint("formmodule",__name__,url_prefix="/")


from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField
from wtforms.validators import DataRequired,EqualTo  #验证不能为空，验证是否相等

def initappconfig(app :Flask):
    """
    初始化表格
    :param app:
    :return:
    """
    # 使用wtforms需要配置SECRET_KEY
    app.config["SECRET_KEY"] = "wtforms"

class Form(FlaskForm):
    username = StringField('账号',validators=[DataRequired("账号不能为空")])
    password = PasswordField('密码',validators=[DataRequired("密码不能为空")])
    password2 = PasswordField('确认密码',validators=[DataRequired("密码不能为空"),EqualTo('password')])
    submit = SubmitField('提交')

@bp.route('/wtforms_', methods=['GET','POST'])
def wtforms_():
    form = Form()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            return f"{username}%%%{password}"
        else:
            return f"打印错误"

    elif request.method == 'GET':

        return render_template("com/lt/wtforms/form.html",form = form)