import sys

from flow import Flow

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

    #flow_table = Table('flow', metadata, autoload=True, autoload_with=engine)
    #print (flow_table.name)

    #for column in flow_table.c:
    #    print (column.name)

    #ses.close()

    flow_res = session.query(Flow).first()
    print (flow_res.flowid, flow_res.sessionid)

if __name__ == "__main__":
    main()
