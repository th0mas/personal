from flask import Blueprint, render_template, redirect, flash
from blog import BlogPost, User
from sqlalchemy import desc
from flask_login import login_user, logout_user, login_required
from .forms import LoginForm

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/')
def home():
    recent = BlogPost.query.order_by(desc(BlogPost.id)).first()
    return render_template('/home/index.html', post=recent)

@home_blueprint.route('/login/', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.get(login_form.email.data)

        if user and user.check_password_hash(login_form.password.data):
            login_user(user)
            return redirect("/")
        else:
            flash("Failed to login: email or password is incorrect")

    return render_template('/home/auth.html', form=login_form)

@home_blueprint.route('/logout/')
def logout():
    logout_user()
    return redirect('/')
