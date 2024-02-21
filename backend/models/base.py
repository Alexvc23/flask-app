# Place the Base = declarative_base() declaration in a separate file, like base.py, 
# within the models directory. This makes the Base class easily importable in other model 
# files and helps avoid circular imports.

from sqlalchemy.ext.declarative import declarative_base

# Create a base class for all mapped classes to inherit from
Base = declarative_base()

# This base class provides common functionality and settings for all SQLAlchemy model classes
# It serves as the base class from which all mapped classes should inherit
# Using this base class allows SQLAlchemy to track model classes and their mappings to database tables
# It provides a centralized place to define metadata about the tables and common functionality for all models

