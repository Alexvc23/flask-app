from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.settings import Config
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

# Initialize Migrate
migrate = Migrate(app, db)

# Import models to ensure they're known to SQLAlchemy
from models import Departement, Commune, Affaire, User

# Additional setup like route import can go here
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')  # Remember to turn off debug mode in production
