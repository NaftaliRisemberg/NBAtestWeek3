from flask import Blueprint, jsonify, request
from models.player import Player
from db import db

player_bp = Blueprint('player', __name__, url_prefix='/api/players')

@player_bp.route('?position={position}&season={season} ', methods=['GET'])
def get_players(position, season):
    pass
