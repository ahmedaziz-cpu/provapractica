from connexion.db import connection_db

def create_tables():
    print("🔧 Creando tablas...")
    conn = connection_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    print("✅ Tablas listas")

