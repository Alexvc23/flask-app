# Import necessary modules
# For the User model:
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# Import database instance
from .base import db

# Define the User model
class User(db.Model):
    # Set table name
    __tablename__ = 'users'

    # Define columns
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    
    # Define relationship to Affaire models
    # back_populates is used to establish bidirectional relationship
    affaires = relationship("Affaire", back_populates="user")
