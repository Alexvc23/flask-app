from sqlalchemy import create_engine  # Importing create_engine function from SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker  # Importing scoped_session and sessionmaker from SQLAlchemy
from config.settings import DATABASE_URL  # Importing DATABASE_URL from config.settings module

# Creating an engine to connect to the database using the DATABASE_URL
engine = create_engine(DATABASE_URL)

# Creating a scoped session factory using sessionmaker,
# configuring it to not autocommit and autoflush, and binding it to the engine
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Function to retrieve a database session
def get_db_session():
    """
    Function to yield a database session to the caller and ensure proper closing afterward.

    Returns:
    db_session: SQLAlchemy database session
    """
    # Creating a new session from the session factory
    db_session = SessionLocal()
    try:
        # Yielding the session to the caller
        yield db_session
    finally:
        # Closing the session when the caller is done with it
        db_session.close()
