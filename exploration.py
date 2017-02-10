import sys
sys.path.append('tables')

from flow import Flow
from trace import Trace

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool


def main():
    DB = 'postgresql+psycopg2:///hostview'
    engine = create_engine(DB, echo=False, poolclass=NullPool)
    Session = sessionmaker(bind=engine)
    metadata = MetaData()

    session = Session()
    metadata.reflect(engine)

    #for table in metadata.tables.values():
    #    print (table.name)

    #flow_table = Table('flow', metadata, autoload=True, autoload_with=engine)
    #print (flow_table.name)

    #for column in flow_table.c:
    #    print (column.name)

    #ses.close()

    #flow_res = session.query(Flow).limit(4).all()
    #for item in flow_res:
    #    print (item.flowid, item.sessionid)

    trace_res = session.query(Trace).limit(5).all()
    for item in trace_res:
        print (item.usermac)

    session.close()

if __name__ == "__main__":
    main()
