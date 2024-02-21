from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database settings
POSTGRES_USER = os.getenv('POSTGRES_USER', 'default_user')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'default_password')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'default_db')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DB}'

