from fastapi import FastAPI, HTTPException
from typing import Optional
from typing import List
from pydantic import BaseModel
from model import User, Gender, Role, UserUpdateRequest
from uuid import UUID, uuid4

app = FastAPI()

db: list[User] = [
    User(
        id=uuid4(),
        first_name="raghul",
        last_name="v",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
    User(
        id=uuid4(),
        first_name="sunil",
        last_name="v",
        gender=Gender.male,
        roles=[Role.student]
    )
]


@app.get("/api/users")
def users():
    return db


@app.post("/api/users")
def addUser(user: User):
    db.append(user)
    return {"id": user.id}


@app.put("/api/users/{user_id}")
def updateUser(user_update: UserUpdateRequest, user_id: UUID) -> None:
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return  # Move the return statement outside the loop

    raise HTTPException(
        status_code=404,
        detail=f"user with id:{user_id} does not exist"
    )

@app.delete("/api/users{user_id}")
def deleteUser(user_id:UUID):
    for user in db:
        if user.id==user_id:
            db.remove(user)
            return{ "msg":"Delete"}
    raise HTTPException(
        status_code=408,
        detail=f"User with id:{user_id}does not exists"
    )
