import sqlite3

connection = sqlite3.connect("Products.db")
cursor = connection.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products(
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                price INTEGER NOT NULL
            );
        ''')
connection.commit()


def initiate_database(product_id, title, descript, price):
    check_id = cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))

    if check_id.fetchone() is None:
        cursor.execute(f'''
    INSERT INTO Products VALUES('{product_id}', '{title}', '{descript}', '{price}')
''')
    connection.commit()


def get_all_products():
    cursor.execute(" SELECT id, title, description, price FROM Products")
    products = cursor.fetchall()
    return products

# for i in range(4):
#    initiate_database(i + 1, f'Продукт {i + 1}', f'описание {i + 1}', f'{(i + 1) * 100}')
