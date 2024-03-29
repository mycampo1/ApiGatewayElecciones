from flask import request, jsonify, Blueprint
import requests
from settings import SECURITY_URL

user_bp = Blueprint("user_blueprint", __name__)


@user_bp.route("", methods=["GET"])
def users():
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.get(
        url=f"{SECURITY_URL}/users",  # localhost:8080/users (ms seguridad)
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al obtener la información de los usuarios"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


@user_bp.route("/<string:role_id>", methods=["POST"])
def create_user(role_id):
    body = request.get_json()
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.post(
        url=f"{SECURITY_URL}/users?roleId={role_id}",
        json=body,
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al crear usuario"
        }), 500
    else:
        return jsonify({"response": response.json()}), response.status_code


@user_bp.route("/<string:userid>", methods=["DELETE"])
def delete_user(userid):
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.delete(
        url=f"{SECURITY_URL}/users/{userid}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al borrar usuario"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


@user_bp.route("/<string:userid>", methods=["PUT"])
def update_user(userid):
    body = request.get_json()
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.put(
        url=f"{SECURITY_URL}/users/{userid}",
        headers=headers,
        json=body
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al actualizar el usuario"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


@user_bp.route("/<string:userid>", methods=["GET"])
def get_user(userid):
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.get(
        url=f"{SECURITY_URL}/users/{userid}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al obtener usuarios"
        }), 500
    else:
        return jsonify(response.json()), response.status_code

