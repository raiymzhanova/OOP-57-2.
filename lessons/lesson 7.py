    import sqlite3


    connect = sqlite3.connect("users.db")

    cursor = connect.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXIST users (  команды эскьюэл
            name VARCHAR(100) NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT,
            
             ''')
        connect.commit()
