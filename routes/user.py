from fastapi import APIRouter
from schemas.user import userEntity, usersEntity
from bson import ObjectId
from models.user import User
from config.db import conn


user = APIRouter()

@user.get('/users')
async def findUsers():
    return  usersEntity(conn.local.user.find())


@user.post('/')
async def createUser(user: User):
    conn.local.user.insert_one(dict(user))
    return  usersEntity(conn.local.user.find())


@user.put('/{id}')
async def updateUser(id,user: User):
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set": dict(user)
    })
    return  usersEntity(conn.local.user.find_one({"_id":ObjectId(id)}))    


@user.delete('/{id}')
async def deleteUser(id,user: User):
    return  usersEntity(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))        

