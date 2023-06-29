from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def index():
	return "Hello World!!!!!"

if __name__ == '__main__':
	app.run(debug = True, host='0.0.0.0', port=8000)
