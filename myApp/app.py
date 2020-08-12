from flask import Flask

from configs import DevelopmentConfig
from myApp.api import urls
from myApp.exts import db


def create_app():
    # app = Flask("应用名")
    app = Flask("myApp")

    # 加载配置
    app.config.from_object(DevelopmentConfig)

    # 加载三方对象
    db.init_app(app)

    # 注册蓝图
    app.register_blueprint(urls)

    return app