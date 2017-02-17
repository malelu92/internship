import sys
sys.path.append('tables')

from flow import Flow
from traceTable import TraceTable
from session import Session
from environment import Environment
from keyevent import Keyevent
#from envid_sessionid import Envid_sessionid

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy import text

def main():
    DB = 'postgresql+psycopg2:///hostview'
    engine = create_engine(DB, echo=False, poolclass=NullPool)
    DBSession = sessionmaker(bind=engine)
    metadata = MetaData()

    dbsession = DBSession()
    metadata.reflect(engine)

    sql = text('select distinct * from session, keyevent where session.sessionid = keyevent.sessionid and session.userid between \'5749374a-0000-0000-0000-000000000000\' and \'5749374a-ffff-ffff-ffff-ffffffffffff\' and keyevent.mouse_key = \'t\' limit 10')
    result = dbsession.execute(sql)

    print ("          sessionid        envid         userid       mouse_key")
    for item in result:
        print (item.sessionid, item.envid, item.starttime, item.mouse_key)
                                                                              
    dbsession.close()

if __name__ == "__main__":
    main()
