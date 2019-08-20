from flask import jsonify
from flask_jwt_extended.config import config


def default_cloud_provider_callback(error_string):

    return jsonify({config.error_msg_key: error_string}), 401
