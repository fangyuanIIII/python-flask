"""
自定义转换器
"""
from werkzeug.routing import BaseConverter
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        # 正则参数
        self.regex = args[0]


# 第三步
regex = RegexConverter


# 第四步   需要在app.py中调用
# @app.route("/user/<regex('lcz.{2}'):username>")
# def user_info(username):
#     return "hello %s" % username

