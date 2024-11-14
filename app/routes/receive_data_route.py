from flask import Blueprint, request, jsonify

from app.services.produce.rew_data_producer import produce_new_rew_data

receive_data_bp = Blueprint('receive_data', __name__)


@receive_data_bp.route('/email', methods=['POST'])
def new_member():
    data = request.json
    if produce_new_rew_data(data):
        return jsonify('Data received successfully.'), 200
    else:
        return jsonify('Failed to received data.'), 500
