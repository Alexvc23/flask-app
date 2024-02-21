from flask import Flask
from models import Base, User # Import Base and User to register them with SQLALchemy 
from sqlalchemy import create_engine
from config.settings import DATABASE_URL

app = Flask(__name__)

def create_database_tables():
    engine =  create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

@app.route('/')
def home():
    return "Hello, Flask!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
