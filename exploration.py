import sys
sys.path.append('tables')

from flow import Flow
from traceTable import TraceTable
from session import Session
from tsjitter import Tsjitter

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

    for table in metadata.tables.values():
        print (table.name)

    #flow_table = Table('flow', metadata, autoload=True, autoload_with=engine)
    #print (flow_table.name)

    #for column in flow_table.c:
    #    print (column.name)

    #ses.close()

   ## print ("flow info")
    #flow_res = dbsession.query(Flow).limit(4).all()
    #for item in flow_res:
    #    print (item.flowid, item.sessionid)
    #col_names = Flow.__table__.columns.keys()
    #for column in col_names:
    #    print (column)

    #print ("trace info") 
    #trace_res = dbsession.query(TraceTable).limit(5).all()
    #for item in trace_res:
    #    print (item.usermac)

print ("session info")
session_res = dbsession.query(Session).filter(and_(Session.starttime <= '2011-01-04', Session.starttime >= '2011-01-10'))
for item in session_res:
    print (item.sessionid, item.starttime, item.endtime)

#    print ("tsjitter info")
#    tsjitter_res = dbsession.query(Tsjitter).limit(2).all()
#    for item in tsjitter_res:
#        print (item.jitterid)

dbsession.close()

if __name__ == "__main__":
    main()
