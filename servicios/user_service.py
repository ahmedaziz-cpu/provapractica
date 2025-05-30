from conexion.db import connection_db
from esquemas.user import user_schema, users_schema

def get_users():
    conn = connection_db()
    cursor = conn.cursor()
    sql_read = "SELECT id, name, email FROM users"
    cursor.execute(sql_read)
    result = cursor.fetchall()
    conn.close()
    return users_schema(result)

def get_user(user_id: int):
    conn = connection_db()
    cursor = conn.cursor()
    sql_read = "SELECT id, name, email FROM users WHERE id = %s"
    cursor.execute(sql_read, (user_id,))
    result = cursor.fetchone()
    conn.close()
    return user_schema(result) if result else None

def create_user(data: dict):
    conn = connection_db()
    cursor = conn.cursor()
    sql_insert = "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id"
    cursor.execute(sql_insert, (data["name"], data["email"]))
    new_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return {"id": new_id, **data}

def update_user(user_id: int, data: dict):
    conn = connection_db()
    cursor = conn.cursor()
    sql_update = "UPDATE users SET name = %s, email = %s WHERE id = %s"
    cursor.execute(sql_update, (data["name"], data["email"], user_id))
    conn.commit()
    conn.close()
    return {"id": user_id, **data}

def delete_user(user_id: int):
    conn = connection_db()
    cursor = conn.cursor()
    sql_delete = "DELETE FROM users WHERE id = %s"
    cursor.execute(sql_delete, (user_id,))
    conn.commit()
    conn.close()