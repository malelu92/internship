from sqlalchemyimport create_engine
from sqlalchemy.ext.declarativeimport declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

DB = 'postgresql+psycopg2:///hostview'
engine = create_engine(DB, echo=False, poolclass=NullPool)
Base = declarative_base(engine)

class Destination(Base):
    __tablename__ = 'destination'
    __table_args__ = {'autoload':True}
