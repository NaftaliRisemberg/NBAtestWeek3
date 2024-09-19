from sqlalchemy import false
from db import db

class PlayerAPI(db.Model):
    def __init__(self, id, player_name, position, age, games, games_started, minutesPg, field_goals,
                 field_attempts, field_percent, threeFg, three_attempts, three_percent, twoFg, two_attempts,
                 two_percent, effectFg_percent, ft_percent, offensiveRb, defensiveRb, totalRb,
                 assists, steals, blocks, turnovers, personal_fouls, points,
                 team, season, player_id):
        id = db.Column(db.Integer, primary_key=True)
        player_name = db.Column(db.String(50), unique=False, nullable=False)
        position = db.Column(db.String(50), unique=False, nullable=False)
        age = db.Column(db.Integer, nullable=False)
        games = db.Column(db.Integer, nullable=False)
        games_started = db.Column(db.Integer, nullable=False)
        minutesPg = db.Column(db.Float, nullable=False)
        field_goals = db.Column(db.Integer, nullable=False)
        field_attempts = db.Column(db.Integer, nullable=False)
        field_percent = db.Column(db.Float, nullable=False)
        threeFg = db.Column(db.Integer, nullable=False)
        three_attempts = db.Column(db.Integer, nullable=False)
        three_percent = db.Column(db.Float, nullable=False)
        twoFg = db.Column(db.Float, nullable=False)
        two_attempts = db.Column(db.Integer, nullable=False)
        two_percent = db.Column(db.Float, nullable=False)
        effectFg_percent = db.Column(db.Float, nullable=False)
        ft_percent = db.Column(db.Float, nullable=False)
        offensiveRb = db.Column(db.Integer, nullable=False)
        defensiveRb = db.Column(db.Integer, nullable=False)
        totalRb = db.Column(db.Integer, nullable=False)
        assists = db.Column(db.Integer, nullable=False)
        steals = db.Column(db.Integer, nullable=False)
        blocks = db.Column(db.Integer, nullable=False)
        turnovers = db.Column(db.Integer, nullable=False)
        personal_fouls = db.Column(db.Integer, nullable=False)
        points = db.Column(db.Integer, nullable=False)
        team = db.Column(db.String(50), unique=False, nullable=False)
        season = db.Column(db.String(50), unique=False, nullable=False)
        player_id = db.Column(db.String(50), unique=True, nullable=False)

    def get_dict(self):
        return {
        'id': self.id,
        'player_name': self.player_name,
        'position' : self.position,
        'age': self.age,
        'games': self.games,
        'games_started': self.games_started,
        'minutesPg': self.minutesPg,
        'field_goals': self.field_goals,
        'field_attempts': self.field_attempts,
        'field_percent': self.field_percent,
        'threeFg': self.threeFg,
        'three_attempts': self.three_attempts,
        'three_percent': self.three_percent,
        'twoFg': self.twoFg,
        'two_attempts': self.two_attempts,
        'two_percent': self.two_percent,
        'effectFg_percent': self.effectFg_percent,
        'ft_percent': self.ft_percent,
        'offensiveRb': self.offensiveRb,
        'defensiveRb': self.defensiveRb,
        'totalRb': self.totalRb,
        'assists': self.assists,
        'steals': self.steals,
        'blocks': self.blocks,
        'turnovers': self.turnovers,
        'personal_fouls': self.personal_fouls,
        'points': self.points,
        'team': self.team,
        'season': self.season,
        'player_id': self.player_id}

    def __iter__(self):
        return self

