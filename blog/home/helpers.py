import requests
from blog import app

# Email helper
def contact_form_send_email(content):
    email_data = {
        "from": "personalsite@tomhaines.xyz",
        "to": "tom@tomhaines.xyz",
        "subject": content.subject.data,
        "message": content.message.data
    }

    requests.post(
        "https://api.mailgun.net/v3/{}/messages".format(app.config["MAILGUN_DOMAIN"]),
        auth=("api", app.config["MAILGUN_API_KEY"]),
        data=email_data
    )