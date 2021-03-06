#!/usr/bin/env python

from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from libs.orm import db
from user.views import user_bp

# 初始化 app
app = Flask(__name__)
app.secret_key = r'7uhgt6&*IJHgfde45edfdsw2#$%RE32wsdfgui9876tyU&^%$#ews'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://seamile:123@localhost:3306/weibo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 每次请求结束后都会自动提交数据库中的变动

# 初始化 manager
manager = Manager(app)

# 初始化 db 和 migrate
db.init_app(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# 注册蓝图
app.register_blueprint(user_bp)


@app.route('/')
def home():
    '''首页'''
    return 'hello world'


if __name__ == "__main__":
    manager.run()
