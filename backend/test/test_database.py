import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User  # Import your models here
from config.settings import DATABASE_URL

class DatabaseConnectionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Connect to the test database
        cls.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    @classmethod
    def tearDownClass(cls):
        # Drop all tables and close the connection
        Base.metadata.drop_all(cls.engine)
        cls.engine.dispose()

    def test_user_creation(self):
        # Test creating a user
        session = self.Session()
        test_user = User(username='testuser', email='testuser@example.com')
        session.add(test_user)
        session.commit()

        # Verify the user was added
        added_user = session.query(User).filter_by(username='testuser').first()
        self.assertIsNotNone(added_user)
        self.assertEqual(added_user.email, 'testuser@example.com')

        session.close()

if __name__ == '__main__':
    unittest.main()
