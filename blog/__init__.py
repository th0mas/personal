import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = "devkey"

#Initialize database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)
from blog.models.post import BlogPost

from blog.home.views import home_blueprint
from blog.view.views import view_blueprint
from blog.create.views import create_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(view_blueprint, url_prefix='/view')
app.register_blueprint(create_blueprint, url_prefix='/create')
