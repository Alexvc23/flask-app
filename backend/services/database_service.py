from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from config.settings import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def get_db_session():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()