import sqlite3

def create_table():
    query = """CREATE TABLE IF NOT EXISTS pablo(
        datetime TEXT NOT NULL,
        count INTEGER NOT NULL
    )"""
    conn = None
    try:
        conn = sqlite3.connect("pablo.db")
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        print("Table created successfully.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"General error: {e}")
    finally:
        if conn:
            conn.close()

create_table()

