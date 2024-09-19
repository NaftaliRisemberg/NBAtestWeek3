from flask import Flask, Blueprint
from db import db
from routes.players_route import player_bp
from routes.teams_route import team_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///players.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
app.register_blueprint(player_bp)
app.register_blueprint(team_bp)

if __name__ == '__main__':
    app.run(debug=True)
