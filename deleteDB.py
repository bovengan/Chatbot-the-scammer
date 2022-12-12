import sqlite3

sqliteConnection = sqlite3.connect('chatbot.db')
cursor = sqliteConnection.cursor()
cursor.execute("DROP TABLE Users")
sqliteConnection.commit()
sqliteConnection.close()

""" Useful commands """
"""
cursor.execute("INSERT INTO Users VALUES ('Daniel', 24, 40)")
cursor.execute("SELECT * FROM Users WHERE name='Daniel'")
cursor.execute("DROP TABLE Users")
print(cursor.fetchall())
"""