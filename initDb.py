import sqlite3

connection = sqlite3.connect('testDatabase.db')

with open('residentsSchema.sql') as file:
    connection.executescript(file.read())

c = connection.cursor()

c.execute("INSERT INTO residents (residentName, age) VALUES (?, ?)",
            ('Jerry', 21)
            )

c.execute("INSERT INTO residents (residentName, age) VALUES (?, ?)",
            ('Sam', 22)
            )
c.execute("INSERT INTO residents (residentName, age) VALUES (?, ?)",
            ('Will', 22)
            )

connection.commit()
connection.close()