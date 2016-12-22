from github import Github
from flask import abort
from blog import cache, app
import pickle


class GitHub():
    """
    Pull specific data down from the Github API
    Designed to be extendable
    """
    def __init__(self, path, args):
        self.g = Github(user_agent="TomIsPrettyCool",
                        login_or_token=app.config["GITHUB_ACCESS_TOKEN"])
        self.path = path
        self.route = path.split('/')

        if args:
            self.args = args

    def valid_api_route(self):
        """
        Check the API route is valid/Make sure theres a function for it
        """
        return hasattr(self, self.route[0])

    def get_result(self):
        """
        Return the result from the function called from the API.
        """
        return getattr(self, self.route[0])()

    # Github API methods
    def get_recent_repos(self):
        """
        Method to get my Repos on Github and return them as a JSON formatted list
        """
        if cache.exists("github_repos"):
            return pickle.loads(cache.get("github_repos"))
        else:
            repos = self.g.search_repositories(
                query="user:TomIsPrettyCool", sort="updated", order="desc", fork="true")
            repo_array = [{"name": x.name, "url": x.html_url,
                           "last-edit": ""} for x in repos]

            # Need to add last activity on GitHub

            cache.set("github_repos", pickle.dumps(repo_array))
            cache.expire("github_repos", 60)
            return repo_array

    def last_activity(self):
        """
        Method to get my last activity on Github, return as JSON values.
        """
        if cache.exists("github_last_activity"):
            return pickle.loads(cache.get("github_last_activity"))
        else:
            events = self.g.get_user("TomIsPrettyCool").get_public_events()[:3]

            for event in events:
                if event.type == "PushEvent":
                    commit_message = event.payload["commits"][0]["message"]
                    activity = "pushing to the repo {0}: ".format(
                        event.repo.name
                    )
                    response = {"activity": activity,
                                "repo": {"url": event.repo.html_url, "name": event.repo.name},
                                "time": event.created_at,
                                "commit_message": commit_message}
                    break
            cache.set("github_last_activity", pickle.dumps(response))
            cache.expire("github_last_activity", 60)
            return response
