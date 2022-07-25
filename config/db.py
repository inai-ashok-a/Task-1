
from sqlalchemy import create_engine,MetaData

engine=create_engine('mysql+pymysql://root:Ashoksql@localhost:3306/ashoksql')
meta=MetaData()
con=engine.connect()