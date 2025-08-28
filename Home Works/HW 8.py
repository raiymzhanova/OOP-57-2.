import sqlite3

def init_db():

    conn = sqlite3.connect('university.db')
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
                       NULL
                   )
                   ''')

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS grades
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY,
                       user_id
                       INTEGER,
                       subject
                       TEXT
                       NOT
                       NULL,
                       grade
                       INTEGER
                       NOT
                       NULL,
                       FOREIGN
                       KEY
                   (
                       user_id
                   ) REFERENCES users
                   (
                       id
                   )
                       )
                   ''')
    conn.commit()
    conn.close()


def seed_db():
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()

    users = [
        ('Алексей', 25),
        ('Мария', 19),
        ('Иван', 22),
        ('Елена', 30),
        ('Петр', 20)
    ]
    cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users)

    grades = [
        (1, 'Математика', 5),
        (1, 'Физика', 4),
        (2, 'Химия', 5),
        (3, 'Математика', 3),
        (4, 'Физика', 5),
        (4, 'Химия', 4),
        (5, 'Математика', 2)
    ]
    cursor.executemany("INSERT INTO grades (user_id, subject, grade) VALUES (?, ?, ?)", grades)

    conn.commit()
    conn.close()


def create_view():

    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE VIEW IF NOT EXISTS users_over_20_with_grades AS
                   SELECT users.name, users.age, grades.subject, grades.grade
                   FROM users
                            LEFT JOIN grades ON users.id = grades.user_id
                   WHERE users.age > 20
                   ''')
    conn.commit()
    conn.close()


def get_from_view():

    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()

    print("Данные из представления 'users_over_20_with_grades':")
    cursor.execute("SELECT * FROM users_over_20_with_grades")
    for row in cursor.fetchall():
        print(f"Имя: {row[0]}, Возраст: {row[1]}, Предмет: {row[2]}, Оценка: {row[3]}")

    conn.close()


# --- Вызов функций ---
if __name__ == "__main__":
    init_db()
    # Запускаем только один раз, чтобы наполнить базу данных
    # seed_db()
    create_view()
    get_from_view()