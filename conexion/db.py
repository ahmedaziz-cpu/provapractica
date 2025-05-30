import psycopg2

def connection_db():
    conn = psycopg2.connect(
        database="practica",
        user="user",
        password="pass",
        host="localhost",  # <- como FastAPI corre fuera del contenedor, se usa localhost
        port="3456"         # <- el puerto que expusiste en Docker
    )
    print("Connexió establerta correctament")
    return conn
