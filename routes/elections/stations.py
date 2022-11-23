from flask import request, jsonify, Blueprint
import requests
from settings import VOTES_URL

stations_bp = Blueprint("stations_blueprint", __name__)


@stations_bp.route("", methods=["POST"])
def create_stations():
    body = request.get_json()
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(
        url=f"{VOTES_URL}/stations",
        json=body,
        headers=headers
    )
    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:
        return jsonify({
            "message": "Hubo un error al crear la mesa"
        }), 500


@stations_bp.route("", methods=["GET"])
def stations():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/stations",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener las mesas"
        }), 500


@stations_bp.route("/<string:station_id>", methods=["GET"])
def station(station_id):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/stations/{station_id}",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener la información de la mesa"
        }), 500


@stations_bp.route("/<string:station_id>", methods=["PUT"])
def update_station(station_id):
    body = request.get_json()
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.put(
        url=f"{VOTES_URL}/stations/{station_id}",
        headers=headers,
        json=body
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al actualizar el candidato"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


@stations_bp.route("/<string:station_id>", methods=["DELETE"])
def delete_station(station_id):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.delete(
        url=f"{VOTES_URL}/stations/{station_id}",
        headers=headers
    )
    if response.status_code == 404:
        return jsonify({
            "message": "La mesa no existe"
        }), 404
    elif response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al eliminar la mesa. Intente nuevamente"
        }), 500
    else:
        return jsonify({
            "message": "la mesa fue eliminada correctamente"
        }), 200