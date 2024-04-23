# Importing necessary modules for defining the model
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

# Importing the database instance
from .base import db

# Define the User model, inheriting from db.Model which represents a table in the database
class User(db.Model):
    # Defining columns for the User table
    id = Column(Integer, primary_key=True)  # Primary key column for uniquely identifying each User
    username = Column(String(50), unique=True, nullable=False)  # Column to store the username, must be unique and cannot be null

    # Defining a relationship with the Affaire model, each User can have multiple affaires
    affaires = relationship('Affaire', backref='user', lazy=True, cascade="all, delete-orphan")

