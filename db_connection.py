import sqlite3

# Connecting to database


try:
    sqlite_connection = sqlite3.connect('fantasy_football.db')
    cursor = sqlite_connection.cursor()
    print('DB init')

    query = 'select sqlite_version();'
    cursor.execute(query)

    result = cursor.fetchall()
    print(f'SQLite version is {result}')

except sqlite3.Error as error:
    print(f'Error - {error}')

finally:
    if sqlite_connection:
        sqlite_connection.close()
        print('SQLite connection closed.')
