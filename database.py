import sqlite3
import config


def connect():
    conn = sqlite3.connect(config.database_name)
    return conn, conn.cursor()


def save(conn):
    conn.commit()
    conn.close()


def create_database():
    conn, cursor = connect()
    sql = """CREATE TABLE inventory (id integer primary key not null,
        item_name text NOT NULL,
        item_price real NOT NULL,
        item_pic text NOT NULL
        )"""
    cursor.execute(sql)
    save(conn)


def add_product(item_name, item_price, item_pic):
    conn, cursor = connect()
    # item_pic should be filename of the picture stored in static
    sql = """INSERT INTO inventory (item_name, item_price, item_pic)
        VALUES (?,?,?)"""
    cursor.execute(sql, (item_name, item_price, item_pic))
    save(conn)


def get_products():
    conn, cursor = connect()
    sql = """SELECT * FROM inventory"""
    cursor.execute(sql)
    products = cursor.fetchall()
    save(conn)
    return products


def delete_product(product_id):
    conn, cursor = connect()
    sql = """DELETE FROM inventory WHERE id=?"""
    cursor.execute(sql, (product_id,))
    save(conn)


if __name__ == "__main__":
    create_database()