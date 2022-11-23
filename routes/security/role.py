from flask import request, jsonify, Blueprint
import requests
from settings import SECURITY_URL

role_bp = Blueprint("role_blueprint", __name__)


@role_bp.route("", methods=["POST"])
def create_role():
    body = request.get_json()
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.post(
        url=f"{SECURITY_URL}/roles",
        headers=headers,
        json=body
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al crear rol"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


@role_bp.route("", methods=["GET"])
def list_roles():
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.get(
        url=f"{SECURITY_URL}/roles",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al obtener los roles"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


@role_bp.route("/<string:role_id>", methods=["GET"])
def get_role(role_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.get(
        url=f"{SECURITY_URL}/roles/{role_id}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al obtener los roles por id"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


@role_bp.route("/<string:role_id>", methods=["PUT"])
def update_role(role_id):
    body = request.get_json()
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.put(
        url=f"{SECURITY_URL}/roles/{role_id}",
        headers=headers,
        json=body
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al actualizar el rol"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


@role_bp.route("/<string:role_id>", methods=["DELETE"])
def delete_role(role_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.delete(
        url=f"{SECURITY_URL}/roles/{role_id}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al eliminar el rol"
        }), 500
    else:
        return jsonify(response.json()), response.status_code