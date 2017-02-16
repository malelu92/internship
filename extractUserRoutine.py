import sys
sys.path.append('tables')

from flow import Flow
from traceTable import TraceTable
from session import Session
from environment import Environment
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

    sql = text('select * from session limit 10')
    result = dbsession.execute(sql)

    for item in result:
        print (item.sessionid)

   # env_res = dbsession.query(Environment, Envid_sessionid).filter(
   #     Environment.userid >= '5749374a-0000-0000-0000-000000000000',
   #     Environment.userid <= '5749374a-ffff-ffff-ffff-ffffffffffff').filter(
   #         Envid_sessionid.envid == Environment.envid)
           

    #env_res2 = dbsession.query(env_res, Envid_sessionid).filter(env_res.

    #for item in env_res:
    #    print (item.sessionid, item.envid, item.hardwareport, item.sourcetype)
                                                
                                                                              
    dbsession.close()

if __name__ == "__main__":
    main()
