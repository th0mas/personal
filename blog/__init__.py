import os
import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = "devkey"

#Initialize database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)

#Initialize redis cache
cache = redis.StrictRedis(os.environ.get("REDIS_URL"))

# Import and Initialize blueprints
from blog.models.post import BlogPost
from blog.home.views import home_blueprint
from blog.view.views import view_blueprint
from blog.create.views import create_blueprint
from blog.api.v1.views import api_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(view_blueprint, url_prefix='/view')
app.register_blueprint(create_blueprint, url_prefix='/create')
app.register_blueprint(api_blueprint, url_prefix='/api/v1')
