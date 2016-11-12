from flask import Blueprint, render_template, abort, request
from blog import BlogPost
from sqlalchemy import desc

view_blueprint = Blueprint('blog', __name__)

@view_blueprint.route('/<int:page>/')
def main(page):
    posts = BlogPost.get_pagination(page)
    return render_template("/view/view_all.html", posts=posts)

@view_blueprint.route('/post/<id>/')
def view_post(id):
    post = BlogPost.query.get(id)
    if not post:
        return abort(404)

    return post.content
