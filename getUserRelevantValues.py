import sys
sys.path.append('tables')

from environment import Environment
from flow import Flow
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

    evaluateUsersWithManySessions(result, dbsession)

    #evaluateUsersWithFewSessions(result2, dbsession)

    dbsession.close()


def evaluateUsersWithManySessions (result, dbsession):
    for item in result:
        sqlSessionPerUser = text('select * from session where userid =:user').bindparams(user = item.userid)
        resultSessionPerUser = dbsession.execute(sqlSessionPerUser)

        evaluateUserEnvironment(item.userid, dbsession)
        break

#        usermacLines = evaluateMacAddress(resultSessionPerUser)
#        print (item.userid, usermacLines)

def evaluateUserEnvironment(userid, dbsession):
    sql = text('select distinct session.sessionid, session.starttime, session.endtime, environment.sourcetype from session, environment where session.envid = environment.envid and session.userid =:user and environment.sourcetype is not NULL order by session.sessionid;').bindparams(user = userid)

    result = dbsession.execute(sql)

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
        print(item.sessionid, item.starttime, item.sourcetype, key)
        #writer.writerow([item.sessionid] + [item.starttime] + [item.endtime] + [resultTime] + [item.sourcetype] + [key])

def evaluateMacAddress (resultSessionPerUser):
    usermacLines = 0
    for userSession in resultSessionPerUser:
        if (userSession.usermac != None):
            usermacLines = usermacLines + 1
    return usermacLines
    

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
