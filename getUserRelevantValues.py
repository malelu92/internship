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

    evaluateUsersWithManySessions (result, dbsession)

    evaluateUsersWithFewSessions(result2, dbsession)

    dbsession.close()


def evaluateUsersWithManySessions (result, dbsession):
    for item in result:
        sqlSessionPerUser = text('select * from session where userid =:user').bindparams(user = item.userid)
        resultSessionPerUser = dbsession.execute(sqlSessionPerUser)

        usermacLines = 0
        for userSession in resultSessionPerUser:
            if (userSession.usermac != None):
                usermacLines = usermacLines + 1
             #   print (userSession.userid)
        print (item.userid, usermacLines)

def evaluateUsersWithFewSessions (result, dbsession):
    #evaluate users with few sessions
    for item in result:
        #will analyse flows
        sqlFlowPerUser = text('select * from session, flow where userid =:user and session.sessionid = flow.sessionid').bindparams(user = item.userid)
        resultFlowPerUser = dbsession.execute(sqlFlowPerUser)
        for userFlow in resultFlowPerUser:
            print (userFlow.userid, userFlow.remoteport)
        #print item.userid

if __name__ == "__main__":
    main()
