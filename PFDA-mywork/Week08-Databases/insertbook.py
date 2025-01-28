import sqlite3

con = sqlite3.connect('pfda.db')
cur = con.cursor()

sql = "select * from book"
result = cur.execute(sql)
print(f"first row: {result.fetchone()}")

sql = """INSERT INTO book VALUES
        ('Book 1', 'Author 1', '123456'),
        ('Book 2', 'Author 2', '234567')
"""
cur.execute(sql)
con.commit()

sql = "select * from book"
result = cur.execute(sql)
print(f"first row: {result.fetchone()}")

con.close()