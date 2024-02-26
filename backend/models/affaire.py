from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from .base import Base

class Affaire(Base):
    __tablename__ = 'affaires'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Nom = Column(String, nullable=False)
    DEP_CODE = Column(String, ForeignKey('departements.DEP_CODE'))
    COM_CODE = Column(String, ForeignKey('communes.COM_CODE'))
    Precision = Column(Text)
    departement = relationship("Departement")
    commune = relationship("Commune")

    def __repr__(self):
        return f"<Affaire(Nom='{self.Nom}', DEP_CODE='{self.DEP_CODE}', COM_CODE='{self.COM_CODE}', Precision='{self.Precision}')>"