from fastapi import FastAPI, HTTPException
from sqlalchemy.testing.suite.test_reflection import users

from esquemas.user import User
from servicios.user_service import get_users, get_user, create_user, update_user, delete_user
from servicios.createtables import create_tables

app = FastAPI()

@app.on_event("startup")
def startup_event():
    create_tables()

@app.get("/users", response_model=list[User])
async def read_users():
    ##result = users.get_users()
    return get_users()


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    user = get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users", response_model=User)
async def create_new_user(user: User):
    return create_user(user)

@app.put("/users/{user_id}", response_model=User)
async def update_existing_user(user_id: int, user: User):
    existing_user = get_user(user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return update_user(user_id, user)

@app.delete("/users/{user_id}")
async def delete_existing_user(user_id: int):
    existing_user = get_user(user_id)
    if existing_user is None:#ss
        raise HTTPException(status_code=404, detail="User not found")
    delete_user(user_id)#ksk
    return {"detail": "User deleted"}