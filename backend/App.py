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

from models import Departement, Commune, Affaire, User, Location, db

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
        json_data = request.get_json()
        affaire_schema = AffaireSchema()

        try:
            data = affaire_schema.load(json_data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        try:
            user = User.query.filter_by(username=data['userName']).first()
            if not user:
                user = User(username=data['userName'])
                db.session.add(user)

            new_affaire = Affaire(nom=data['nomDeLaffaire'], user=user)
            db.session.add(new_affaire)  # Make sure to add the new affaire to the session here

            for loc in data.get('locations', []):
                departement = Departement.query.filter_by(DEP_CODE=loc['department']).first()
                commune = Commune.query.filter_by(COM_NOM=loc['commune']).first()
                if not departement or not commune:
                    return jsonify({"error": "Missing department or commune data"}), 400

                new_location = Location(department=loc['department'], commune=loc['commune'], precision=loc['precision'], affaire=new_affaire)
                db.session.add(new_location)

            db.session.commit()
            return jsonify({'success': True, 'message': 'Affaire and locations saved successfully'}), 201

        except IntegrityError as e:
            db.session.rollback()
            error_info = str(e.__cause__)
            if 'uix_nom_user_id' in error_info:
                return jsonify({"error": "Une affaire avec le même nom existe déjà pour cet utilisateur"}), 400
            elif 'users_username_key' in error_info:
                return jsonify({"error": "Un utilisateur avec le même nom d'utilisateur existe déjà"}), 400
            return jsonify({"error": "Un problème d'intégrité de la base de données s'est produit"}), 400


        except Exception as e:
            db.session.rollback()
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