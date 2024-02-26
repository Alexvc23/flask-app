import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Departement, Commune, Affaire  # Import your models here
from config.settings import DATABASE_URL
from scripts.initialize_db import initialize_db

# Set up database connection
engine = create_engine(DATABASE_URL)
initialize_db()
Session = sessionmaker(bind=engine)

session = Session()

# Fetch and print data from each table
print("Departements in the Database:")
departements = session.query(Departement).all()
for dep in departements:
    print(dep)

print("\nCommunes in the Database:")
communes = session.query(Commune).all()
for com in communes:
    print(com)

print("\nAffaires in the Database:")
affaires = session.query(Affaire).all()
for aff in affaires:
    print(aff)

session.close()
