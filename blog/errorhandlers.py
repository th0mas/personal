from blog import app
from flask import redirect, url_for, flash

@app.errorhandler(401)
def unauthorized(error):
    flash("401, You need to login to access this")
    return redirect(url_for("home.login"))

@app.errorhandler(404)
def page_not_found(error):
    flash("404, that page wasn't found :(")
    return redirect(url_for("home.home"))