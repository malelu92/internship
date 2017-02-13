from sqlalchemyimport create_engine
from sqlalchemy.ext.declarativeimport declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

DB = 'postgresql+psycopg2:///hostview'
engine = create_engine(DB, echo=False, poolclass=NullPool)
Base = declarative_base(engine)

class Tscpu(Base):
    __tablename__ = 'tscpu'
    __table_args__ = {'autoload':True}
