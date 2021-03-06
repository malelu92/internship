from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

DB = 'postgresql+psycopg2:///hostview'
engine = create_engine(DB, echo=False, poolclass=NullPool)
Base = declarative_base(engine)

class Keyevent(Base):
    __tablename__ = 'keyevent'
    __table_args__ = {'autoload':True}

def loadSession():
    """"""
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    return Session()

if __name__ == "__main__":
    session = loadSession()
    res = session.query(Keyevent).first()
    print (res.keyid, res.sessionid)
    session.close()
