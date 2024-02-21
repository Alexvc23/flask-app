from dotenv import load_dotenv  # Importing the load_dotenv function from the dotenv module
import os  # Importing the os module for interacting with the operating system

# Load environment variables from .env file
load_dotenv()  # Calling the load_dotenv function to load environment variables from a .env file

# Database settings

# Retrieving the value of the environment variable 'POSTGRES_USER', defaulting to 'default_user' if not set
POSTGRES_USER = os.getenv('POSTGRES_USER', 'default_user')

# Retrieving the value of the environment variable 'POSTGRES_PASSWORD', defaulting to 'default_password' if not set
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'default_password')

# Retrieving the value of the environment variable 'POSTGRES_DB', defaulting to 'default_db' if not set
POSTGRES_DB = os.getenv('POSTGRES_DB', 'default_db')

# Retrieving the value of the environment variable 'POSTGRES_HOST', defaulting to 'localhost' if not set
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')

# Constructing the DATABASE_URL string using the retrieved environment variables
DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}'
