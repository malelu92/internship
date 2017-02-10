import sys

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy.pool import NullPool


def main():
    DB = 'postgresql+psycopg2:///hostview'

    engine = create_engine(DB, echo=False, poolclass=NullPool)
    metadata = MetaData()
    metadata.reflect(engine)
    #for table in metadata.tables.values():
    #    if table.name == "flow":
    #        for column in table.c:
    #            print column.name
    
    flow_table = Table('flow', metadata, autoload=True, autoload_with=engine)
    print (flow_table.name)

    for column in flow_table.c:
        print (column.name)

if __name__ == "__main__":
    main()
