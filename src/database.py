import psycopg2

def connect_db():
    return psycopg2.connect(
        dbname="earnings_db",
        user="your_user",
        password="your_password",
        host="localhost",
        port="5432"
    )

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS population (
            id SERIAL PRIMARY KEY,
            name TEXT,
            gender TEXT,
            dob DATE,
            salary FLOAT
        )
    """)
    conn.commit()
    conn.close()
