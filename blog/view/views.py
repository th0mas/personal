from flask import Blueprint, render_template, abort, request
from blog import BlogPost
from sqlalchemy import desc

view_blueprint = Blueprint('view', __name__)

@view_blueprint.route('/')
def main():
    args = request.args
    if "page" in args:
        page = int(args['page'])
        end = (page * 5)
        start = end - 5
    else:
        start = 0
        end = 5
    posts = BlogPost.query.order_by(desc(BlogPost.id)).all()[start:end]

    
    return render_template("/view/view_all.html", posts=posts)

@view_blueprint.route('/<id>')
def view_post(id):
    post = BlogPost.query.get(id)
    if not post:
        return abort(404)

    return post.content
