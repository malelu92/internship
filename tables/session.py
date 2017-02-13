from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

DB = 'postgresql+psycopg2:///hostview'
engine = create_engine(DB, echo=False, poolclass=NullPool)
Base = declarative_base(engine)

class Session(Base):
    __tablename__ = 'session'
    __table_args__ = {'autoload':True}

def loadDatabaseSession():
    """"""
    metadata = Base.metadata
    Database_session = sessionmaker(bind=engine)
    return Database_session()

if __name__ == "__main__":
    database_session = loadDatabaseSession()
    res = database_session.query(Session).first()
    print (res.sessionid, res.starttime, res.endtime)
    database_session.close()
