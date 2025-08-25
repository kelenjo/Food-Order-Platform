from flask import Flask
from src.admin_views.base import SecureModelView
from src.admin_views import UserView, ProductView
from src.config import Config
from src.ext import db, migrate, login_manager, admin
from src.view import product_blueprint, auth_blueprint, main_blueprint
from src.commands import init_db_command, populate_db_command
from src.models import User, Product
from flask_admin.menu import MenuLink

Blueprints = [product_blueprint, auth_blueprint, main_blueprint]
Commands = [init_db_command, populate_db_command]


def create_app(test_config=None):

    app = Flask(__name__)
    app.config.from_object(Config)

    # Then override with test config if passed
    if test_config:
        app.config.update(test_config)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extensions(app):

    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)

    # Flask-LoginManager
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(_id)

    # Flask-Admin
    admin.init_app(app)
    admin.add_view(UserView(User, db.session))
    admin.add_view(ProductView(Product, db.session, endpoint="product_admin"))

    admin.add_link(MenuLink("Back To Site", url="/", icon_type="fa", icon_value="fa-sing-out"))


def register_blueprints(app):
    for blueprint in Blueprints:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in Commands:
        app.cli.add_command(command)


