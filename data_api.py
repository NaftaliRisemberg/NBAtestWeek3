import requests
from app import app
from db import db
from models.player import Player

BASE_URL = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season='
END_URL = '&&pageSize=1000'
def get_season_data_players(season: int):
    response = requests.get(f'{BASE_URL}{season}{END_URL}')
    response_json = response.json()
    return response_json

def insert_players(api_json):
    with app.app_context():
        for player in api_json:
            new_player = Player(
                player_name=player['playerName'],
                position=player['position'],
                age=player['age'],
                games=player['games'],
                games_started=player['gamesStarted'],
                minutesPg=player['minutesPg'],
                field_goals=player['fieldGoals'],
                field_attempts=player['fieldAttempts'],
                field_percent=player['fieldPercent'],
                threeFg=player['threeFg'],
                three_attempts=player['threeAttempts'],
                three_percent=player['threePercent'],
                twoFg=player['twoFg'],
                two_attempts=player['twoAttempts'],
                two_percent=player['twoPercent'],
                effectFg_percent=player['effectFgPercent'],
                ft_percent=player['ftPercent'],
                offensiveRb=player['offensiveRb'],
                defensiveRb=player['defensiveRb'],
                totalRb=player['totalRb'],
                assists=player['assists'],
                steals=player['steals'],
                blocks=player['blocks'],
                turnovers=player['turnovers'],
                personal_fouls=player['personalFouls'],
                points=player['points'],
                team=player['team'],
                season=player['season'],
                player_id=player['playerId']
            )
            db.session.add(new_player)
        db.session.commit()
    return "player data inserted successfully"

season_2022 = get_season_data_players(2024)
season_2023 = get_season_data_players(2023)
season_2024 = get_season_data_players(2024)
insert_players(season_2022)
insert_players(season_2023)
insert_players(season_2024)
