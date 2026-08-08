import sqlite3 as s

conn = s.connect('trial.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS customers (
    First_name text,
    password text
)""")
conn.commit()
conn.close()


