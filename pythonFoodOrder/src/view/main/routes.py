from flask import Blueprint, render_template, redirect, url_for, flash
from src.view.main.forms import FeedbackForm
from src.models.product import Offer
from src.models import Role, User

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def index():
    offers = Offer.query.filter_by(active=True).all()
    return render_template("main/index.html", offers=offers)


@main_blueprint.route("/about")
def about():
    return render_template("main/about.html")


@main_blueprint.route("/branches")
def branches():
    return render_template("main/branches.html")


@main_blueprint.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        # Save to DB or send email
        flash('Thank you for your feedback!', 'success')
        print("feedback was sent")
        return redirect(url_for('main.feedback'))
    print("feedback was not sent")
    return render_template('main/feedback.html', form=form)
