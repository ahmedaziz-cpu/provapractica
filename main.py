from fastapi import FastAPI
from typing import Dict
from servicios.user_service import get_users, get_user, create_user, update_user, delete_user
from servicios.createtables import create_tables
from esquemas.user import user_schema, users_schema

app = FastAPI()

@app.on_event("startup")
def startup_event():
    create_tables()

@app.get("/users")
async def read_users():
    users = get_users()
    return users_schema(users)

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    user = get_user(user_id)
    if not user:
        return {"error": "User not found"}
    return user_schema(user)

@app.post("/users")
async def create_new_user(data: Dict):
    return create_user(data)

@app.put("/users/{user_id}")
async def update_existing_user(user_id: int, data: Dict):
    existing = get_user(user_id)
    if not existing:
        return {"error": "no hay usuario"}
    return update_user(user_id, data)

@app.delete("/users/{user_id}")
async def delete_existing_user(user_id: int):
    existing = get_user(user_id)
    if not existing:
        return {"error": "no hay usuario"}
    delete_user(user_id)
    return {"detail": "User deleted"}
