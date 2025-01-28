import sqlite3

con = sqlite3.connect('pfda.db')
cur = con.cursor()

for row in cur.execute("SELECT * from book"):
    print(f"row{row}")