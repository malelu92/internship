import sys
sys.path.append('tables')

from session import Session

from sqlalchemy import and_
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool


def main():
    DB = 'postgresql+psycopg2:///hostview'
    engine = create_engine(DB, echo=False, poolclass=NullPool)
    DBSession = sessionmaker(bind=engine)
    metadata = MetaData()

    dbsession = DBSession()
    metadata.reflect(engine)

    session_res = dbsession.query(Session).filter(Session.starttime >= '2011-01-04',\
                                                  Session.starttime <= '2011-01-05').filter(\
                                                                                            Session.userid >= '56135a80-0000-0000-0000-000000000000',\
                                                    Session.userid <=  '56135a80-ffff-ffff-ffff-ffffffffffff')
    #session_res2 = dbsession.query(session_res).filter(session
    for item in session_res:
        print (item.sessionid, item.starttime, item.endtime)

    dbsession.close()

if __name__ == "__main__":
    main()
