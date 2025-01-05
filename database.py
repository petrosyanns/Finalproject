from sqlalchemy import create_enginefrom sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
MySQLDATABASE_URL = "mysql://semyon_petrosyan:1234@localhost/cooperative_db"

engine = create_engine(DATABASE_URL, pool_size=5, max_overflow=0, pool_recycle=3600)


Base = declarative_base()

