# My personal site.
[![Build Status](https://travis-ci.org/TomIsPrettyCool/personal.svg?branch=master)](https://travis-ci.org/TomIsPrettyCool/personal)
[![Coverage Status](https://coveralls.io/repos/github/TomIsPrettyCool/personal/badge.svg?branch=master)](https://coveralls.io/github/TomIsPrettyCool/personal?branch=master)

This is the repo that powers my personal site. Not very interesting, its just cheaper when you open source everything. 

Set up to run on Heroku style services (I run on Dokku)

In case you want to run, the instructions are here. 
Mainly just so I don't forget.

## Running
#### Prequesites:
You need pip, virtualenv, a SQL thing and a Redis cache availiable.
#### \*nix systems:
```
git clone https://github.com/TomIsPrettyCool/personal.git #Get the repo
cd personal
virtualenv env # Create a virtual environment, I use python 3
source env/bin/activate # Activate the new shiny environment
pip install -r requirements.txt # Load in the many requirements
export FLASK_APP=blog:app && DATABASE_URL=<db_url> && flask db upgrade #create db
```
Done! There are several other environment variables needed to run, I will list them here, create a script or something.
```
DATABASE_URL:<The Database URL>
FLASK_DEBUG: <Enable debugging mode, takes a 1 or 0>
FLASK_APP: <Path to the flask app, usually blog:app>
REDIS_URL: <URI for the redis cache
GITHUB_TOKEN: <Github API token>
MAILGUN_DOMAIN: <Mailgun domain>
MAILGUN_API_KEY: <What do you expect>
SENTRY_DSN: <This app uses sentry to debug. You should try it>
```
Finally you can run with: `flask run`

# Other
:)
