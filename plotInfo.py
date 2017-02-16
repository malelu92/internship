import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

matplotlib.style.use('ggplot')
sys.path.append('tables')

from session import Session
from traceTable import TraceTable

from sqlalchemy import and_
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

    session_res = dbsession.query(Session).filter(\
                    Session.starttime >= '2012-02-27',\
                    Session.starttime <= '2012-04-01').filter(\
                        Session.userid >= '5749374a-0000-0000-0000-000000000000',\
                        Session.userid <=  '5749374a-ffff-ffff-ffff-ffffffffffff').order_by(\
                                                                                            Session.sessionid)

    with open('userInfo.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for item in session_res:
            resultTime = item.endtime - item.starttime
            #writer.writerow([item.sessionid]+[item.starttime]+[item.endtime])
            #print (item.sessionid, item.starttime, item.endtime)
            writer.writerow([item.starttime] + [item.endtime] + [resultTime])

    dbsession.close()

if __name__ == "__main__":
    main()
