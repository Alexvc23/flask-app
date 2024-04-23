# Importing necessary modules for defining the model
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.schema import UniqueConstraint

# Importing the database instance
from .base import db

# Defining the Affaire model, inheriting from db.Model which represents a table in the database
class Affaire(db.Model):
    # Defining columns for the Affaire table
    id = db.Column(db.Integer, primary_key=True)  # Primary key column for uniquely identifying each Affaire
    nom = db.Column(db.String(100), nullable=False)  # Column to store the name of the Affaire, cannot be null
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key column referencing the User table, cannot be null

    # Defining a relationship with the Location model, each Affaire can have multiple locations
    locations = db.relationship('Location', backref='affaire', lazy=True, cascade="all, delete-orphan")

    # Defining additional table constraints, in this case, a unique constraint on 'nom' and 'user_id' combination
    __table_args__ = (
        UniqueConstraint('nom', 'user_id', name='uix_nom_user_id'),  # Ensures that each (nom, user_id) combination is unique
    )
