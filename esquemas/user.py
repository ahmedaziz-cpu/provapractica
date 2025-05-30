def user_schema(user) -> dict:
    return {
        "id": user[0],
        "name": user[1],
        "email": user[2]
    }

def users_schema(users) -> list[dict]:
    return [user_schema(user) for user in users]
