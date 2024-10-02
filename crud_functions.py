import sqlite3

connection = sqlite3.connect("Products.db")
cursor = connection.cursor()


def database_creation():
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Products(
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT,
                    price INTEGER NOT NULL
                );
            ''')
    connection.commit()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Users(
                    id INT PRIMARY KEY,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    age INT NOT NULL,
                    balance INT DEFAULT 1000
                );
            ''')
    connection.commit()


def initiate_database(product_id, title, descript, price):
    check_id = cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
    if check_id.fetchone() is None:
        cursor.execute('''
        INSERT INTO Products (id, title, description, price)
         VALUES(?, ?, ?, ?)
    ''', (product_id, title, descript, price))
    connection.commit()


def get_all_products():
    products = cursor.execute(" SELECT id, title, description, price FROM Products").fetchall()
    return products


def add_user(username, email, age):
    check_name = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if check_name.fetchone() is None:
        cursor.execute('''
        INSERT INTO Users (username, email, age)
        VALUES(?, ?, ?)       
    ''', (username, email, age))
    connection.commit()


def is_included(username):
    user_check = cursor.execute("SELECT username FROM Users WHERE username = ?",
                                (username,)).fetchone()
    if user_check:
        return True
    else:
        return False


database_creation()
# for i in range(4):
#    initiate_database(i + 1, f'Продукт {i + 1}', f'описание {i + 1}', f'{(i + 1) * 100}')
