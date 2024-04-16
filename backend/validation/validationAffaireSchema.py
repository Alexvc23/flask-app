from colorama import Fore, Style  # Importing modules for styling (not used in provided code)
from marshmallow import Schema, fields, ValidationError, validates  # Importing marshmallow for data validation
import re  # Importing regular expression module

# Define custom validation functions
# ──────────────────────────────────────────────────────────────────────

# Custom validation function to validate alphanumeric characters with spaces and certain accented characters
def validate_alpha_numeric_with_space(value, message="La valeur doit contenir uniquement des caractères alphanumériques," +
                                      " des espaces, des tirets et des caractères accentués."):
    """
    Validates that only alphanumeric characters with spaces and certain accented characters are present.
    """
    if not re.match(r'^[a-zA-Z0-9 àâäéèêëîïôöùûüçÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ-]*$', value):
        raise ValidationError(message)

# ──────────────────────────────────────────────────────────────────────

# Schema for the location data
class LocationSchema(Schema):
    """
    Schema for the location data.
    """
    # Validation per field
    department = fields.String(required=True)  # Updated department field
    commune = fields.String(required=True)  # Updated commune field
    precision = fields.String(required=True)  # Precision is optional

    # Custom validation for the 'department' field
    @validates('department') 
    def validate_department(self, value):
        # Attempt to convert to an integer
        try:
            num = int(value)
        except ValueError:
            raise ValidationError("Le champ 'department' doit être validé.")

        # Check if it's within the desired range
        if not (1 <= num <= 99):
            raise ValidationError("La champ 'Departement' doit être un entier 1 et 99.")

    # Custom validation for the 'commune' field
    @validates('commune') 
    def validate_commune(self, value):
        # Validate alphanumeric characters with spaces and certain accented characters
        validate_alpha_numeric_with_space(value, "La valeur du champ 'commune' doit contenir uniquement des caractères alphanumériques," +
                                          " des espaces, des tirets et des caractères accentués.")
        
        # Check if it's within the desired range
        if not (1 <= len(value) <= 30):
            raise ValidationError("La champ 'Commune' doit être un entier 1 et 30.")

    # Custom validation for the 'precision' field
    @validates('precision') 
    def validate_precision(self, value):
        # Validate alphanumeric characters with spaces and certain accented characters
        validate_alpha_numeric_with_space(value, "La valeur du champ 'precision' doit contenir uniquement des caractères alphanumériques," +
                                          " des espaces, des tirets et des caractères accentués.")
        
        # Check if it's within the desired range
        if not (10 <= len(value) <= 400):
            raise ValidationError("La longueur du champ 'Precision' doit être comprise entre 10 et 400.")

# ──────────────────────────────────────────────────────────────────────

# Schema for the affair data
class AffaireSchema(Schema):
    """
    Schema for the affair data.
    """
    userName = fields.String(required=True)  # Username field
    nomDeLaffaire = fields.String(required=True)  # Name of the affair field
    locations = fields.List(fields.Nested(LocationSchema), required=True)  # Location data is mandatory 

    # Custom validation for the 'userName' field
    @validates('userName') 
    def validate_username(self, value):
        # Validate alphanumeric characters with spaces and certain accented characters
        validate_alpha_numeric_with_space(value, "La valeur du champ 'userName' doit contenir uniquement des caractères alphanumériques," +
                                           " des espaces, des tirets et des caractères accentués.")
        
        # Check if it's within the desired range
        if not (3 <= len(value) <= 30):
            raise ValidationError("La longueur du champ 'userName' doit être comprise entre 5 et 30.")

    # Custom validation for the 'nomDeLaffaire' field
    @validates('nomDeLaffaire') 
    def validate_nomdelaffaire(self, value):
        # Validate alphanumeric characters with spaces and certain accented characters
        validate_alpha_numeric_with_space(value, "La valeur du champ 'nomDeLaffaire' doit contenir uniquement des caractères alphanumériques," + 
                                          " des espaces, des tirets et des caractères accentués.")
        
        # Check if it's within the desired range
        if not (5 <= len(value) <= 50):
            raise ValidationError("La longueur du champ 'nom de l'affaire' doit être comprise entre 5 et 50.")