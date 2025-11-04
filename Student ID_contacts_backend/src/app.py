from flask import Flask
from flask_cors import CORS
import os
from .models import db
from .routes import init_routes

def create_app():
    app = Flask(__name__)
    CORS(app)

    # 配置数据库
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '..', 'contacts.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 初始化数据库
    db.init_app(app)

    # 初始化路由
    init_routes(app)

    # 创建数据库表
    with app.app_context():
        db.create_all()

    return app

app = create_app()
