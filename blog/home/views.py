from flask import Blueprint, render_template
from blog import BlogPost
from sqlalchemy import desc

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/')
def home():
    recent = BlogPost.query.order_by(desc(BlogPost.id)).first()
    return render_template('/home/index.html', post=recent)
