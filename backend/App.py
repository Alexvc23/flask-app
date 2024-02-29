# Import necessary modules and classes from Flask
from flask import Flask, jsonify, request
# Import SQLAlchemy for database management
from flask_sqlalchemy import SQLAlchemy
# Import Config class from settings module to configure the Flask app
from config.settings import Config
# Import Migrate class from flask_migrate for handling database migrations
from flask_migrate import Migrate
# Import models from the models module to ensure they are recognized by SQLAlchemy
from models import Departement, Commune, Affaire, User  

from sqlalchemy.exc import SQLAlchemyError # to handle exception 


# Initialize Flask application
app = Flask(__name__)

# Load configuration settings from the Config class
app.config.from_object(Config)

# Initialize SQLAlchemy object and bind it to the Flask application
# SQLAlchemy is an ORM (Object-Relational Mapping) tool that simplifies database management in Flask applications.
# By creating an instance of SQLAlchemy and binding it to the Flask application,
# we enable interaction with the database using SQLAlchemy's ORM features.
# This allows us to define database models as Python classes and perform operations on them easily.
db = SQLAlchemy(app)

# Initialize the Migrate object with the Flask app and SQLAlchemy db instance
# This allows for easy database migrations using Flask-Migrate
migrate = Migrate(app, db)



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


@app.route('/departement', methods=['GET'])
def get_departements():
    try:
        departements = Departement.query.all()
        return jsonify([{'DEP_CODE': dep.DEP_CODE, 'DEP_NOM': dep.DEP_NOM} for dep in departements])
    except SQLAlchemyError as e:
        # Log the exception here
        return jsonify(error="Database error occurred"), 500

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


# Additional setup like route import can go here
@app.route('/')
def hello_world():
    return 'Hello, World!'


"""

 #    #   ##   # #    #    #####  #####   ####   ####  #####    ##   #    #
 ##  ##  #  #  # ##   #    #    # #    # #    # #    # #    #  #  #  ##  ##
 # ## # #    # # # #  #    #    # #    # #    # #      #    # #    # # ## #
 #    # ###### # #  # #    #####  #####  #    # #  ### #####  ###### #    #
 #    # #    # # #   ##    #      #   #  #    # #    # #   #  #    # #    #
 #    # #    # # #    #    #      #    #  ####   ####  #    # #    # #    #

"""
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')  # Remember to turn off debug mode in production
