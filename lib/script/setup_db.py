from lib.db.connection import get_connection

def setup_database():
    with open("lib/db/schema.sql") as f:
        schema = f.read()

    conn = get_connection()
    conn.executescript(schema)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
