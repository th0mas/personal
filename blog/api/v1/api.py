from github import Github
from flask import abort
from blog import cache, app
import pickle

class GitHub():
    def __init__(self, path, args):
        self.g = Github(user_agent="TomIsPrettyCool", login_or_token=app.config["GITHUB_ACCESS_TOKEN"])
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

    # Github API methods
    def get_recent_repos(self):
		# Cache and get GitHub repos! Could be done nicer, but it works so isn't a priority
        if cache.exists("github_repos"):
            return pickle.loads(cache.get("github_repos"))
        else:
            github_user = self.g.get_user(login="TomIsPrettyCool")
            repos = github_user.get_repos()
            repo_array = [{"name": x.name, "url": x.html_url} for x in repos]
            cache.set("github_repos", pickle.dumps(repo_array))
            cache.expire("github_repos", 30)
            return repo_array
