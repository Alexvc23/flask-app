from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from .departement import Departement
from .base import Base

""" Commune
 * COM_CODE: Unique code for the commune (e.g., '40090' for Boursieres)
 * COM_NOM : Name of the commune (e.g., Boursireres)
 * DEP_CODE: ForeignKey linking the department """

class Commune(Base):
    __tablename__ = 'communes'
    COM_CODE = Column(String, primary_key=True)
    COM_NOM = Column(String, nullable=False)
    DEP_CODE = Column(String, ForeignKey('departements.DEP_CODE'))
    departement = relationship("Departement")

    def __repr__(self):
            return f"<Commune(COM_CODE='{self.COM_CODE}', COM_NOM='{self.COM_NOM}', DEP_CODE='{self.DEP_CODE}')>"
