import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Departement, Commune, Affaire  # Import your models here
from config.settings import DATABASE_URL
from colorama import Fore, Style  # Import colorama for colored output

class DatabaseConnectionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f"{Fore.BLUE}Setting up test class...{Style.RESET_ALL}")
        # Connect to the test database
        cls.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        print(f"{Fore.YELLOW}--------------------------------------------------\n{Style.RESET_ALL}")

    @classmethod
    def tearDownClass(cls):
        print(f"{Fore.BLUE}Tearing down test class...{Style.RESET_ALL}")
        # Drop all tables and close the connection
        Base.metadata.drop_all(cls.engine)
        cls.engine.dispose()

        print(f"{Fore.YELLOW}--------------------------------------------------\n{Style.RESET_ALL}")

    def setUp(self):
        print(f"{Fore.CYAN}Setting up test...{Style.RESET_ALL}")
        # Start a new transaction for each test
        self.connection = self.engine.connect()
        self.transaction = self.connection.begin()
        self.session = self.Session(bind=self.connection)

    def tearDown(self):
        print(f"{Fore.CYAN}Tearing down test...{Style.RESET_ALL}")
        # Roll back the transaction and close the connection after each test
        self.session.close()
        self.transaction.rollback()
        self.connection.close()

    def test_departement_creation(self):
        print(f"{Fore.GREEN}Testing department creation...{Style.RESET_ALL}")
        # Use self.session for database operations
        test_departement = Departement(DEP_CODE='01', DEP_NOM='Example Departement')
        self.session.add(test_departement)
        self.session.commit()

        added_departement = self.session.query(Departement).filter_by(DEP_CODE='01').first()
        print(f"{Fore.YELLOW}Added department:{Style.RESET_ALL}", added_departement)
        self.assertIsNotNone(added_departement)
        self.assertEqual(added_departement.DEP_NOM, 'Example Departement')
        print(f"{Fore.YELLOW}--------------------------------------------------\n{Style.RESET_ALL}")

    def test_commune_creation(self):
        print(f"{Fore.GREEN}Testing commune creation...{Style.RESET_ALL}")
        # Test creating a commune with checks for existing departement
        test_departement = self.session.query(Departement).filter_by(DEP_CODE='01').first()
        if not test_departement:
            test_departement = Departement(DEP_CODE='01', DEP_NOM='Example Departement')
            self.session.add(test_departement)
            self.session.commit()
        
        test_commune = Commune(COM_CODE='01001', COM_NOM='Example Commune', DEP_CODE='01')
        self.session.add(test_commune)
        self.session.commit()

        added_commune = self.session.query(Commune).filter_by(COM_CODE='01001').first()
        print(f"{Fore.YELLOW}Added commune:{Style.RESET_ALL}", added_commune)
        self.assertIsNotNone(added_commune)
        self.assertEqual(added_commune.COM_NOM, 'Example Commune')
        print(f"{Fore.YELLOW}--------------------------------------------------\n{Style.RESET_ALL}")

    def test_affaire_creation(self):
        print(f"{Fore.GREEN}Testing affaire creation...{Style.RESET_ALL}")
        # Ensure necessary Departement exists
        departement = self.session.query(Departement).filter_by(DEP_CODE='01').first()
        if not departement:
            departement = Departement(DEP_CODE='01', DEP_NOM='Example Departement')
            self.session.add(departement)
            self.session.commit()

        # Ensure necessary Commune exists
        commune = self.session.query(Commune).filter_by(COM_CODE='01001').first()
        if not commune:
            commune = Commune(COM_CODE='01001', COM_NOM='Example Commune', DEP_CODE='01')
            self.session.add(commune)
            self.session.commit()

        # Now, create the Affaire instance
        affaire = Affaire(Nom='Example Affaire', DEP_CODE='01', COM_CODE='01001', Precision='Example Details')
        self.session.add(affaire)
        self.session.commit()  # This should now work, as required foreign keys exist

        # Verify the Affaire was added
        added_affaire = self.session.query(Affaire).filter_by(Nom='Example Affaire').first()
        print(f"{Fore.YELLOW}Added affaire:{Style.RESET_ALL}", added_affaire)
        self.assertIsNotNone(added_affaire)
        self.assertEqual(added_affaire.Precision, 'Example Details')
        print(f"{Fore.YELLOW}--------------------------------------------------\n{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()
