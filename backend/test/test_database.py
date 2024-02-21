import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Departement, Commune, Affaire  # Import your models here
from config.settings import DATABASE_URL

class DatabaseConnectionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Connect to the test database
        cls.engine = create_engine(DATABASE_URL)  # Create an engine to connect to the database
        Base.metadata.create_all(cls.engine)  # Create all the tables defined in the Base class
        cls.Session = sessionmaker(bind=cls.engine)  # Create a session maker bound to the engine

    @classmethod
    def tearDownClass(cls):
        # Drop all tables and close the connection
        Base.metadata.drop_all(cls.engine)  # Drop all the tables
        cls.engine.dispose()  # Close the connection to the database

    def test_departement_creation(self):
        # Test creating a departement
        session = self.Session()  # Create a new session
        test_departement = Departement(DEP_CODE='01', DEP_NOM='Example Departement')  # Create a new Departement object
        session.add(test_departement)  # Add the departement object to the session
        session.commit()  # Commit the transaction to persist the changes to the database

        # Verify the departement was added
        added_departement = session.query(Departement).filter_by(DEP_CODE='01').first()  # Query the database for the added departement
        self.assertIsNotNone(added_departement)  # Assert that the added departement is not None (i.e., exists)
        self.assertEqual(added_departement.DEP_NOM, 'Example Departement')  # Assert that the departement's name matches the expected value

        session.close()  # Close the session after the test is completed

    def test_commune_creation(self):
        # Test creating a commune
        session = self.Session()  # Create a new session
        test_commune = Commune(COM_CODE='01001', COM_NOM='Example Commune', DEP_CODE='01')  # Create a new Commune object
        session.add(test_commune)  # Add the commune object to the session
        session.commit()  # Commit the transaction to persist the changes to the database

        # Verify the commune was added
        added_commune = session.query(Commune).filter_by(COM_CODE='01001').first()  # Query the database for the added commune
        self.assertIsNotNone(added_commune)  # Assert that the added commune is not None (i.e., exists)
        self.assertEqual(added_commune.COM_NOM, 'Example Commune')  # Assert that the commune's name matches the expected value

        session.close()  # Close the session after the test is completed

    def test_affaire_creation(self):
        # Test creating an affaire
        session = self.Session()  # Create a new session
        test_affaire = Affaire(Nom='Example Affaire', DEP_CODE='01', COM_CODE='01001', Precision='Example Details')  # Create a new Affaire object
        session.add(test_affaire)  # Add the affaire object to the session
        session.commit()  # Commit the transaction to persist the changes to the database

        # Verify the affaire was added
        added_affaire = session.query(Affaire).filter_by(Nom='Example Affaire').first()  # Query the database for the added affaire
        self.assertIsNotNone(added_affaire)  # Assert that the added affaire is not None (i.e., exists)
        self.assertEqual(added_affaire.Precision, 'Example Details')  # Assert that the affaire's precision matches the expected value

        session.close()  # Close the session after the test is completed

if __name__ == '__main__':
    unittest.main()  # Run the tests
