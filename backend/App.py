import sys
from flask import request, jsonify
# Import necessary modules and classes from Flask
from flask import Flask, jsonify, request
# Import SQLAlchemy for database management
from flask_sqlalchemy import SQLAlchemy
# Import Config class from settings module to configure the Flask app
from config.settings import Config
# Import Migrate class from flask_migrate for handling database migrations
from flask_migrate import Migrate

from marshmallow import ValidationError
# Import models from the models module to ensure they are recognized by SQLAlchemy

from models import Departement, Commune, Affaire, User, db


from validation import AffaireSchema


from sqlalchemy.exc import SQLAlchemyError, IntegrityError # to handle exception 

from flask_cors import CORS


def create_app(cofing_class= Config):
    # Initialize Flask application
    app = Flask(__name__)

    # Load configuration settings from the Config class
    app.config.from_object(cofing_class)

    db.init_app(app)

    # Initialize the Migrate object with the Flask app and SQLAlchemy db instance
    # This allows for easy database migrations using Flask-Migrate
    migrate = Migrate(app, db)
    

    # Replace 'http://example.com' with the actual origin of your frontend
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})



    """

    #####   ####  #    # ##### ######  ####
    #    # #    # #    #   #   #      #
    #    # #    # #    #   #   #####   ####
    #####  #    # #    #   #   #           #
    #   #  #    # #    #   #   #      #    #
    #    #  ####   ####    #   ######  ####

    """

    @app.errorhandler(Exception)
    def handle_exception(e):
        # Log the error here with app.logger or another logging mechanism
        return jsonify(error=str(e)), 500


    # ──────────────────────────────────────────────────────────────────────

    @app.route('/departement', methods=['GET'])
    def get_departements():
        try:
            departements = Departement.query.all()
            return jsonify([{'DEP_CODE': dep.DEP_CODE, 'DEP_NOM': dep.DEP_NOM} for dep in departements])
        except SQLAlchemyError as e:
            # Log the exception here
            return jsonify(error="Database error occurred"), 500

    # ──────────────────────────────────────────────────────────────────────
    @app.route('/communes', methods=['GET'])
    def get_communes():
        dep_code = request.args.get('dep_code')
        if not dep_code:
            return jsonify(error="Department code is required"), 400

        try:
            communes = Commune.query.filter_by(DEP_CODE=dep_code).all()
            if not communes:
                return jsonify(error="Department not found or has no communes"), 404
            return jsonify([{'COM_CODE': com.COM_CODE, 'COM_NOM': com.COM_NOM, 'DEP_CODE': com.DEP_CODE} for com in communes])
        except SQLAlchemyError as e:
            # Log the exception here
            return jsonify(error="Database error occurred"), 500
    # ──────────────────────────────────────────────────────────────────────


    @app.route('/my-endpoint', methods=['POST'])
    def create_affaire():
        # Create an instance of the AffaireSchema
        json_data = request.get_json()
        # inicilise an instace of the data validator
        affaire_schema = AffaireSchema()
        try:
            #validate the data against the schema
            data = affaire_schema.load(json_data)
            print(f"receiving data from Fronted: {data}")
            sys.stderr.write("Received data: {}\n".format(data))  # Add a print statement to log received data
        except ValidationError as err:
            # Return validation errors 
            return jsonify(err.messages), 400

        try:
            # The following link explains how error handling for the Affaire object (model)s
            # https://diagrams.helpful.dev/d/d:2ByVkNFB

            # Create new user instace representation with the new username
            newUser = User(username=data['userName'])
            db.session.add(newUser)
            # Create new Affaire instace representation with the new affaire name
            new_affaire = Affaire(Nom=data['nomDeLaffaire'])
            db.session.add(new_affaire)

            # Iterate over locations if they exist
            for loc in data.get('locations', []):
                # Assuming that each location must have an existing department and commune
                #?  the department data base already exist, here we are just making sure it is an existing deparment so we can associated wo the new
                #?  affaire we are creating
                departement = Departement.query.filter_by(DEP_CODE=loc['department']).first()
                #? we do the same procedure we applied to the department data base
                commune = Commune.query.filter_by(COM_CODE=loc['commune']).first()
                
                if not departement or not commune:
                    # One way to handle this could be to skip the locations with missing data,
                    # or you could return an error - depends on your business logic.
                    sys.stderr.write("Missing department or commune data for location: {}\n".format(loc))
                    continue

                # Associate the affaire with the departement and commune
                # This assumes your Affaire model can directly link to Departement and Commune
                new_affaire.DEP_CODE = departement.DEP_CODE
                new_affaire.COM_CODE = commune.COM_CODE
                # Add more logic as needed to correctly associate the data

            # Commit the transaction
            db.session.commit()
            sys.stdout.write("Affaire and locations saved successfully\n")
            return jsonify({'success': True, 'message': 'Affaire and locations saved successfully'}), 201
        except IntegrityError as e:
                db.session.rollback()
                error_info = str(e.__cause__)
                sys.stderr.write(f"IntegrityError occurred: {error_info}\n")
                if 'affaires_Nom_key' in error_info:
                    return jsonify({"error": "An affaire with the same name already exists"}), 400
                elif 'users_username_key' in error_info:
                    return jsonify({"error": "A user with the same username already exists"}), 400
                else:
                    return jsonify({"error": "A database integrity issue occurred"}), 400
        except Exception as e:
            db.session.rollback()
            sys.stderr.write(f"Error occurred during processing: {e}\n")
            return jsonify({'error': 'Server error', 'message': str(e)}), 500


    # ──────────────────────────────────────────────────────────────────────
    # Additional setup like route import can go here
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app

"""

 #    #   ##   # #    #    #####  #####   ####   ####  #####    ##   #    #
 ##  ##  #  #  # ##   #    #    # #    # #    # #    # #    #  #  #  ##  ##
 # ## # #    # # # #  #    #    # #    # #    # #      #    # #    # # ## #
 #    # ###### # #  # #    #####  #####  #    # #  ### #####  ###### #    #
 #    # #    # # #   ##    #      #   #  #    # #    # #   #  #    # #    #
 #    # #    # # #    #    #      #    #  ####   ####  #    # #    # #    #

"""

app = create_app(); 

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')  # Remember to turn off debug mode in production