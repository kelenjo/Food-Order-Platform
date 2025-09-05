from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user
from flask import abort


class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.roles.name == "admin"

    def inaccessible_callback(self, name, **kwargs):
        return abort(403)


class SecureIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.roles.name == "admin"

    def inaccessible_callback(self, name, **kwargs):
        return abort(403)


