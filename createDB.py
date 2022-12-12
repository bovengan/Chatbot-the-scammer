import sqlite3
from sqlite3 import OperationalError

sqliteConnection = sqlite3.connect('chatbot.db')
cursor = sqliteConnection.cursor()

try:
    cursor.execute("CREATE TABLE Users (id int, age int, tickets int)")
    sqliteConnection.commit()
    print('New table created')
except OperationalError:
    print('Table already exists')
sqliteConnection.commit()
sqliteConnection.close()
