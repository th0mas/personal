import requests
from flask import request, flash
from blog import app, cache

def contact_form_send_email(content):
    """
    Sends an email using the MailGun API
    content: WTForms object including:
        email.data : the email entered in the format
        subject.data : the subject
        message.data : the content of the email

    Caches the logon to prevent spam using a crude ip cache
    """
    remote_ip = request.remote_addr
    if cache.get(remote_ip) == "cached!":
        flash("Sorry! To prevent spam, sending from your IP has been disabled for a while. Sorry about this.")

    else:
        # To prevent spam we ignore this and return an error
        email_data = {
            "from": content.email.data,
            "to": ["tom@tomhaines.xyz"],
            "subject": content.subject.data,
            "text": content.message.data
            }

        r = requests.post(
            "https://api.mailgun.net/v3/{}/messages".format(app.config["MAILGUN_DOMAIN"]),
            auth=("api", app.config["MAILGUN_API_KEY"]),
            data=email_data
        )
        cache.set(remote_ip, "cached!")
        cache.expire(remote_ip, 600)
        flash("Thanks your message has been recieved")
