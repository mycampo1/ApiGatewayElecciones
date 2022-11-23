from flask import request, jsonify, Blueprint
import requests
from settings import VOTES_URL

candidates_bp = Blueprint("candidates_blueprint", __name__)


@candidates_bp.route("", methods=["POST"])
def create_candidates():
    body = request.get_json()
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(
        url=f"{VOTES_URL}/candidates",
        json=body,
        headers=headers
    )
    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:
        return jsonify({
            "message": "Hubo un error al crear el candidato"
        }), 500


@candidates_bp.route("", methods=["GET"])
def candidates():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/candidates",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener los candidatos"
        }), 500


@candidates_bp.route("/<string:candidate_id>", methods=["GET"])
def candidate(candidate_id):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/candidates/{candidate_id}",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener la información del candidato"
        }), 500


@candidates_bp.route("/<string:candidate_id>", methods=["PUT"])
def update_candidate(candidate_id):
    body = request.get_json()
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.put(
        url=f"{VOTES_URL}/candidates/{candidate_id}",
        headers=headers,
        json=body
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al actualizar el candidato"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


@candidates_bp.route("/<string:candidate_id>", methods=["DELETE"])
def delete_candidate(candidate_id):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.delete(
        url=f"{VOTES_URL}/candidates/{candidate_id}",
        headers=headers
    )
    if response.status_code == 404:
        return jsonify({
            "message": "El candidato no existe"
        }), 404
    elif response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al eliminar el candidato. Intente nuevamente"
        }), 500
    else:
        return jsonify({
            "message": "El candidato fue eliminado correctamente"
        }), 200