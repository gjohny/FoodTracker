from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_user_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://default:zI2KueQhmL8X@ep-jolly-shadow-a4bh5699-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require'
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Food

    with app.app_context():
        # db.drop_all()
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# def create_database(arg):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(arg = arg)
#         print('Created Database')
