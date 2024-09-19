from db import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(80), nullable=False)
    team = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(80), nullable=False)
    season = db.Column(db.String(80), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    games = db.Column(db.Integer, nullable=False)
    two_percent = db.Column(db.Integer, nullable=False)
    three_percent = db.Column(db.Integer, nullable=False)
    atr = db.Column(db.Integer, nullable=False)
    ppg_ratio = db.Column(db.Integer, nullable=False)

    def get_dict(self):
        return {
            'id': self.id,
            'player_name': self.player_name,
            'team': self.team,
            'position': self.position,
            'season': self.season,
            'points': self.points,
            'games': self.games,
            'two_percent': self.two_percent,
            'three_percent': self.three_percent,
            'atr': self.atr,
            'ppg_ratio': self.ppg_ratio,
        }