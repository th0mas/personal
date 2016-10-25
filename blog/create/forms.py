"""Forms for the 'create' part of the site,
these revolve around creating and editing blog posts"""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField
from wtforms.validators import DataRequired

class CreateForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    tags = StringField('tags')
    post = TextAreaField('post')
