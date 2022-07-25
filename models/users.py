from config.db import meta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String


users=Table(
    'user_data',meta,
    Column('id',Integer),
    Column('name',String(255)),
    Column('age',Integer),
    Column('email',String(255)),

)