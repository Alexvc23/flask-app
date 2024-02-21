# In the __init__.py file of the models directory, import your models to make them accessible through the package. 
#This approach also helps with resolving circular dependencies and makes imports cleaner in other parts of your application.
# /backend/models/__init__.py:

from .base import Base  # Import the base class to make it available for metadata creation
from .user import User  # Import the User model to make it available for import from the models package
