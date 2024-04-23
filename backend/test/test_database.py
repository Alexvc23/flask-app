import unittest
import pandas as pd

# Importing models from your application
from models import User, Affaire, Location, Departement, Commune

from sqlalchemy.exc import SQLAlchemyError, IntegrityError # to handle exception 

# Importing test configuration and application setup
from config.settings import TestConfig
from App import create_app, db

# Importing colorama for colored terminal output
from colorama import Fore, Style

# Defining a test class inheriting from unittest.TestCase
class DatabaseConnectionTest(unittest.TestCase):

    # Setting up class-level resources before any tests are run
    @classmethod
    def setUpClass(cls):
        print(f"{Fore.BLUE}Setting up test class...{Style.RESET_ALL}")

        # Creating the Flask application with the test configuration
        cls.app = create_app(TestConfig)
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        # Creating all database tables
        db.create_all() 
        # Printing separator for clarity
        print(f"{Fore.YELLOW}--------------------------------------------------{Style.RESET_ALL}")

    # Tearing down class-level resources after all tests have been run
    @classmethod
    def tearDownClass(cls):
        print(f"{Fore.BLUE}Tearing down test class...{Style.RESET_ALL}")

        # Removing the application context
        # Dropping all database tables
        db.drop_all()
        db.session.remove()
        cls.app_context.pop()

        # Printing separator for clarity
        print(f"{Fore.YELLOW}--------------------------------------------------{Style.RESET_ALL}")

    # ──────────────────────────────────────────────────────────────

    # Setting up resources before each test method
    def setUp(self):
        print(f"{Fore.CYAN}Setting up test...{Style.RESET_ALL}")
        super().setUp()

        # Starting a nested transaction
        db.session.begin_nested()

    # Tearing down resources after each test method
    def tearDown(self):
        print(f"{Fore.CYAN}Tearing down test...{Style.RESET_ALL}")

        # Rolling back the nested transaction to discard changes made during the test
        db.session.rollback()

    # Test method for user creation
    def test_user_creation(self):
        print(f"{Fore.GREEN}Testing user creation...{Style.RESET_ALL}")
        existing_user = User.query.filter_by(username='tony').first()
        if not existing_user:
            test_user = User(username='tony')
            db.session.add(test_user)
            db.session.commit()
            added_user = User.query.filter_by(username='tony').first()
            self.assertIsNotNone(added_user)
            self.assertEqual(added_user.username, 'tony')
        else:
            print(f"{Fore.YELLOW}User already exists, skipping insert.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}--------------------------------------------------{Style.RESET_ALL}")

   # ──────────────────────────────────────────────────────────────

    # Test method for affaire and location creation
    def test_affaire_and_location_creation(self):
        print(f"{Fore.GREEN}Testing affaire and location creation...{Style.RESET_ALL}")

        # Creating a test user
        user = User(username='alex')
        db.session.add(user)
        db.session.commit()

        # Creating a test affaire associated with the user
        affaire = Affaire(nom='alexTest', user=user)
        db.session.add(affaire)
        db.session.commit()

        # Defining test locations data
        locations = [
            {'department': '72', 'commune': 'Aviernoz', 'precision': 'precision1'},
            {'department': '71', 'commune': 'Berzé-le-Châtel', 'precision': 'precision2'}
        ]

        # Iterating over the test locations and creating them
        for loc in locations:
            location = Location(department=loc['department'], commune=loc['commune'], precision=loc['precision'], affaire=affaire)
            db.session.add(location)
        db.session.commit()

        # Querying the added affaire from the database
        added_affaire = Affaire.query.filter_by(nom='alexTest').first()

        # Asserting and printing details
        self.assertIsNotNone(added_affaire)
        self.assertEqual(len(added_affaire.locations), 2)
        self.assertEqual(added_affaire.locations[0].precision, 'precision1')
        self.assertEqual(added_affaire.locations[1].precision, 'precision2')
        print(f"{Fore.YELLOW}Added affaire and locations: {added_affaire}{Style.RESET_ALL}")
        for loc in added_affaire.locations:
            print(f"{Fore.GREEN}Location - Department: {loc.department}, Commune: {loc.commune}, Precision: {loc.precision}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}--------------------------------------------------{Style.RESET_ALL}")

    # Affaire uniqueness with different users
    def test_affaire_uniqueness(self):
        print(f"{Fore.GREEN}Testing affaire uniqueness...{Style.RESET_ALL}")
        user1 = User(username='user1')
        user2 = User(username='user2')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        affaire1 = Affaire(nom='uniqueTest', user=user1)
        affaire2 = Affaire(nom='uniqueTest', user=user2)
        db.session.add(affaire1)
        db.session.add(affaire2)
        db.session.commit()

        # Expect both affaires to be added without issues if uniqueness is scoped to user
        self.assertEqual(Affaire.query.filter_by(nom='uniqueTest').count(), 2)
        print(f"{Fore.YELLOW}Tested uniqueness of affaire name across different users.{Style.RESET_ALL}")

    #single user affaire uniqueness, as the user should have uniqueness contrain in terms of affaire name 
    def test_affaire_uniqueness_within_single_user(self):
        print(f"{Fore.GREEN}Testing affaire uniqueness within a single user...{Style.RESET_ALL}")
        user = User(username='unique_user')
        db.session.add(user)
        db.session.commit()

        # Attempt to create two affaires with the same name for the same user
        affaire1 = Affaire(nom='duplicateTest', user=user)
        affaire2 = Affaire(nom='duplicateTest', user=user)
        db.session.add(affaire1)
        db.session.add(affaire2)

        # Expecting an IntegrityError on commit because of the unique constraint
        with self.assertRaises(IntegrityError):
            db.session.commit()
        print(f"{Fore.YELLOW}Passing by IntegityError after tryting to add the same affaire name with the same user.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Tested uniqueness of affaire name within the same user.{Style.RESET_ALL}")
        db.session.rollback()  # Cleanup after expected failure

        # Checking if there is nothing in the data base as a error was raised and the rollback was applied 
        count = Affaire.query.filter_by(nom='duplicateTest', user_id=user.id).count()
        self.assertEqual(count, 0, "No affaire should be present due to rollback after failed uniqueness test")
        print(f" number of affaires: ${count} with user ${user.username} ")
        print(f"{Fore.YELLOW}--------------------------------------------------{Style.RESET_ALL}")


    # Testing adding multiple users and multiple affaires
    def test_multiple_users_affaires(self):
        print(f"{Fore.GREEN}Testing multiple affaires for different users...{Style.RESET_ALL}")
        users = [User(username='charlie'), User(username='dave')]
        db.session.add_all(users)
        db.session.commit()  # Ensure users are committed before using them

        affaires = [Affaire(nom=f'Project {u.username}', user=u) for u in User.query.all()]  # Fetch fresh from the DB
        db.session.add_all(affaires)
        db.session.commit()

        for a in affaires:
            added = Affaire.query.filter_by(nom=a.nom).first()
            self.assertIsNotNone(added)
            self.assertEqual(added.user.username, a.user.username)
            print(f"{Fore.YELLOW}Added {added.nom} for {added.user.username}{Style.RESET_ALL}")

        print(f"{Fore.YELLOW}--------------------------------------------------{Style.RESET_ALL}")


# Running the tests if this script is executed directly
if __name__ == '__main__':
    unittest.main()
