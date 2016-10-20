from github import Github
from flask import abort

class Api():
    g = Github(user_agent="TomIsPrettyCool")
    github_user = g.get_user(login="TomIsPrettyCool")
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
        print(self.route[1])
        return getattr(self, "_github_{}".format(self.route[1]))()

    # API Methods declared here!
    def _github_get_recent_repos(self,):
        repos = self.github_user.get_repos()
        return [{"name": x.name, "url": x.html_url} for x in repos]
