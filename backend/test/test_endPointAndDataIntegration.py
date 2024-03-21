import json
from App import create_app, db
from flask_testing import TestCase
from models import Affaire, Departement, Commune
from colorama import Fore, Style

class TestMyEndpoint(TestCase):
    # Setting up test environment
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        # Creating a test Flask application
        app = create_app(self)
        # Setting testing environment for the app
        app.config['TESTING'] = True
        # Setting up database URI for testing
        app.config['SQLALCHEMY_DATABASE_URI'] = self.SQLALCHEMY_DATABASE_URI
        return app

    def setUp(self):
        # Setting up before each test
        print(f"{Fore.YELLOW}Setting up test...{Style.RESET_ALL}")
        db.create_all()  # Creating database tables
        # Adding some sample data for testing
        db.session.add(Departement(DEP_CODE='01', DEP_NOM='Example Department'))
        db.session.add(Commune(COM_CODE='01001', COM_NOM='Example Commune', DEP_CODE='01'))
        db.session.commit()  # Committing changes to the database
        print(f"{Fore.GREEN}Test setup completed.{Style.RESET_ALL}")

    def tearDown(self):
        # Tearing down after each test
        print(f"{Fore.YELLOW}Tearing down test...{Style.RESET_ALL}")
        db.session.remove()  # Removing the database session
        db.drop_all()  # Dropping all database tables
        print(f"{Fore.GREEN}Test teardown completed.{Style.RESET_ALL}")

    def test_affaire_creation_with_multiple_locations(self):
        # Running a test to create an 'affaire' with multiple locations
        print(f"{Fore.YELLOW}Running test_affaire_creation_with_multiple_locations...{Style.RESET_ALL}")
        
        # Constructing the payload with multiple locations
        payload = {
            'nomDeLaffaire': 'New Affaire',
            'locations': [
                {'department': '01', 'commune': '01001', 'precision': 'Details about location 1'},
                {'department': '02', 'commune': '02001', 'precision': 'Details about location 2'},
                {'department': '03', 'commune': '03001', 'precision': 'Details about location 3'}
            ]
        }

        # Adding necessary data for new locations
        db.session.add_all([
            Departement(DEP_CODE='02', DEP_NOM='Second Department'),
            Commune(COM_CODE='02001', COM_NOM='Second Commune', DEP_CODE='02'),
            Departement(DEP_CODE='03', DEP_NOM='Third Department'),
            Commune(COM_CODE='03001', COM_NOM='Third Commune', DEP_CODE='03')
        ])
        db.session.commit()  # Committing changes to the database

        # Sending a POST request to the endpoint under test
        print(f"{Fore.BLUE}Sending POST request with payload: {json.dumps(payload)}{Style.RESET_ALL}")
        response = self.client.post('/my-endpoint',
                                    data=json.dumps(payload),
                                    content_type='application/json')
        print(f"{Fore.GREEN}POST request sent.{Style.RESET_ALL}")

        # Asserting the response status code
        print(f"{Fore.BLUE}Asserting response status code...{Style.RESET_ALL}")
        self.assertEqual(response.status_code, 201)

        # Verifying that the 'Affaire' was added to the database
        affaire = Affaire.query.first()
        print(f"{Fore.BLUE}Asserting Affaire in database...{Style.RESET_ALL}")
        self.assertIsNotNone(affaire)
        self.assertEqual(affaire.Nom, 'New Affaire')

        # Checking that the 'Affaire' is correctly associated with multiple locations
        for loc in payload['locations']:
            # Fetching the associated department and commune from the database
            departement = Departement.query.filter_by(DEP_CODE=loc['department']).first()
            commune = Commune.query.filter_by(COM_CODE=loc['commune']).first()

            # Asserting that the department and commune exist and are correctly linked to the 'Affaire'
            print(f"{Fore.BLUE}Asserting department and commune for location: {loc}{Style.RESET_ALL}")
            self.assertIsNotNone(departement)
            self.assertIsNotNone(commune)
            # Note: If there was a direct relationship between 'affaires' and locations, we'd check it here

        # Additional assertions can be added if needed
        print(f"{Fore.GREEN}Test test_affaire_creation_with_multiple_locations completed.{Style.RESET_ALL}")
