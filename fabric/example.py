from db import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("""
SELECT * FROM artists;
""")

for row in cur.fetchall():
    print(row)

conn.close()
