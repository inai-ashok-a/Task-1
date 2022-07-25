from fastapi import FastAPI
from config.db import con
from schemas.users import User,check_email
from models.users import users


app=FastAPI();    #creating object for FastAPI()

@app.post("/")
async def root():
    return {"message": "Hello World"}

@app.get('/api/users')                                  #used to fetch data from my sql
async def index():                                      #asynchronous function
    data=con.execute(users.select()).fetchall()         #quey statement to fetch data from mysql
    return data                                         #returning the state of object

@app.post('/api/users')
async def store(obj:User):

       data=con.execute(users.select().where (users.c.email == obj.email)).fetchall()
       #condition to check whether the email present in mysql already


       if check_email(obj.email) and (data.__len__()==0): #check_email is a function used to validate email
        data=con.execute(users.insert().values(
        name=obj.name,
        age=obj.age,                        #query to insert data in the database
        email=obj.email
        ))
        data=con.execute(users.select()).fetchall()
        return data
       else:
           return "False"


@app.put('/api/users/{id}')
async def func_to_update(id:int,obj:User):   #asynchronous function to update the date to my sql

    data = con.execute(users.select().where(users.c.email == obj.email)).fetchall() #refer the above statement

    if check_email(obj.email) and (data.__len__() == 0):

        data=con.execute(users.update().values(
        name=obj.name,
        age=obj.age,
        email=obj.email,
        ).where(users.c.id == id))
        data = con.execute(users.select()).fetchall()
        return data

    else:
        return "False"


@app.delete('/api/users/{id}')             #asynchronous function to delete the data from the database
async def delete(id:int):
    data=con.execute(users.delete().where(users.c.id==id))
    data = con.execute(users.select()).fetchall()
    return data
