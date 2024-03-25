from colorama import Fore, Style
from marshmallow import Schema, fields, ValidationError 
import re

# Define custom validation functions
"""

  ,,                               ,,          ,...                                      ,,
`7MM                             `7MM        .d' ""                               mm     db
  MM                               MM        dM`                                  MM
  MM  ,pW"Wq.   ,p6"bo   ,6"Yb.    MM       mMMmm`7MM  `7MM  `7MMpMMMb.  ,p6"bo mmMMmm `7MM  ,pW"Wq.`7MMpMMMb.
  MM 6W'   `Wb 6M'  OO  8)   MM    MM        MM    MM    MM    MM    MM 6M'  OO   MM     MM 6W'   `Wb MM    MM
  MM 8M     M8 8M        ,pm9MM    MM        MM    MM    MM    MM    MM 8M        MM     MM 8M     M8 MM    MM
  MM YA.   ,A9 YM.    , 8M   MM    MM        MM    MM    MM    MM    MM YM.    ,  MM     MM YA.   ,A9 MM    MM
.JMML.`Ybmd9'   YMbmd'  `Moo9^Yo..JMML.    .JMML.  `Mbod"YML..JMML  JMML.YMbmd'   `Mbmo.JMML.`Ybmd9'.JMML  JMML.


"""
def validate_alpha_numeric(value):
    """
    Validates that only alphanumeric characters are present.
    
    Args:
        value (str): The value to be validated.
        
    Raises:
        ValidationError: If the value contains characters other than alphanumeric.
    """
    print(Fore.BLUE + "Validating alpha numeric characters..." + Style.RESET_ALL)
    if not re.match(r'^[a-zA-Z0-9]*$', value):
        raise ValidationError(Fore.RED + "Value must contain only alphanumeric characters" + Style.RESET_ALL)
    # ──────────────────────────────────────────────────────────────────────
    
def validate_department_length(value):
    """
    Validates the length of the department code.
    
    Args:
        value (int or str): The value to be validated.
        
    Raises:
        ValidationError: If the value is not within the specified length constraints.
    """
    print(Fore.BLUE + "Validating department length..." + Style.RESET_ALL)

    # accept only alpha numeric characters
    validate_alpha_numeric(value)

    if isinstance(value, int):
        if not 1 <= value <= 99:
            raise ValidationError(Fore.RED + "Department code must be an integer between 1 and 99" + Style.RESET_ALL)
    elif isinstance(value, str):
        if not 1 <= len(value) <= 2:
            raise ValidationError(Fore.RED + "Department code must be a string with length between 1 and 2" + Style.RESET_ALL)
    else:
        raise ValidationError(Fore.RED + "Invalid type for department code" + Style.RESET_ALL)
        # ──────────────────────────────────────────────────────────────

def validate_commune_length(value):
    """
    Validates the length of the commune code.
    
    Args:
        value (str): The value to be validated.
        
    Raises:
        ValidationError: If the value is not within the specified length constraints.
    """
    print(Fore.BLUE + "Validating commune length..." + Style.RESET_ALL)
    if not 1 <= len(value) <= 20:
        raise ValidationError(Fore.RED + "Commune code must be a string with length between 1 and 20 long" + Style.RESET_ALL)
        # ──────────────────────────────────────────────────────────────

def validate_nomDeLaffaire_length(value):
    """
    Validates the length of the affair name.
    
    Args:
        value (str): The value to be validated.
        
    Raises:
        ValidationError: If the value is not within the specified length constraints.
    """
    # accept only alpha numeric characters
    validate_alpha_numeric(value)

    print(Fore.BLUE + "Validating affaire name length..." + Style.RESET_ALL)
    if not 1 <= len(value) <= 100:
        raise ValidationError(Fore.RED + "Affaire name must be a string with length between 1 and 100 characters long" + Style.RESET_ALL)
        # ──────────────────────────────────────────────────────────────

def validate_presition_length(value):
    """
    Validates the length of the precision field.
    
    Args:
        value (str): The value to be validated.
        
    Raises:
        ValidationError: If the value is not within the specified length constraints.
    """
    # accept only alpha numeric characters
    validate_alpha_numeric(value)

    print(Fore.BLUE + "Validating presition field length..." + Style.RESET_ALL)
    if not 1 <= len(value) <= 400:
        raise ValidationError(Fore.RED + "presition field must be a string with length between 1 and 400 characters long" + Style.RESET_ALL)

# ──────────────────────────────────────────────────────────────────────────────
"""

                     ,,    ,,        ,,                  ,,                                  ,,
                   `7MM    db      `7MM           mm     db                                `7MM
                     MM              MM           MM                                         MM
`7M'   `MF',6"Yb.    MM  `7MM   ,M""bMM   ,6"Yb.mmMMmm `7MM  ,pW"Wq.`7MMpMMMb.       ,p6"bo  MM   ,6"Yb.  ,pP"Ybd ,pP"Ybd  .gP"Ya  ,pP"Ybd
  VA   ,V 8)   MM    MM    MM ,AP    MM  8)   MM  MM     MM 6W'   `Wb MM    MM      6M'  OO  MM  8)   MM  8I   `" 8I   `" ,M'   Yb 8I   `"
   VA ,V   ,pm9MM    MM    MM 8MI    MM   ,pm9MM  MM     MM 8M     M8 MM    MM      8M       MM   ,pm9MM  `YMMMa. `YMMMa. 8M"""""" `YMMMa.
    VVV   8M   MM    MM    MM `Mb    MM  8M   MM  MM     MM YA.   ,A9 MM    MM      YM.    , MM  8M   MM  L.   I8 L.   I8 YM.    , L.   I8
     W    `Moo9^Yo..JMML..JMML.`Wbmd"MML.`Moo9^Yo.`Mbmo.JMML.`Ybmd9'.JMML  JMML.     YMbmd'.JMML.`Moo9^Yo.M9mmmP' M9mmmP'  `Mbmmd' M9mmmP'


"""
class LocationSchema(Schema):
    """
    Schema for the location data.
    """
    department = fields.Field(required=True, validate=validate_department_length)  # Updated department field
    commune = fields.String(required=True, validate=validate_commune_length)  # Updated commune field
    precision = fields.String(required=True, validate=validate_presition_length)  # Precision is optional
# ──────────────────────────────────────────────────────────────────────────────

class AffaireSchema(Schema):
    """
    Schema for the affair data.
    """
    nomDeLaffaire = fields.String(required=True, validate=validate_nomDeLaffaire_length)
    locations = fields.List(fields.Nested(LocationSchema), required=True)  # Locations are optional
