from flask import Blueprint, flash, redirect, render_template, abort, url_for
from flask_login import login_required, current_user
from src.utils import roles_required
from src.view.auth.forms import RegisterForm
from src.view.profile.forms import ChangePasswordForm, EditUsernameForm
from src.models import User

profile_blueprint = Blueprint("profile", __name__)


@profile_blueprint.route("/profile")
@login_required
def profile():
    return render_template("profile/profile.html")


@profile_blueprint.route("/edit-username", methods=["GET", "POST"])
@login_required
def edit_username():
    form = EditUsernameForm(username=current_user.username)
    if form.validate_on_submit():
        new_name = form.username.data

        if User.query.filter_by(username=new_name).first() is not None and new_name != current_user.username:
            flash("Username is already taken!", "danger")
        else:
            current_user.username = new_name
            current_user.save()
            flash("Username updated!", "success")
            return redirect(url_for("profile.profile"))

    return render_template("profile/edit_username.html", form=form)


# Change password
@profile_blueprint.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if not current_user.check_password(form.current_password.data):
            flash("Current password is incorrect", "danger")
        else:
            current_user.password = form.new_password.data
            current_user.save()
            flash("Password changed successfully!", "success")
            return redirect(url_for("profile.profile"))
    return render_template("profile/change_password.html", form=form)


@profile_blueprint.route("/delete/<int:user_id>")
@login_required
@roles_required("Admin")
def delete(user_id):
    if current_user.id == user_id:
        flash("You can not delete your self baka", "danger")
    usertodel = User.query.get_or_404(user_id)
    print(usertodel)
    usertodel.delete()
    print(url_for("main.index"))
    return redirect(url_for("main.index"))


@profile_blueprint.route("/edit", methods=["GET", "POST"])
@profile_blueprint.route("/edit/<int:user_id>", methods=["GET", "POST"])
@login_required
def edit(user_id=None):
    # Case 1: no user_id -> edit current user's profile
    if user_id is None:
        user = current_user
    else:
        # Case 2: with user_id -> only admins can edit others
        if not current_user.has_role("Admin"):
            abort(403)  # Forbidden
        user = User.query.get_or_404(user_id)

    oldname = user.username
    form = RegisterForm(username=user.username, email=user.email, password=user.password)

    if form.validate_on_submit():
        user.edit(form)
        user.save()
        print(f"{oldname} has changed its name to {user.username}")

    else:
        print(form.errors)

    return render_template("profile/edit.html", form=form)
