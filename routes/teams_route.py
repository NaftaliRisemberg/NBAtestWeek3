from flask import Blueprint, jsonify, request
from models.teams import Team
from db import db

team_bp = Blueprint('teams', __name__, url_prefix='/api/teams')

@team_bp.route('/', methods=['POST'])
def create_team():
    pass

@team_bp.route('/api/teams/<team_id> ', methods=['PUT'])
def update_team(team_id):
    pass

@team_bp.route('/api/teams/<team_id>', methods=['DELETE'])
def delete_team(team_id):
    pass

@team_bp.route('/api/teams/<team_id>', methods=['GET'])
def get_team_players(team_id):
    pass

@team_bp.route('/api/teams/compare?team1={team_id}&team2={team_id}&', methods=["GET"])
def compare_teams(team1_id, team2_id):
    pass