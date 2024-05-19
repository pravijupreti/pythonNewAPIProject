from fastapi import APIRouter
from modules.user import User
from config.db import conn
from schemas.user import userEntity,usersEntity
from bson.objectid import ObjectId

user_router = APIRouter()

@user_router.get('/')
async def FindAllUsers(): 
    return usersEntity(conn.local.user.find())

@user_router.post('/')
async def createUsers(user: User): 
    conn.local.user.insert_one(dict(user))
    return user

@user_router.put('/{id}')
async def updateUser(id,user:User):
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return userEntity(conn.local.user.find_one({"_id":ObjectId(id)}))

@user_router.delete('/{id}')
async def DeleteUser(id):
    return userEntity(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))

@user_router.get('/{id}')
async def getUserById(id):
    return userEntity(conn.local.user.find_one({"_id":ObjectId(id)}))


