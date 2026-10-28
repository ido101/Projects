import sqlite3
import os
os.chdir(r"C:\Users\IDO123\Downloads\blackbox7\secret2")
con = sqlite3.connect("game_database.db")
cur = con.cursor()
cur.execute("INSERT INTO users VALUES (1, 'Ido', '123')")
res = cur.execute("SELECT * FROM users")
print(res.fetchone())
con.commit()