import sqlite3

# Name of database, pfda.db
con = sqlite3.connect('pfda.db')
cur = con.cursor()

sql = "Create TABLE book(title, author, ISBN)"
cur.execute(sql)

con.close()