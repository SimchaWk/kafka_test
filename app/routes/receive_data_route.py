from idlelib.pyparse import trans

from flask import Blueprint, request, jsonify

receive_data_bp = Blueprint('receive_data', __name__)


@receive_data_bp.route('/email', methods=['POST'])
def new_member():
    data = request.json
    if True:
        return jsonify('Data saved successfully.'), 200
    else:
        return jsonify('Failed to save data.'), 500