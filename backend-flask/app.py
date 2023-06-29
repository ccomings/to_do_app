from flask import Flask
import os
from sqlalchemy import create_engine, MetaData, select
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

engine = create_engine("postgresql://postgres:postgres@db:5432/postgres")
metadata = MetaData()
metadata.reflect(engine, only=['todos_todo'])
Base = automap_base(metadata=metadata)
Base.prepare()
Todo = Base.classes.todos_todo
session = Session(engine)

@app.route("/")
def index():
	todos = session.query(Todo).all()
	response = ["----" + todo.text + '\n' for todo in todos]
	return " ".join(response)

if __name__ == '__main__':
	app.run(debug = True, host='0.0.0.0', port=8000)
