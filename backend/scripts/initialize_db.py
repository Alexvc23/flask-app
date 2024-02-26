from sqlalchemy import create_engine
from models import Base  # Import the Base from your models
from config.settings import DATABASE_URL  # Import your database URL from the settings

def initialize_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
