import unittest
import blog
import tempfile
import os
from blog import models

class BlogTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd = tempfile.mkstemp()
        blog.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + self.db_fd[1]
        blog.app.config["TESTING"] = True
        blog.app.config["WTF_CSRF_ENABLED"] = False # Dont need to pass token with testing
        self.app = blog.app.test_client()
        self.db = blog.db

        with blog.app.app_context():
            self.db.create_all()

    def tearDown(self):
        self.db.drop_all()
        self.db.session.remove()
        os.close(self.db_fd[0])
        os.unlink(self.db_fd[1])

    def test_url_path(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_blog_db(self):
        test_post = models.post.BlogPost(
        "test_title", "test content"
        )
        self.db.session.add(test_post)
        self.db.session.commit()

        self.assertEqual(test_post.title, "test_title")
        self.assertEqual(test_post.content, "test content")

    def test_create_form(self):
        rc = self.app.post('/create/', data={
            "title": "test title",
            "tags": "test, post",
            "post": "This is a post!"
        }, follow_redirects=True)
        rc = rc.data.decode()
        assert "This is a post!" in rc

if __name__ == "__main__":
    unittest.main()
