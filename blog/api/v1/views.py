from flask import Blueprint, render_template, redirect, url_for, request, abort, jsonify
from .api import Api

api_blueprint = Blueprint('apiv1', __name__)

@api_blueprint.route("/<path:api_path>")
def api_endpoint(api_path):
    processor = Api(api_path, request.args)

    if processor.valid_api_route():
        return jsonify(processor.get_result())
    else:
        return abort(404)
