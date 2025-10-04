from wtforms.fields import PasswordField
from markupsafe import Markup
from src.models import User, Role
from src.admin_views.base import SecureModelView

#
# class UserView(SecureModelView):
#
#     create_modal = True
#     edit_modal = True
#     form_columns = ["username", "email", "roles", "password"]
#     form_ajax_refs = {"roles": {"fields": ["name"]}}
#     form_extra_fields = {"password": PasswordField("Password")}



from wtforms.fields import PasswordField
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from src.models import User, Role
from src.admin_views.base import SecureModelView

from wtforms.fields import PasswordField
from markupsafe import Markup
from src.models import User, Role
from src.admin_views.base import SecureModelView

from wtforms_sqlalchemy.fields import QuerySelectMultipleField

class UserView(SecureModelView):
    create_modal = True
    edit_modal = True
    column_list = ("username", "email", "get_role_names")
    column_formatters = {
        "get_role_names": lambda v, c, m, n: ", ".join([r.name for r in m.roles])
    }

    form_overrides = {"roles": QuerySelectMultipleField}
    form_args = {
        "roles": {
            "query_factory": lambda: Role.query.all(),
            "get_label": "name",
            "allow_blank": False
        }
    }
    form_columns = ["username", "email", "roles", "password"]
    form_extra_fields = {"password": PasswordField("Password")}

    def on_model_change(self, form, model, is_created):
        if form.password.data:
            model.password = form.password.data
