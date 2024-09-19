from flask import Blueprint, jsonify, request
from services.player_service import *
from models.player import Player
from sqlalchemy import and_


player_bp = Blueprint('player', __name__, url_prefix='/api/players')

@player_bp.route('position/<string:position>/<int:season>', methods=['GET'])
def get_players(position, season):
    players = Player.query.all()
    data = list(filter(lambda player: player.position == position and
                                      player.season == season, players))
    players_list = [player.get_dict() for player in data]
    return jsonify(players_list)
