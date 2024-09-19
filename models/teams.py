from db import db

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    C = db.Column(db.String(50), unique=True, nullable=False)
    PF = db.Column(db.String(50), unique=True, nullable=False)
    SF = db.Column(db.String(50), unique=True, nullable=False)
    SG = db.Column(db.String(50), unique=True, nullable=False)
    PG = db.Column(db.String(50), unique=True, nullable=False)