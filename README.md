# My personal site - tomhaines.xyz
[![Build Status](https://travis-ci.org/TomIsPrettyCool/personal.svg?branch=master)](https://travis-ci.org/TomIsPrettyCool/personal)
[![Coverage Status](https://coveralls.io/repos/github/TomIsPrettyCool/personal/badge.svg?branch=master)](https://coveralls.io/github/TomIsPrettyCool/personal?branch=master)

The Big One. A blog and my landing page rolled into one.

This is my main site, a blog and portfolio.

## Running

From the root directory:
Install dependencies: `pip install -r requirements.txt`

Initialize the Flask environment variables:
`export FLASK_APP=blog:app && export FLASK_DEBUG=1`

Set the database environment var (App is set up for PostgreSQL and SQLITE3): `export DATABASE_URL=<Database URI>`

Run the app: `python -m flask run`

If running windows, there is a bat file that can be run

## Tests
Tests are in `site_tests.py` and can be run with simply `python site-tests.py`

## Todo:
Make a todo list
