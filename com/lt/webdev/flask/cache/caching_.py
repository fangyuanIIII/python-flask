"""
初始化缓存
pip install flask-caching
"""
from flask_caching import Cache
from flask import Blueprint,request
bp = Blueprint('cache', __name__,url_prefix='/cache_')
cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})

def init(app):
    cache.init_app(app=app)

#设置缓存超时时间      当缓存返回时   不执行cache_内部语句只返回结果
@bp.route('/')
@cache.cached(timeout=10)
def cache_():
    print('cache')
    return "ok"

@bp.before_request
def before():
    print('before')
    ip = request.remote_addr
    print(ip)
    if cache.get(ip) :
        return "不要爬了"
    else:
        #设置缓存10s 钟
        cache.set(ip,"val",timeout=10)
