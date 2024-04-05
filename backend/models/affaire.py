# Import necessary modules
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

# Import database instance
from .base import db

# Define the Affaire model
class Affaire(db.Model):
    # Set table name
    __tablename__ = 'affaires'

    # Define columns
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Nom = Column(String, nullable=False)
    DEP_CODE = Column(String, ForeignKey('departements.DEP_CODE'))
    COM_CODE = Column(String, ForeignKey('communes.COM_CODE'))
    Precision = Column(Text)
    
    # Define foreign key to link to the User model
    user_id = Column(Integer, ForeignKey('users.id'))
    
    # Define relationships
    departement = relationship("Departement")
    commune = relationship("Commune")
    
    # Define the back relationship to User
    user = relationship("User", back_populates="affaires")

    # Define representation of the object
    def __repr__(self):
        return f"<Affaire(Nom='{self.Nom}', DEP_CODE='{self.DEP_CODE}', COM_CODE='{self.COM_CODE}', Precision='{self.Precision}', UserID='{self.user_id}')>"
