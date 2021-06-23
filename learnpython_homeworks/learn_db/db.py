from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("postgresql://mfkhtwul:UCu5TZs_LG4EiFD_iF-cW33_RJ49dKmO@"
                       "hattie.db.elephantsql.com/mfkhtwul")
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
