"""rmon.views.urls

定义了所有 API 对应的 URI
"""
from flask import Blueprint
from rmon.views.index import IndexView
from rmon.views.server import ServerList
from rmon.views.server import ServerDetail

api = Blueprint('api',__name__)
api.add_url_rule('/',view_func=IndexView.as_view('index'))
api.add_url_rule('/servers',view_func=ServerList.as_view('server_list'))
app.add_url_rule('/servers/<int:object_id>',view_func=ServerDetail.as_view('server_datail'))
