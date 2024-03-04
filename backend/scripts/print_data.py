import pandas as pd
from flask import Flask
from models import Commune, Departement
from App import create_app, db  # Adjust this import path to match your project structure
from config.settings import Config  # Assuming you have a Config class in settings

app = create_app(Config)

# Fetch and print data from each table
def print_departments():
    with app.app_context():
        print("Departements in the Database:")
        try:
            departements = db.session.query(Departement).all()
            for dep in departements:
                print(dep)
        except Exception as e:
            print("error fetching department information")

# print("\nCommunes in the Database:")
# communes = session.query(Commune).all()
# for com in communes:
#     print(com)

def print_communes():
    with app.app_context():
        print("Communes in the Database:")
        try:
            communes = db.session.query(Commune).all()
            for com in communes:
                print(com)
        except Exception as e:
            print("error fetching commun information")

# print("\nAffaires in the Database:")
# affaires = session.query(Affaire).all()
# for aff in affaires:
#     print(aff)
if __name__ == '__main__':
    print_departments()
    print("\n\n\n-------------------------------------------------------------------------------------------\n\n\n")
    print_communes()