import sqlite3

def connection_db(name_database):
    connec_db = None
    try:
        connec_db = sqlite3.connect(name_database)
        
    except sqlite3.Error() as e:
        print(e)
    return connec_db

def create_table(connec_db, sql):
    try:
        cursor = connec_db.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_product(conncer_db, product):
    sql = '''INSERT INTO products 
    (product_title, price, quantity)
    VALUES ("potato", 45, 100), 
    ("onion", 15, 60),
    ("beet", 80, 23),
    ("cabbage", 55, 15),
    ("carrot", 25, 100),
    ("tomato", 140, 50),
    ("banan", 120, 50), 
    ("apple", 155, 45),
    ("mushroom", 180, 15),
    ("pumpkin", 148, 40),
    ("pepper", 250, 24),
    ("garlic", 135, 5),
    ("corn", 90, 10),
    ("cucumber", 130, 35),
    ("beans", 55, 150);
    
     
    '''
    try:
        cursor = conncer_db.cursor()
        cursor.execute(sql, product)
        conncer_db.commit()
    except sqlite3.Error as e:
        print(e)


def update_quantity(connec_db, product):
    sql = '''UPDATE products SET quantity = ?
    WHERE id = ?'''
    try:
        cursor = connec_db.cursor()
        cursor.execute(sql, product)
        connec_db.commit()
    except sqlite3.Error as e:
        print(e)

def update_price(connec_db, product):
    sql = '''UPDATE products SET price = ?
    WHERE id = ?'''
    try:
        cursor = connec_db.cursor()
        cursor.execute(sql, product)
        connec_db.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(connec_db, id):
    sql = '''DELETE from products WHERE id = ?'''
    try:
        cursor = connec_db.cursor()
        cursor.execute(sql, (id,))
        connec_db.commit()
    except sqlite3.Error as e:
        print(e)




create_produkts_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

def get_all_list_product(connec_db):
    sql = '''SELECT * FROM products'''
    try:
        cursor = connec_db.cursor()
        cursor.execute(sql)
        get_all = cursor.fetchall()

        for prod in get_all:
            print(prod)
    except sqlite3.Error as e:
        print(e)


def select_product_by(connec_db, by_price, by_quantity):
    sql = '''SELECT * FROM products WHERE price <= ? and quantity >= ? '''
    try:
        cursor = connec_db.cursor()
        cursor.execute(sql, (by_price, by_quantity))
        prod_list = cursor.fetchall()

        for prod in prod_list:
            print(prod)
    except sqlite3.Error as e:
        print(e)

def surche_product(connec_db, value):
    sql = '''SELECT * FROM products WHERE product_title LIKE '%value%' '''
    try:
        cursor = connec_db.cursor()
        cursor.execute(sql, (value, ))
        prod_list = cursor.fetchall()

        for prod in prod_list:
            print(prod)
    except sqlite3.Error as e:
        print(e)

conn_database = connection_db("hw.db")
if conn_database != None:
    print("The connection is established")
    #create_table(conn_database, create_produkts_table)
    #insert_product(conn_database, ())
    #update_quantity(conn_database, (100, 1))
    #update_price(conn_database, (300, 1))
    #delete_product(conn_database, 2)
    # get_all_list_product(conn_database)
    #select_product_by(conn_database, 100,10)
    surche_product(conn_database, "an")

    conn_database.close()