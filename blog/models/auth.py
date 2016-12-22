# Models for authentication
from blog import db, bcrypt

class User(db.Model):
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.LargeBinary())

    role = db.Column(db.String(3))

    #flask_login requirements
    is_authenticated = True
    is_anonymous = False
    is_account_active = db.Column(db.Boolean)

    def __init__(self, email, password, role=""):
        """
        Set User object values, including default role.
        Hashes password
        """
        self.email = email
        self.password = self.create_password_hash(password)
        self.is_account_active = True
        if role:
            self.role = role
        else:
            self.role = "usr"

    def is_active(self):
        """Returns if the account is active"""
        return bool(self.is_account_active)

    def get_id(self):
        """Used for flask-login, gets the users id from database"""
        return self.email

    def create_password_hash(self, password):
        """Creates a secure password hash using bcrypt"""
        return bcrypt.generate_password_hash(password)

    def check_password_hash(self, password):
        """
        Checks the password entered against the hash 
        in the database
        """
        return bcrypt.check_password_hash(self.password, password)
