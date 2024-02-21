# In the __init__.py file of the models directory, import your models to make them accessible through the package. 
#This approach also helps with resolving circular dependencies and makes imports cleaner in other parts of your application.
# /backend/models/__init__.py:

from .base import Base  # Ifrom .base import Base  # Import Base to ensure it's initialized
from .departement import Departement
from .commune import Commune
from .affaire import Affaire
from .user import User