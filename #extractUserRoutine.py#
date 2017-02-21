import csv
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

    #sql = text('select distinct * from session, keyevent \
    #where session.sessionid = keyevent.sessionid \ 
    #and session.userid between \'3920542c-0000-0000-0000-000000000000\' \ 
    #and \'3920542c-ffff-ffff-ffff-ffffffffffff\' \ 
    #and keyevent.mouse_key = \'t\' limit 10')
    
    """sql = text('select distinct session.sessionid, session.starttime, flow.flowid, flow.srcip, flow.srcport, flow.dstip, flow.dstport from session, flow where session.sessionid = flow.sessionid and session.userid between \'3920542c-0000-0000-0000-000000000000\' and \'3920542c-ffff-ffff-ffff-ffffffffffff\' order by session.sessionid;')"""

    sql = text('select distinct session.sessionid, session.starttime, session.endtime, environment.sourcetype from session, environment where session.envid = environment.envid and session.userid between \'11f73e79-0000-0000-0000-000000000000\' and \'11f73e79-ffff-ffff-ffff-ffffffffffff\' and environment.sourcetype is not NULL order by session.sessionid;')
 
    result = dbsession.execute(sql)
    
    with open('userSessionEnvironment.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        for item in result:

            if (item.sourcetype == "Home"):
                key = 1;
            elif (item.sourcetype == "Conference/meeting"):
                key = 2;
            elif (item.sourcetype == "Work"):
                key = 3;
            else:
                key = 4;

            resultTime = item.endtime - item.starttime
            writer.writerow([item.sessionid] + [item.starttime] + [item.endtime] + [resultTime] + [item.sourcetype] + [key])

    dbsession.close()

if __name__ == "__main__":
    main()
