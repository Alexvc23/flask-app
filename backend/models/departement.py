
from .base import db

class Departement(db.Model):
    __tablename__ = 'departements'
    DEP_CODE = db.Column(db.String, primary_key=True)
    DEP_NOM = db.Column(db.String, nullable=False)

    def __repr__(self):
            return f"<Departement(DEP_CODE='{self.DEP_CODE}', DEP_NOM='{self.DEP_NOM}')>"
