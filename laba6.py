import sqlite3 
 
def create_data_basa(): 
    conn = sqlite3.connect('myBasa.db') 
    cursor = conn.cursor() 
 
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS users ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL, 
        age INTEGER 
    ); 
    ''') 
 
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS products ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL, 
        price INTEGER 
    ); 
    ''') 
 
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS email ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        email TEXT NOT NULL, 
        logo TEXT 
    ); 
    ''') 
 
    cursor.execute("INSERT INTO users (name, age) VALUES ('Николай', 30);") 
    cursor.execute("INSERT INTO users (name, age) VALUES ('Виталий', 20);") 
    cursor.execute("INSERT INTO users (name, age) VALUES ('Андрей', 24);") 
 
 
 
    cursor.execute("INSERT INTO email (email, logo) VALUES ('andrey456@mail.com', 'Rubby');") 
    cursor.execute("INSERT INTO email (email, logo) VALUES ('tankionline@yandex.com', 'ken');") 
    cursor.execute("INSERT INTO email (email, logo) VALUES ('damagextra@gmail.com', 'barby');") 
 
 
    cursor.execute("INSERT INTO products (name, price) VALUES ('PC', 575);") 
    cursor.execute("INSERT INTO products (name, price) VALUES ('mobile', 499);") 
    cursor.execute("INSERT INTO products (name, price) VALUES ('PC', 600);") 
 
    conn.commit() 
    conn.close() 
 
    print("БД создана") 
 
create_data_basa()

import sqlite3 
 
 
def insert_to_tables(tables_data): 
    conn = sqlite3.connect('myBasa.db') 
    cursor = conn.cursor() 
 
    try: 
        for table_name, data in tables_data.items(): 
            if not data: 
                continue 
 
           
            placeholders = ', '.join(['?'] * len(data[0])) 
            query = f'INSERT INTO {table_name} VALUES ({placeholders})' 
 
            cursor.executemany(query, data) 
 
        conn.commit() 
        print("Данные успешно вставлены.") 
 
    except sqlite3.Error as e: 
        print(f"Ошибка: {e}") 
        conn.rollback()
 
    finally: 
        conn.close() 
 
data = { 
    'users': [ 
        (4, 'Никита', 25), 
        (5, 'Виталий', 30), 
        (6, 'Николай', 20) 
    ], 
    'products': [ 
        (4, 'Laptop', 999), 
        (5, 'Smartphone', 599), 
        (6, 'Smartphone', 599) 
    ], 
    'email': [ 
            (4, 'killer@mail.com', 'nik'), 
            (5, 'killer2@mail.com', 'vilka'), 
            (6, 'killer3@mail.com', 'sber') 
        ] 
} 
 
insert_to_tables(data)
