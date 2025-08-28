import sqlite3


def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY,
                       name
                       TEXT
                       NOT
                       NULL,
                       age
                       INTEGER
                       NOT
                       NULL,
                       hobby
                       TEXT
                   )
                   ''')
    conn.commit()
    conn.close()


def add_user(name, age, hobby=None):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
                   INSERT INTO users (name, age, hobby)
                   VALUES (?, ?, ?)
                   ''', (name, age, hobby))
    conn.commit()
    conn.close()


def get_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users


def update_user(user_id, name=None, age=None, hobby=None):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    updates = []
    params = []

    if name is not None:
        updates.append("name = ?")
        params.append(name)
    if age is not None:
        updates.append("age = ?")
        params.append(age)
    if hobby is not None:
        updates.append("hobby = ?")
        params.append(hobby)

    if updates:
        query = "UPDATE users SET " + ", ".join(updates) + " WHERE id = ?"
        params.append(user_id)
        cursor.execute(query, tuple(params))
        conn.commit()

    conn.close()


def delete_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()


def get_user_by_id(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()

    if user:
        print(f"Пользователь найден! ID: {user[0]}, Имя: {user[1]}, Возраст: {user[2]}, Хобби: {user[3]}")
    else:
        print(f"Пользователь с ID {user_id} не найден.")


#Пример использования
if __name__ == '__main__':
    init_db()

    add_user("Алексей", 30, "чтение")
    add_user("Мария", 25, "рисование")
    add_user("Иван", 40)

    print("Все пользователи:")
    all_users = get_users()
    for user in all_users:
        print(user)
    print("-" * 20)

    get_user_by_id(1)
    get_user_by_id(2)
    get_user_by_id(99)

    delete_user(1)
    delete_user(2)
    delete_user(3)