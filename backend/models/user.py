# # Define each of your models in separate files within the models directory. For example, 
# put the User class in a file named user.py. This keeps each model encapsulated in its own space 
# and makes your codebase more organized.

# /backend/models/user.py:
from sqlalchemy import Column, Integer, String
from .base import Base  # Import Base from base.py

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
