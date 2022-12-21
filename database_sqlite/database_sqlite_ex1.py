import sqlite3  # sqlite import ediyoruz

# If the database example.db exists, it connects, if not, it creates the database and connects

connect = sqlite3.connect("example.db")

cursor = connect.cursor()

# If the table exists, it does not operate, otherwise it creates

cursor.execute("CREATE TABLE IF NOT EXISTS team(name TEXT, age INT, gender TEXT)")

# data insertion example

cursor.execute("INSERT INTO team VALUES('name1',25,'F')")
cursor.execute("INSERT INTO team VALUES('name2',29,'M')")
cursor.execute("INSERT INTO team VALUES('name3',35,'F')")

connect.commit()  # we sent the connect
connect.close()
