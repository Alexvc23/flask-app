import unittest  # Importing the unittest module for creating test cases
import pandas as pd  # Importing pandas for data manipulation
from models import Departement, Commune, Affaire, User  # Importing database models
from config.settings import TestConfig  # Importing TestConfig for test settings
from App import create_app, db  # Importing create_app function and database instance
from colorama import Fore, Style  # Importing colorama for colored console output

# Define a test case class
class DatabaseConnectionTest(unittest.TestCase):
    """

      ####  #        ##    ####   ####      ####   ####  #    # ###### #  ####  #    # #####    ##   ##### #  ####  #    #
     #    # #       #  #  #      #         #    # #    # ##   # #      # #    # #    # #    #  #  #    #   # #    # ##   #
     #      #      #    #  ####   ####     #      #    # # #  # #####  # #      #    # #    # #    #   #   # #    # # #  #
     #      #      ######      #      #    #      #    # #  # # #      # #  ### #    # #####  ######   #   # #    # #  # #
     #    # #      #    # #    # #    #    #    # #    # #   ## #      # #    # #    # #   #  #    #   #   # #    # #   ##
      ####  ###### #    #  ####   ####      ####   ####  #    # #      #  ####   ####  #    # #    #   #   #  ####  #    #

    """

    # Set up the class (like a constructor in c++)
    @classmethod
    def setUpClass(cls):
        print(f"{Fore.BLUE}Setting up test class...{Style.RESET_ALL}")
        cls.app = create_app(TestConfig)  # Creating the Flask app instance with test settings
        cls.app_context = cls.app.app_context()  # Creating an application context
        cls.app_context.push()  # Pushing the application context
        db.create_all()  # Creating all tables in the database
        print(f"{Fore.YELLOW}--------------------------------------------------{Style.RESET_ALL}")

    # Tear down the class (like a destructor in c++)
    @classmethod
    def tearDownClass(cls):
        print(f"{Fore.BLUE}Tearing down test class...{Style.RESET_ALL}")
        db.session.remove()  # Removing the session
        db.drop_all()  # Dropping all tables from the database
        cls.app_context.pop()  # Popping the application context
        print(f"{Fore.YELLOW}--------------------------------------------------{Style.RESET_ALL}")

# ──────────────────────────────────────────────────────────────────────────────

    """

     ##### ######  ####  #####  ####      ####   ####  #    # ###### #  ####  #    # #####    ##   ##### #  ####  #    #  ####
       #   #      #        #   #         #    # #    # ##   # #      # #    # #    # #    #  #  #    #   # #    # ##   # #
       #   #####   ####    #    ####     #      #    # # #  # #####  # #      #    # #    # #    #   #   # #    # # #  #  ####
       #   #           #   #        #    #      #    # #  # # #      # #  ### #    # #####  ######   #   # #    # #  # #      #
       #   #      #    #   #   #    #    #    # #    # #   ## #      # #    # #    # #   #  #    #   #   # #    # #   ## #    #
       #   ######  ####    #    ####      ####   ####  #    # #      #  ####   ####  #    # #    #   #   #  ####  #    #  ####

    """
    # Set up each individual test. (it is like a constructor for each funtion)
    def setUp(self):
        print(f"{Fore.CYAN}Setting up test...{Style.RESET_ALL}")
        super().setUp()  # Calling the parent class's setUp method
        db.session.begin_nested()  # Starting a nested transaction
        # Commune.query.delete()
        # Departement.query.delete()
        # db.session.commit()  # Make sure the deletions are applied


    # Tear down each individual test (it a desctructor for each function test)
    def tearDown(self):
        print(f"{Fore.CYAN}Tearing down test...{Style.RESET_ALL}")
        db.session.rollback()  # Rolling back the transaction

