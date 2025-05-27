from lib.db.connection import get_connection

def setup_database():
    with open('lib/db/schema.sql', 'r') as f:
        schema_sql = f.read()
    
    conn = get_connection()
    conn.executescript(schema_sql)
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Database schema created.")