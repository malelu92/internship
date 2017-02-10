import sys

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.pool import NullPool

def main():
    DB = 'postgresql+psycopg2:///ucnstudy'

    engine = create_engine(DB, echo=False, poolclass=NullPool)
    metadata = MetaData()
    metadata.reflect(engine)
    for table in metadata.tables.values():
        print(table.name)
        for column in table.c:
            print (column.name)

if __name__ == "__main__":
    main()
