from fastapi import FastAPI
from config.db import con
from schemas.users import User
from models.users import users

app=FastAPI();

@app.post("/")
async def root():
    return {"message": "Hello World"}

@app.get('/api/users')
async def index():
    data=con.execute(users.select()).fetchall()
    return data

@app.post('/api/users')
async def store(obj:User):
    data=con.execute(users.insert().values(
        id=obj.id,
        name=obj.name,
        email=obj.email

    ))
    data=con.execute(users.select()).fetchall()
    return data


@app.put('/api/users/{id}')
async def func_to_update(id:int,obj:User):
    data=con.execute(users.update().values(
        name=obj.name,
        email=obj.email,
    ).where(users.c.id==id))
    data = con.execute(users.select()).fetchall()
    return data


@app.delete('/api/users/{id}')
async def delete(id:int):
    data=con.execute(users.delete().where(users.c.id==id))
    data = con.execute(users.select()).fetchall()
    return data
