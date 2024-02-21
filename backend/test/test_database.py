import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User  # Import your models here
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

    def test_user_creation(self):
        # Test creating a user
        session = self.Session()  # Create a new session
        test_user = User(username='testuser', email='testuser@example.com')  # Create a new user object
        session.add(test_user)  # Add the user object to the session
        session.commit()  # Commit the transaction to persist the changes to the database

        # Verify the user was added
        added_user = session.query(User).filter_by(username='testuser').first()  # Query the database for the added user
        self.assertIsNotNone(added_user)  # Assert that the added user is not None (i.e., exists)
        self.assertEqual(added_user.email, 'testuser@example.com')  # Assert that the user's email matches the expected value

        session.close()  # Close the session after the test is completed

if __name__ == '__main__':
    unittest.main()  # Run the tests
