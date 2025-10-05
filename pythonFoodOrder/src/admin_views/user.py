from src.admin_views.base import SecureModelView
from src.admin_views.admin_forms import UserAdminForm
from src.ext import db
from src.models import User, Role, UserRole


class UserView(SecureModelView):
    can_view_details = True
    can_delete = True  # enable deletion

    column_list = ("username", "email", "role_names")  # role_names computed manually
    column_details_list = ("username", "email", "_password", "role_names")
    column_searchable_list = ["username"]

    form = UserAdminForm
    form_excluded_columns = ("products", "password", "_password", "roles")

    # ------------------------
    # Manual creation
    # ------------------------
    def create_model(self, form):
        if not form.password_plain.data:
            raise ValueError("Password is required when creating a new user")

        # Create user
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password_plain.data
        )
        db.session.add(user)
        db.session.commit()  # commit to generate user.id

        # Assign roles manually via UserRole
        role_ids = form.roles.data or []
        for role_id in role_ids:
            ur = UserRole(user_id=user.id, role_id=role_id)
            db.session.add(ur)

        db.session.commit()
        return True

    # ------------------------
    # Manual update
    # ------------------------
    def update_model(self, form, model):

        model.username = form.username.data
        model.email = form.email.data
        if form.password_plain.data:
            model.password = form.password_plain.data
        db.session.commit()

        # --------------------
        # Fetch current roles
        # --------------------
        current_role_ids = set(
            ur.role_id for ur in db.session.query(UserRole).filter(UserRole.user_id == model.id).all()
        )
        new_role_ids = set(form.roles.data or [])

        # --------------------
        # Add new roles manually
        # --------------------
        for role_id in new_role_ids - current_role_ids:
            ur = UserRole(user_id=model.id, role_id=role_id)
            db.session.add(ur)

        # --------------------
        # Remove roles that were unchecked
        # --------------------
        for role_id in current_role_ids - new_role_ids:
            db.session.query(UserRole).filter(
                UserRole.user_id == model.id,
                UserRole.role_id == role_id
            ).delete()

        db.session.commit()
        return True

    # ------------------------
    # Manual deletion
    # ------------------------
    def delete_model(self, model):
        # Delete all user-role associations
        if model.id == 1:
            raise ValueError("You can not delete primary account")

        db.session.query(UserRole).filter(UserRole.user_id == model.id).delete()
        db.session.commit()

        # Delete the user
        db.session.delete(model)
        db.session.commit()
        return True

    # ------------------------
    # Prefill roles for edit form
    def edit_form(self, obj=None):
        form = UserAdminForm()
        if obj:
            form.username.data = obj.username
            form.email.data = obj.email
            # manually fetch role ids from UserRole table
            role_ids = [ur.role_id for ur in db.session.query(UserRole).filter(UserRole.user_id == obj.id).all()]
            form.roles.data = role_ids
        return form

    # ------------------------
    # Helper to display role names
    # ------------------------
    def _role_names_formatter(self, context, model, name):
        # get role names manually
        role_ids = [ur.role_id for ur in db.session.query(UserRole).filter(UserRole.user_id == model.id).all()]
        roles = db.session.query(Role).filter(Role.id.in_(role_ids)).all()
        return ", ".join([r.name for r in roles])

    column_formatters = {
        'role_names': _role_names_formatter
    }
