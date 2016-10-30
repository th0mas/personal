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
        self.email = email
        self.password = self.create_password_hash(password)
        self.is_account_active = True
        if role:
            self.role = role
        else:
            self.role = "usr"

    def is_active(self):
        return bool(self.is_account_active)

    def get_id(self):
        return self.email

    def create_password_hash(self, password):
        return bcrypt.generate_password_hash(password)

    def check_password_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)
