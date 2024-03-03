import unittest
import pandas as pd
from models import Departement, Commune, Affaire  # Ensure these are the models configured with Flask-SQLAlchemy
from config.settings import TestConfig  # Import TestConfig for your test settings
from App import create_app, db  # Correct the typo here
from colorama import Fore, Style

class DatabaseConnectionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f"{Fore.BLUE}Setting up test class...{Style.RESET_ALL}")
        cls.app = create_app(TestConfig)  # Use TestConfig here
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()
        print(f"{Fore.YELLOW}--------------------------------------------------{Style.RESET_ALL}")

    @classmethod
    def tearDownClass(cls):
        print(f"{Fore.BLUE}Tearing down test class...{Style.RESET_ALL}")
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()
        print(f"{Fore.YELLOW}--------------------------------------------------{Style.RESET_ALL}")

    def setUp(self):
        print(f"{Fore.CYAN}Setting up test...{Style.RESET_ALL}")
        super().setUp()  # If you have this from extending a base class
        db.session.begin_nested()  # Starts a new transaction
        # Clear data - this is a brute-force approach and typically not necessary with transactional tests
        # Commune.query.delete()
        # Departement.query.delete()
        # db.session.commit()  # Make sure the deletions are applied

    def tearDown(self):
        print(f"{Fore.CYAN}Tearing down test...{Style.RESET_ALL}")
        db.session.rollback()  # Rollback the transaction

    def test_01_departement_creation(self):
        print(f"{Fore.GREEN}Testing department creation...{Style.RESET_ALL}")
        test_departement = Departement(DEP_CODE='01', DEP_NOM='Example Departement')
        db.session.add(test_departement)
        db.session.commit()

        added_departement = Departement.query.filter_by(DEP_CODE='01').first()
        print(f"{Fore.YELLOW}Added department: {added_departement}{Style.RESET_ALL}")
        self.assertIsNotNone(added_departement)
        self.assertEqual(added_departement.DEP_NOM, 'Example Departement')
        print(f"{Fore.YELLOW}--------------------------------------------------{Style.RESET_ALL}")


    # ──────────────────────────────────────────────────────────────────────

    def test_02_commune_creation(self):
        print(f"{Fore.GREEN}Testing commune creation...{Style.RESET_ALL}")
        # Ensure necessary Departement exists first to satisfy foreign key constraints
        departement = Departement.query.filter_by(DEP_CODE='01').first()
        if not departement:
            print(f"{Fore.RED}Departement not found, creating...{Style.RESET_ALL}")
            departement = Departement(DEP_CODE='01', DEP_NOM='Example Departement')
            db.session.add(departement)
            db.session.commit()

        # Test creating a commune
        test_commune = Commune(COM_CODE='01001', COM_NOM='Example Commune', DEP_CODE='01')
        db.session.add(test_commune)
        db.session.commit()

        added_commune = Commune.query.filter_by(COM_CODE='01001').first()
        print(f"{Fore.YELLOW}Added commune:{Style.RESET_ALL}", added_commune)
        self.assertIsNotNone(added_commune)
        self.assertEqual(added_commune.COM_NOM, 'Example Commune')
        print(f"{Fore.YELLOW}--------------------------------------------------{Style.RESET_ALL}")
# ──────────────────────────────────────────────────────────────────────────────

    def test_03_affaire_creation(self):
        print(f"{Fore.GREEN}Testing affaire creation...{Style.RESET_ALL}")
        # Ensure necessary Departement exists
        departement = Departement.query.filter_by(DEP_CODE='01').first()
        if not departement:
            print(f"{Fore.RED}Departement not found, creating...{Style.RESET_ALL}")
            departement = Departement(DEP_CODE='01', DEP_NOM='Example Departement')
            db.session.add(departement)
            db.session.commit()

        # Ensure necessary Commune exists
        commune = Commune.query.filter_by(COM_CODE='01001').first()
        if not commune:
            print(f"{Fore.RED}Commune not found, creating...{Style.RESET_ALL}")
            commune = Commune(COM_CODE='01001', COM_NOM='Example Commune', DEP_CODE='01')
            db.session.add(commune)
            db.session.commit()

        # Now, create the Affaire instance
        affaire = Affaire(Nom='Example Affaire', DEP_CODE='01', COM_CODE='01001', Precision='Example Details')
        db.session.add(affaire)
        db.session.commit()

        # Verify the Affaire was added
        added_affaire = Affaire.query.filter_by(Nom='Example Affaire').first()
        print(f"{Fore.YELLOW}Added affaire:{Style.RESET_ALL}", added_affaire)
        self.assertIsNotNone(added_affaire)
        self.assertEqual(added_affaire.Precision, 'Example Details')
        print(f"{Fore.YELLOW}--------------------------------------------------{Style.RESET_ALL}")

if __name__ == '__main__':
    unittest.main()
