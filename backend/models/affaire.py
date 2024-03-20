from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from .base import db

# Define a class named 'Affaire' that represents a table in the database.
class Affaire(db.Model):
    # Define the name of the table in the database.
    __tablename__ = 'affaires'
    
    # Define the columns of the table.
    # 'ID' column represents the primary key of the table.
    ID = Column(Integer, primary_key=True, autoincrement=True)
    
    # 'Nom' column represents the name of the affair. It is a string column and cannot be null.
    Nom = Column(String, nullable=False)
    
    # 'DEP_CODE' column represents the department code associated with the affair.
    # It is a string column and is linked to the 'DEP_CODE' column of the 'departements' table as a foreign key.
    DEP_CODE = Column(String, ForeignKey('departements.DEP_CODE'))
    
    # 'COM_CODE' column represents the commune code associated with the affair.
    # It is a string column and is linked to the 'COM_CODE' column of the 'communes' table as a foreign key.
    COM_CODE = Column(String, ForeignKey('communes.COM_CODE'))
    
    # 'Precision' column represents additional details or precision about the affair.
    # It is a text column.
    Precision = Column(Text)
    
    # Define relationships to other tables.
    # 'departement' relationship defines a many-to-one relationship with the 'Departement' table.
    departement = relationship("Departement")
    
    # 'commune' relationship defines a many-to-one relationship with the 'Commune' table.
    commune = relationship("Commune")


    def __repr__(self):
        return f"<Affaire(Nom='{self.Nom}', DEP_CODE='{self.DEP_CODE}', COM_CODE='{self.COM_CODE}', Precision='{self.Precision}')>"