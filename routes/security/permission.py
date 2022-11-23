from flask import request, jsonify, Blueprint
import requests
from settings import SECURITY_URL

permission_bp = Blueprint("permission_blueprint", __name__)


@permission_bp.route("", methods=["POST"])
def create_permission():
    body = request.get_json()
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.post(
        url=f"{SECURITY_URL}/permissions",
        headers=headers,
        json=body
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al crear el permiso"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


@permission_bp.route("", methods=["GET"])
def list_permission():
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.get(
        url=f"{SECURITY_URL}/permissions",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al obtener los permisos"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


@permission_bp.route("/<string:permission_id>", methods=["GET"])
def get_permission(permission_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.get(
        url=f"{SECURITY_URL}/permissions/{permission_id}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al obtener el permiso"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


@permission_bp.route("/<string:permission_id>", methods=["PUT"])
def update_permission(permission_id):
    body = request.get_json()
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.put(
        url=f"{SECURITY_URL}/permissions/{permission_id}",
        headers=headers,
        json=body
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al actualizar el permiso"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


@permission_bp.route("/<string:permission_id>", methods=["DELETE"])
def delete_permission(permission_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.delete(
        url=f"{SECURITY_URL}/permissions/{permission_id}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al eliminar el permiso"
        }), 500
    else:
        return jsonify(response.json()), response.status_code