# ──────────────────────────────────────────────────────────────────────────────
    """

     ##### ######  ####  #####  ####
       #   #      #        #   #
       #   #####   ####    #    ####
       #   #           #   #        #
       #   #      #    #   #   #    #
       #   ######  ####    #    ####

    """
    # Test for user creation
    def test_01_user_creation(self):
        print(f"{Fore.GREEN}Testing user creation...{Style.RESET_ALL}")
        test_user = User(id='1', username='Example username')  # Creating a test user object
        db.session.add(test_user)  # Adding the user to the session
        db.session.commit()  # Committing the session

        added_user = User.query.filter_by(id='1').first()  # Querying for the added user
        print(f"{Fore.YELLOW}Added user: {added_user}{Style.RESET_ALL}")  # Printing added user details
        self.assertIsNotNone(added_user)  # Asserting that the user was added
        self.assertEqual(added_user.username, 'Example username')  # Asserting user name
        print(f"{Fore.YELLOW}--------------------------------------------------{Style.RESET_ALL}")
    # Test for department creation
    def test_02_departement_creation(self):
        print(f"{Fore.GREEN}Testing department creation...{Style.RESET_ALL}")
        test_departement = Departement(DEP_CODE='01', DEP_NOM='Example Departement')  # Creating a test department object
        db.session.add(test_departement)  # Adding the department to the session
        db.session.commit()  # Committing the session

        added_departement = Departement.query.filter_by(DEP_CODE='01').first()  # Querying for the added department
        print(f"{Fore.YELLOW}Added department: {added_departement}{Style.RESET_ALL}")  # Printing added department details
        self.assertIsNotNone(added_departement)  # Asserting that the department was added
        self.assertEqual(added_departement.DEP_NOM, 'Example Departement')  # Asserting department name
        print(f"{Fore.YELLOW}--------------------------------------------------{Style.RESET_ALL}")

    # ──────────────────────────────────────────────────────────────────────────────

    # Test for commune creation
    def test_03_commune_creation(self):
        print(f"{Fore.GREEN}Testing commune creation...{Style.RESET_ALL}")
        departement = Departement.query.filter_by(DEP_CODE='01').first()  # Querying for department with code '01'
        if not departement:
            print(f"{Fore.RED}Departement not found, creating...{Style.RESET_ALL}")
            departement = Departement(DEP_CODE='01', DEP_NOM='Example Departement')  # Creating a new department
            db.session.add(departement)  # Adding the department to the session
            db.session.commit()  # Committing the session

        test_commune = Commune(COM_CODE='01001', COM_NOM='Example Commune', DEP_CODE='01')  # Creating a test commune
        db.session.add(test_commune)  # Adding the commune to the session
        db.session.commit()  # Committing the session

        added_commune = Commune.query.filter_by(COM_CODE='01001').first()  # Querying for the added commune
        print(f"{Fore.YELLOW}Added commune:{Style.RESET_ALL}", added_commune)  # Printing added commune details
        self.assertIsNotNone(added_commune)  # Asserting that the commune was added
        self.assertEqual(added_commune.COM_NOM, 'Example Commune')  # Asserting commune name
        print(f"{Fore.YELLOW}--------------------------------------------------{Style.RESET_ALL}")

    # ──────────────────────────────────────────────────────────────────────────────


    # Test for affaire creation
    def test_04_affaire_creation(self):
        print(f"{Fore.GREEN}Testing affaire creation...{Style.RESET_ALL}")
        departement = Departement.query.filter_by(DEP_CODE='01').first()  # Querying for department with code '01'
        if not departement:
            print(f"{Fore.RED}Departement not found, creating...{Style.RESET_ALL}")
            departement = Departement(DEP_CODE='01', DEP_NOM='Example Departement')  # Creating a new department
            db.session.add(departement)  # Adding the department to the session
            db.session.commit()  # Committing the session

        commune = Commune.query.filter_by(COM_CODE='01001').first()  # Querying for commune with code '01001'
        if not commune:
            print(f"{Fore.RED}Commune not found, creating...{Style.RESET_ALL}")
            commune = Commune(COM_CODE='01001', COM_NOM='Example Commune', DEP_CODE='01')  # Creating a new commune
            db.session.add(commune)  # Adding the commune to the session
            db.session.commit()  # Committing the session

        affaire = Affaire(Nom='Example Affaire', DEP_CODE='01', COM_CODE='01001', Precision='Example Details')  # Creating a test affaire
        db.session.add(affaire)  # Adding the affaire to the session
        db.session.commit()  # Committing the session

        added_affaire = Affaire.query.filter_by(Nom='Example Affaire').first()  # Querying for the added affaire
        print(f"{Fore.YELLOW}Added affaire:{Style.RESET_ALL}", added_affaire)  # Printing added affaire details
        self.assertIsNotNone(added_affaire)  # Asserting that the affaire was added
        self.assertEqual(added_affaire.Precision, 'Example Details')  # Asserting affaire details
        print(f"{Fore.YELLOW}--------------------------------------------------{Style.RESET_ALL}")

    # ──────────────────────────────────────────────────────────────────────────────


# Main entry point
if __name__ == '__main__':
    unittest.main()  # Running the unittests
