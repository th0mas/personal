from flask import Blueprint, render_template, redirect, url_for
from .forms import CreateForm
from blog import db, BlogPost

create_blueprint = Blueprint('create', __name__)

@create_blueprint.route('/', methods=["GET", "POST"])
def main():
    create_form = CreateForm()
    if create_form.validate_on_submit():
        new_post = BlogPost(
            create_form.title.data,
            create_form.post.data,
            )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('view.view_post', id=new_post.id))
    return render_template('/create/create.html', create_form=create_form)
