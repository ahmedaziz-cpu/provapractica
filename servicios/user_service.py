from connexion.db import connection_db
from esquemas.user import User

def get_users():
    conn = connection_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users")
    rows = cur.fetchall()
    conn.close()
    return [User(id=row[0], name=row[1], email=row[2]) for row in rows]

def get_user(user_id: int):
    conn = connection_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return User(id=row[0], name=row[1], email=row[2])
    return None

def create_user(user: User):
    conn = connection_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id", (user.name, user.email))
    new_id = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return User(id=new_id, name=user.name, email=user.email)

def update_user(user_id: int, user: User):
    conn = connection_db()
    cur = conn.cursor()
    cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (user.name, user.email, user_id))
    conn.commit()
    conn.close()
    return User(id=user_id, name=user.name, email=user.email)

def delete_user(user_id: int):
    conn = connection_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    conn.close()
