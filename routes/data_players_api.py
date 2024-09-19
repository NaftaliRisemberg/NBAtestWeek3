from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from models.player_api import PlayerAPI

players_api__bp = Blueprint('players_api', __name__)

@players_api__bp.route('/create', methods=['POST'])
def create_player():
    pass
