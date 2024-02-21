
from sqlalchemy import Column, String
from .base import Base

class Departement(Base):
    __tablename__ = 'departements'
    DEP_CODE = Column(String, primary_key=True)
    DEP_NOM = Column(String, nullable=False)