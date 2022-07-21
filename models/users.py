from config.db import meta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String


users=Table(
    'users',meta,
    Column('id',Integer),
    Column('name',String(255)),
    Column('email',String(255)),

)