"""
Models for BLOG posts
"""
from blog import db
from datetime import datetime
from sqlalchemy import desc

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.Text)
    datetimeposted = db.Column(db.DateTime)

    def __init__(self, title, content):
        """
        Set the values of the Model, sets the time posted
        """
        self.title = title
        self.content = content
        self.datetimeposted = datetime.utcnow()

    @staticmethod
    def get_pagination(page):
        """
        Returns a page of blog posts.
        Also has other helpers such as next page that can be used in templating.
        """
        return BlogPost.query.order_by(desc(BlogPost.datetimeposted)).paginate(
                                        page=page, per_page=5)

