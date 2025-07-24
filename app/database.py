from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite DB URL — creates books.db in the project root
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"
# For PostgreSQL: "postgresql://user:password@localhost/dbname"

# Engine setup with SQLite-specific argument
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
Base = declarative_base()

