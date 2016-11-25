from flask import Blueprint, render_template, redirect, url_for, request, abort, jsonify
from .api import GitHub

api_blueprint = Blueprint('apiv1', __name__)

# GITHUB API
@api_blueprint.route("/github/<path:api_path>")
def github_api_endpoint(api_path):
    processor = GitHub(api_path, request.args)

    if processor.valid_api_route():
        return jsonify(processor.get_result())
    else:
        return abort(404)
