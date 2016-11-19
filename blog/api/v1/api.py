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
        return hasattr(self, self.route[0])

    def get_result(self):
        return getattr(self, self.route[0])()

    # Github API methods
    def get_recent_repos(self):
		# Cache and get GitHub repos! Could be done nicer, but it works so isn't a priority
        if cache.exists("github_repos"):
            return pickle.loads(cache.get("github_repos"))
        else:
            repos = self.g.search_repositories(query="user:TomIsPrettyCool", sort="updated", order="desc", fork="true")
            repo_array =  [{"name": x.name, "url": x.html_url, "last-edit":""} for x in repos]

            # Need to add last activity on GitHub

            cache.set("github_repos", pickle.dumps(repo_array))
            cache.expire("github_repos", 30)
            return repo_array

    def last_activity(self):
        # Get last activity on github, spaghetti code incoming
        event = self.g.get_user("TomIsPrettyCool").get_public_events()[0]
        response = {"payload": event.payload, 
                    "repo": {"url": event.repo.html_url, "name": event.repo.name},
                    "time": event.created_at,
                    "type": event.type}
        
        return response
