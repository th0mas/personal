from blog import app
from flask import redirect, url_for, flash, render_template

@app.errorhandler(401)
def unauthorized(error):
    """
    Returns error 401, redirects the user to home
    """
    return redirect(url_for("home.home")), 401

@app.errorhandler(404)
def page_not_found(error):
    """
    Returns error 404, returns an error page
    """
    return render_template("error.html", error=404, description="page not found"), 404