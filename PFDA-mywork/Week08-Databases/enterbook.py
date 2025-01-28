import sqlite3

con = sqlite3.connect('pfda.db')
cur = con.cursor()

book = {}

book['title'] =  input("Please enter book title:")
book['author'] =  input("Please enter book author:")
book['ISBN'] =  input("Please enter book ISBN:")

data = [book]

sql = "INSERT into book VALUES (:title, :author, :ISBN)"
cur.executemany(sql, data)
con.commit()

for row in cur.execute("SELECT * FROM book"):
    print(f"row {row}")