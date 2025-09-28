from flask_admin.contrib.sqla import ModelView
from wtforms.fields import PasswordField
from markupsafe import Markup
from src.models import User, Role

from src.admin_views.base import SecureModelView

#
# class UserView(SecureModelView):
#     can_view_details = True
#     can_delete = False
#
#     column_list = ("username", "email")
#     column_details_list = ("username", "email", "_password")
#     column_searchable_list = ["username"]


# class UserView(SecureModelView):
#     """Flask-Admin view for managing users"""
#
#     can_view_details = True   # allows opening detailed view
#     can_delete = False        # prevent accidental deletions
#
#     # Columns displayed in the table
#     column_list = ("username", "email", "get_role_names")
#     column_details_list = ("username", "email", "_password", "roles")
#
#     # Columns searchable in the table
#     column_searchable_list = ["username", "email"]
#
#     # Filters for admin to narrow down the list
#     column_filters = ["roles.name"]
#
#     # Columns editable inline in list view
#     column_editable_list = ("username", "email")
#
#     # Show roles as readable names instead of relationship object
#     column_formatters = {
#         "get_role_names": lambda v, c, m, n: ", ".join(m.get_role_names)
#     }
#
#     # Fields shown in create/edit forms
#     form_columns = ["username", "email", "password"]
#
#     # Override password field to render as a password input
#     form_overrides = {"password": PasswordField}
#
#     # Enable AJAX search for roles when assigning them
#     # form_ajax_refs = {
#     #     'roles': {
#     #         'fields': ['name']
#     #     }
#     # }
#
#
#     form_columns = ["username", "email", "password"]
#     form_overrides = {"password": PasswordField}
#     # form_ajax_refs = {
#     #     'roles': {'fields': ['name']}
#     # }
class UserView(SecureModelView):
    can_view_details = True
    can_delete = False

    column_list = ("username", "email")  # only real columns
    column_searchable_list = ["username", "email"]
    column_filters = ["roles.name"]
    column_editable_list = ("username", "email")

    column_formatters = {
        "get_role_names": lambda v, c, m, n: ", ".join(m.get_role_names)
    }

    form_columns = ["username", "email", "roles"]
    form_ajax_refs = {
        'roles': {'fields': ['name']}
    }

    form_extra_fields = {
        "password": PasswordField("Password")
    }

    def on_model_change(self, form, model, is_created):
        if form.password.data:
            model.password = form.password.data  # hashes automatically
