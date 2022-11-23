from flask import request, jsonify, Blueprint
import requests
from settings import VOTES_URL

votes_bp = Blueprint("votes_blueprint", __name__)


@votes_bp.route("", methods=["POST"])
def create_votes():
    body = request.get_json()
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(
        url=f"{VOTES_URL}/votes",
        json=body,
        headers=headers
    )
    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:
        return jsonify({
            "message": "Hubo un error al crear el voto"
        }), 500


@votes_bp.route("", methods=["GET"])
def votes():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/votes",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener los votos"
        }), 500


@votes_bp.route("/<string:vote_id>", methods=["GET"])
def vote(vote_id):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/votes/{vote_id}",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener la información de los votos"
        }), 500


@votes_bp.route("/<string:vote_id>", methods=["PUT"])
def update_vote(vote_id):
    body = request.get_json()
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.put(
        url=f"{VOTES_URL}/votes/{vote_id}",
        headers=headers,
        json=body
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al actualizar el voto"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


@votes_bp.route("/<string:vote_id>", methods=["DELETE"])
def delete_vote(vote_id):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.delete(
        url=f"{VOTES_URL}/votes/{vote_id}",
        headers=headers
    )
    if response.status_code == 404:
        return jsonify({
            "message": "El voto no existe"
        }), 404
    elif response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al eliminar el voto. Intente nuevamente"
        }), 500
    else:
        return jsonify({
            "message": "El voto fue eliminada correctamente"
        }), 200