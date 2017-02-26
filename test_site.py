import unittest
import blog
import tempfile
import os
from blog import models
from blog import bcrypt
from flask_login import login_user, current_user
from flask import url_for

class BaseTestCase(unittest.TestCase):
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

class BasicTestCase(BaseTestCase):
    def test_home_url(self):
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

    def test_blog_url(self):
        result = self.app.get('/blog/1/')
        self.assertEqual(result.status_code, 200)

    def test_api_github_get_recent_repos(self):
        # Make sure
        result = self.app.get('/api/v1/github/get_recent_repos/')
        self.assertEqual(result.status_code, 200)

    def test_api_github_get_last_activity(self):
        result = self.app.get('/api/v1/github/last_activity/')
        self.assertEqual(result.status_code, 200)

    def test_user_account_create(self):
        test_user = models.auth.User("test@example.com",
            "testpass1",
            "ADM")
        self.db.session.add(test_user)
        self.db.session.commit()

        hashed_pw = bcrypt.generate_password_hash("testpass1")

        self.assertTrue(test_user.check_password_hash("testpass1"))
        self.assertEqual(test_user.get_id(), "test@example.com")
    
    def test_contact_form(self):
        r = self.app.post('/',
            data={
                "name": "test",
                "email": "testemail@email.com",
                "subject": "test_subject",
                "message": "message"
            })
        self.assertEqual(302, r.status_code)

    def test_login_security(self):
        result = self.app.get('/create/')
        self.assertEqual(result.status_code, 401)

    def test_error_404(self):
        result = self.app.get('/pagethatdoesntexist/')
        self.assertEqual(result.status_code, 404)
    
    def test_api_error_404(self):
        result = self.app.get('/api/v1/github/doesnotexist/')
        self.assertEqual(result.status_code, 404)

class LoggedInTestCase(BaseTestCase):
    def setUp(self):
        super(LoggedInTestCase, self).setUp()
        user = models.auth.User("testusr@example.com", "TestPass1", "ADM")
        self.db.session.add(user)
        self.db.session.commit()

    def tearDown(self):
        super(LoggedInTestCase, self).tearDown()

    def log_in(self):
        self.app.post('/login/',
            data={"email": "testusr@example.com", "password": "TestPass1"},
            follow_redirects=True)

    def test_log_in(self):
        with self.app:
            self.log_in()
            self.assertEqual(current_user.email, "testusr@example.com")

    def test_create_page(self):
        with self.app:
            self.log_in()

            result = self.app.post('/create/',
                data={"title": "test post", "post": "test content"},
                follow_redirects=True)

            self.assertIn("test content", result.data.decode())
    
    def test_logout_method(self):
        self.log_in()
        result = self.app.get('/logout/')
        self.assertEqual(result.status_code, 302)

if __name__ == "__main__":
    unittest.main()
    