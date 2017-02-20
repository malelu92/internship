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

    #get users with a lot and just a few session info
    sql = text('select userid from session group by userid having count(userid) > 300;')
    sql2 = text('select userid from session group by userid having count(userid) <= 300;')

    result = dbsession.execute(sql)
    result2 = dbsession.execute(sql2)

    for item in result:
        sqlPerUser = text('select * from session where userid =:user').bindparams(user = item.userid)
        resultPerUser = dbsession.execute(sqlPerUser)
        
        usermacLines = 0
        for userSession in resultPerUser:
            if (userSession.usermac != None):
                usermacLines = usermacLines + 1
             #   print (userSession.userid)
        print (item.userid, usermacLines)

#    for item in result2:
#        print item.userid


    dbsession.close()

if __name__ == "__main__":
    main()
