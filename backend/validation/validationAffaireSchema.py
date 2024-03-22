from marshmallow import Schema, fields, validate, ValidationError 


# Define custom validation functions
def validate_department_length(value):
    print("Validating department length...")
    if isinstance(value, int):
        if not 1 <= value <= 99:
            raise ValidationError("Department code must be an integer between 1 and 99")
    elif isinstance(value, str):
        if not 1 <= len(value) <= 2:
            raise ValidationError("Department code must be a string with length between 1 and 2")
    else:
        raise ValidationError("Invalid type for department code")

def validate_commune_length(value):
    print("Validating commune length...")
    if not 1 <= len(value) <= 20:
        raise ValidationError("Commune code must be a string with length between 1 and 20")

class LocationSchema(Schema):
    department = fields.Field(required=True, validate=validate_department_length)  # Updated department field
    commune = fields.String(required=True, validate=validate_commune_length)  # Updated commune field
    precision = fields.String(required=True)  # Precision is optional


class AffaireSchema(Schema):
    nomDeLaffaire = fields.String(required=True)
    locations = fields.List(fields.Nested(LocationSchema), required=True)  # Locations are optional
