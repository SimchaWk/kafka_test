from flask import Blueprint, jsonify

from app.services.queries_service import get_email_by_address, get_most_common_word

queries_bp = Blueprint('queries', __name__)


@queries_bp.route('/email/<email_address>', methods=['GET'])
def get_email_details(email_address: str):
    data = get_email_by_address(email_address)
    if data:
        return jsonify(data), 200
    return jsonify({'error': f'Email {email_address} not found'}), 404


@queries_bp.route('stats/most-common-word', methods=['GET'])
def get_most_common_word_stats():
    stats = get_most_common_word()
    if stats["word"] is None:
        return jsonify({
            "error": "No words found in database",
            "stats": stats
        }), 404

    return jsonify({
        "message": "Statistics retrieved successfully",
        "stats": stats
    }), 200
