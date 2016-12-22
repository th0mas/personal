from flask import Blueprint, render_template, redirect, url_for, request, abort, jsonify
from .api import GitHub

api_blueprint = Blueprint('apiv1', __name__)

"""
GITHUB API METHODS
"""
@api_blueprint.route("/github/<path:api_path>")
def github_api_endpoint(api_path):
    # Initialize Github API processor
    processor = GitHub(api_path, request.args)

    # Check route is valid
    if processor.valid_api_route():
        # Return the result, formatted as JSON
        return jsonify(processor.get_result())
    else:
        # if it cant process, return 404
        return abort(404)
