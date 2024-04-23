# Importing necessary modules for defining the model
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

# Importing the database instance
from .base import db

# Define the Location model, inheriting from db.Model which represents a table in the database
class Location(db.Model):
    # Defining columns for the Location table
    id = Column(Integer, primary_key=True)  # Primary key column for uniquely identifying each Location
    department = Column(String(50), nullable=False)  # Column to store the department of the location, cannot be null
    commune = Column(String(50), nullable=False)  # Column to store the commune of the location, cannot be null
    precision = Column(Text, nullable=False)  # Column to store precision information about the location, cannot be null

    # Defining a foreign key column referencing the Affaire table, representing the association with an Affaire
    affaire_id = Column(Integer, ForeignKey('affaire.id'), nullable=False)

    # Defining a representation method to provide a string representation of the Location object
    def __repr__(self):
        return f"<Location(id='{self.id}', department='{self.department}', commune='{self.commune}', precision='{self.precision}', affaire_id='{self.affaire_id}')>"
