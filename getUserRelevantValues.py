import sys
sys.path.append('tables')

from flow import Flow
from traceTable import TraceTable
from session import Session

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

def main():
    DB = 'postgresql+psycopg2:///hostview'
    engine = create_engine(DB, echo=False, poolclass=NullPool)
    DBSession = sessionmaker(bind=engine)
    metadata = MetaData()

    dbsession = DBSession()
    metadata.reflect(engine)

    sql = text('select userid from session group by userid having count(userid) > 300;')

    result = dbsession.execute(sql)

    for item in result:
        print item.userid


    dbsession.close()

if __name__ == "__main__":
    main()
