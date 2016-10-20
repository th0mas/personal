from flask import Blueprint, render_template, abort
from blog import BlogPost
view_blueprint = Blueprint('view', __name__)

@view_blueprint.route('/')
def main():
    return("Oops! You thats not a valid post")

@view_blueprint.route('/<id>')
def view_post(id):
    post = BlogPost.query.get(id)
    if not post:
        return abort(404)

    return post.content
