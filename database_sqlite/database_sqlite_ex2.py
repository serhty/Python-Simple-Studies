import sqlite3  # sqlite import ediyoruz

# If the database example.db exists, it connects, if not, it creates the database and connects
#If we make the connection with with, there is no need for the close() operation at the end of the page. with already does the closing itself.

with sqlite3.connect("example.db") as connect:

    cursor = connect.cursor()

    # reading data
    
    cursor.execute("SELECT * FROM team")  # We get all data with *
    for data in cursor.fetchall():
        print(data)

    connect.commit()  # we sent the connect
