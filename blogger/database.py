from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://interns:interns%40123@192.168.0.220:5432/internsb2"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(bind = engine)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
