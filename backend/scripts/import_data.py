import sys
sys.path.append('/Users/alex/Documents/programming/flask-app-alex/backend')

# Import necessary libraries
import pandas as pd  # Pandas is a popular library for data manipulation and analysis
from sqlalchemy import create_engine, exc  # SQLAlchemy is a toolkit for SQL databases in Python
from sqlalchemy.orm import sessionmaker  # SQLAlchemy sessionmaker is used to create sessions
from models import Base, Commune, Departement
from scripts.initialize_db import initialize_db
from config.settings import DATABASE_URL  # Import database connection settings

# Set up database connection
engine = create_engine(DATABASE_URL)  # Create a database engine using the connection URL

initialize_db()

Session = sessionmaker(bind=engine)  # Create a session class bound to the engine

# Read CSV data
df = pd.read_csv('/Users/alex/Documents/programing/flask-app-alex/backend/data/copy-data.csv', dtype={'DEP_CODE': str, 'COM_CODE': str})

# Function to check and add departement
def add_departement(session, dep_code, dep_nom):
    # Check if the department already exists in the database
    exist_dep = session.query(Departement).filter_by(DEP_CODE=dep_code).first()
    if not exist_dep:  # If department doesn't exist, add it to the session
        new_dep = Departement(DEP_CODE=dep_code, DEP_NOM=dep_nom)  # Create a new department object
        session.add(new_dep)  # Add the new department to the session
        return new_dep  # Return the newly added department
    return exist_dep  # If department already exists, return the existing department

# Function to check and add commune
def add_commune(session, com_code, com_nom, dep_code):
    # Check if the commune already exists in the database
    exist_com = session.query(Commune).filter_by(COM_CODE=com_code).first()
    if not exist_com:  # If commune doesn't exist, add it to the session
        # Ensure the department exists or add it
        departement = add_departement(session, dep_code, '')  # Add or retrieve department
        new_com = Commune(COM_CODE=com_code, COM_NOM=com_nom, DEP_CODE=dep_code)  # Create a new commune object
        session.add(new_com)  # Add the new commune to the session
        return new_com  # Return the newly added commune
    return exist_com  # If commune already exists, return the existing commune

# Main function to load data into the database
def load_data(session, dataframe):
    # Iterate through the dataframe row by row
    for _, row in dataframe.iterrows():
        try:
            # Add department and commune from each row
            dep = add_departement(session, row['DEP_CODE'], row['DEP_NOM'])  # Add department
            com = add_commune(session, row['COM_CODE'], row['COM_NOM'], row['DEP_CODE'])  # Add commune

            # Commit after each row or batch for performance - adjust based on your data size
            session.commit()  # Commit the transaction to the database
        except exc.SQLAlchemyError as e:
            print(f"Error adding row {row}: {e}")  # Print error message if an error occurs
            session.rollback()  # Rollback the session on error

# Execute loading process
with Session() as session:  # Open a session
    load_data(session, df)  # Call the load_data function to load data into the database
    session.close()  # Close the session after the process completes
