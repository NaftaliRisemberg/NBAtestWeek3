from db import db

class Player(db.Model):
    __tablename__ = 'players_all_data'
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(50))
    position = db.Column(db.String(50))
    age = db.Column(db.Integer)
    games = db.Column(db.Integer)
    games_started = db.Column(db.Integer)
    minutesPg = db.Column(db.Float)
    field_goals = db.Column(db.Integer)
    field_attempts = db.Column(db.Integer)
    field_percent = db.Column(db.Float)
    threeFg = db.Column(db.Integer)
    three_attempts = db.Column(db.Integer)
    three_percent = db.Column(db.Float)
    twoFg = db.Column(db.Float)
    two_attempts = db.Column(db.Integer)
    two_percent = db.Column(db.Float)
    effectFg_percent = db.Column(db.Float)
    ft_percent = db.Column(db.Float)
    offensiveRb = db.Column(db.Integer)
    defensiveRb = db.Column(db.Integer)
    totalRb = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    steals = db.Column(db.Integer)
    blocks = db.Column(db.Integer)
    turnovers = db.Column(db.Integer)
    personal_fouls = db.Column(db.Integer)
    points = db.Column(db.Integer)
    team = db.Column(db.String(50))
    season = db.Column(db.String(50))
    player_id = db.Column(db.String(50))

    def get_dict(self):
        return {
            'id': self.id,
            'player_name': self.player_name,
            'position': self.position,
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
            'player_id': self.player_id,
        }
