from flask import Blueprint, request, jsonify
from app.services.imei_service import IMEIService
from app.models.users import User

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/check-imei', methods=['POST'])
def check_imei():
    imei = request.json.get('deviceId')
    token = request.headers.get('Authorization')

    if not imei or not token:
        return jsonify({"error": "IMEI and token are required"}), 400

    if token.startswith("Bearer "):
        token = token[len("Bearer "):]

    user = User.query.filter_by(token=token).first()
    if not user:
        return jsonify({"error": "Unauthorized user"}), 403

    imei_data = IMEIService.check_imei_is_valid(imei, token, service_id=12)

    if 'error' in imei_data:
        return jsonify(imei_data), 400

    return jsonify(imei_data), 200



