from src.admin_views.base import SecureModelView


class UserView(SecureModelView):
    can_view_details = True
    can_delete = False

    column_list = ("username", "email")
    column_details_list = ("username", "email", "_password")
    column_searchable_list = ["username"]