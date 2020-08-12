from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from myApp import create_app
from myApp.exts import db

app = create_app()

# 迁移管理对象
migrate = Migrate(app,db)

# 创建工程实例
manager = Manager(app)

# 给工程管理对象添加 db 命令
manager.add_command("db",MigrateCommand)


if __name__ == '__main__':
    manager.run()
