from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ---------------------------------------------------------
# DATABASE URL
# ---------------------------------------------------------
# SQLite database stored locally as a file
SQLALCHEMY_DATABASE_URL = "sqlite:///./table_time.db"


# ---------------------------------------------------------
# ENGINE CREATION
# ---------------------------------------------------------
# The engine is responsible for connecting to the database
# check_same_thread=False is required for SQLite when used with FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)


# ---------------------------------------------------------
# SESSION FACTORY
# ---------------------------------------------------------
# SessionLocal creates new database sessions (connections)
# autocommit=False → changes must be committed manually
# autoflush=False → prevents automatic DB writes
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ---------------------------------------------------------
# BASE CLASS FOR MODELS
# ---------------------------------------------------------
# All database models (like Task) inherit from this Base
# It keeps track of tables and allows SQLAlchemy to create them
Base = declarative_base()