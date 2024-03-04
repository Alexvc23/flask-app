import pandas as pd
from flask import Flask
from models import Commune, Departement
from App import create_app, db  # Adjust this import path to match your project structure
from config.settings import Config  # Assuming you have a Config class in settings

# Initialize Flask app using the application factory pattern
app = create_app(Config)

# Function to add departement
def add_departement(dep_code, dep_nom):
    with app.app_context():
        exist_dep = db.session.query(Departement).filter_by(DEP_CODE=dep_code).first()
        if not exist_dep:
            new_dep = Departement(DEP_CODE=dep_code, DEP_NOM=dep_nom)
            db.session.add(new_dep)
            db.session.commit()
            return new_dep
        return exist_dep

# Function to add commune
def add_commune(com_code, com_nom, dep_code):
    with app.app_context():
        exist_com = db.session.query(Commune).filter_by(COM_CODE=com_code).first()
        if not exist_com:
            departement = add_departement(dep_code, '')  # Assumes departement name isn't necessary here
            new_com = Commune(COM_CODE=com_code, COM_NOM=com_nom, DEP_CODE=dep_code)
            db.session.add(new_com)
            db.session.commit()
            return new_com
        return exist_com

# Main function to load data into the database
def load_data(dataframe):
    with app.app_context():
        for _, row in dataframe.iterrows():
            try:
                add_departement(row['DEP_CODE'], row['DEP_NOM'])
                add_commune(row['COM_CODE'], row['COM_NOM'], row['DEP_CODE'])
            except Exception as e:  # Catch broader exceptions or use specific ones as per your requirements
                print(f"Error adding row {row}: {e}")
                db.session.rollback()


# Execute loading process
if __name__ == '__main__':
    # Read CSV data
    with app.app_context():
        df = pd.read_csv('/Users/alex/Documents/programing/flask-app-alex/backend/data/copy-data.csv', dtype={'DEP_CODE': str, 'COM_CODE': str})
        load_data(df)
