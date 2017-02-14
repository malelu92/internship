import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

matplotlib.style.use('ggplot')
sys.path.append('tables')

from session import Session

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
                                                  Session.starttime >= '2011-01-04',\
                                                  Session.starttime <= '2011-01-05').filter(\
                                                                                            Session.userid >= '56135a80-0000-0000-0000-000000000000',\
                                                                                            Session.userid <=  '56135a80-ffff-ffff-ffff-ffffffffffff')

    with open('userInfo.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        #writer.writerow(['la la']*5)
        for item in session_res:
            writer.writerow([item.sessionid])
        #print (item.sessionid, item.starttime, item.endtime)

#    ts = pd.Series(np.random.rand(1000), index=pd.date_range('1/1/2000', periods=1000))
#    ts = ts.cumsum()
#    ts.plot()

    dbsession.close()

if __name__ == "__main__":
    main()
