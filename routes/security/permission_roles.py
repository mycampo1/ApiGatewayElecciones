from flask import request, jsonify, Blueprint
import requests
from settings import SECURITY_URL

permissions_roles_bp = Blueprint("permission_roles_blueprint", __name__)


@permissions_roles_bp.route("/<string:permission_role_id>", methods=["DELETE"])
def delete_permission_role(permission_role_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.delete(
        url=f"{SECURITY_URL}/permissions-roles/{permission_role_id}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al borrar el acceso"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


@permissions_roles_bp.route("/<string:permission_role_id>/role/<string:role_id>", methods=["PUT"])
def change_role_to_permission(permission_role_id, role_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.put(
        url=f"{SECURITY_URL}/permissions-roles/{permission_role_id}/role/{role_id}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al cambiar el rol al acceso"
        }), 500
    else:
        return jsonify(response.json()), response.status_code

@permissions_roles_bp.route("/<string:permission_role_id>/permission/<string:permission_id>", methods=["PUT"])
def change_permission_to_permission(permission_role_id, permission_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.put(
        url=f"{SECURITY_URL}/permissions-roles/{permission_role_id}/permission/{permission_id}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al cambiar el permiso al acceso"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


@permissions_roles_bp.route("/role/<string:role_id>/permission/<string:permission_id>", methods=["POST"])
def create_permission_role(role_id, permission_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.post(
        url=f"{SECURITY_URL}/permissions-roles/role/{role_id}/permission/{permission_id}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al crear el acceso"
        }), 500
    else:
        return jsonify(response.json()), response.status_code

@permissions_roles_bp.route("", methods=["GET"])
def permission_role():
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.get(
        url=f"{SECURITY_URL}/permissions-roles",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al obtener la información de los permisos"
        }), 500
    else:
        return jsonify(response.json()), response.status_code

@permissions_roles_bp.route("/role/<string:role_id>", methods=["GET"])
def get_role_permission_rol(role_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.get(
        url=f"{SECURITY_URL}/permissions-roles/role/{role_id}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al obtener la información de los permisos del rol"
        }), 500
    else:
        return jsonify(response.json()), response.status_code

@permissions_roles_bp.route("/permission/<string:permission_id>", methods=["GET"])
def get_permission_permission_rol(permission_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.get(
        url=f"{SECURITY_URL}/permissions-roles/permission/{permission_id}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al obtener la información de los permisos del rol desde permisos"
        }), 500
    else:
        return jsonify(response.json()), response.status_code
