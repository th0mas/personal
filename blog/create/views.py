from flask import Blueprint, render_template, redirect, url_for
from .forms import CreateForm
from blog import db, BlogPost
from flask_login import login_required

create_blueprint = Blueprint('create', __name__)


@create_blueprint.route('/', methods=["GET", "POST"])
@login_required
def main():
    # Initliaze WTForms create post object
    create_form = CreateForm()

    # If the form is valid add to DB
    if create_form.validate_on_submit():
        new_post = BlogPost(
            create_form.title.data,
            create_form.post.data,
            )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('blog.view_post', id=new_post.id))
    # Else render the form
    return render_template('/create/create.html', create_form=create_form)
