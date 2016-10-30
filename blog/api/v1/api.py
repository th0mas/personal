from github import Github
from flask import abort
from blog import cache, app
import pickle

class Api():
    def __init__(self, path, args=""):
        self.path = path
        self.route = path.split('/')

        if args:
            self.args = args

    def valid_api_route(self):
        if hasattr(self, self.route[0]):
            return True
        else:
            return False

    def get_result(self):
        return getattr(self, self.route[0])()

    def github(self):
        # Initialize Github api client then call correc
        print(self.route[1])
        g = Github(user_agent="TomIsPrettyCool", login_or_token=app.config["GITHUB_ACCESS_TOKEN"])
        return getattr(self, "_github_{}".format(self.route[1]))(g)

    # Github API methods
    def _github_get_recent_repos(self, g):
		# Cache and get GitHub repos! Could be done nicer, but it works so isn't a priority
        if cache.exists("github_repos"):
            return pickle.loads(cache.get("github_repos"))
        else:
            github_user = g.get_user(login="TomIsPrettyCool")
            repos = github_user.get_repos()
            repo_array = [{"name": x.name, "url": x.html_url} for x in repos]
            cache.set("github_repos", pickle.dumps(repo_array))
            cache.expire("github_repos", 30)
            return repo_array
