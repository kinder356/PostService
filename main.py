import sqlite3
import json
from interface import *


class Properties:
    database_filename = ''

    def __init__(self, input=dict()):
        self.database_filename = input.get("database_filename")


class PostServiceAPI:
    def __init__(self):
        with open("properties.json", 'r') as open_file:
            self.properties = json.load(open_file, object_hook=Properties)
        db_filename = self.properties.database_filename
        self.conn = sqlite3.connect(db_filename)
        self.cur = self.conn.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
           userid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
           login TEXT UNIQUE NOT NULL,
           password TEXT NOT NULL,
           name TEXT NOT NULL,
           surname TEXT NOT NULL,
           phone TEXT UNIQUE,
           email TEXT UNIQUE,
           birthdate DATE);
        """)

        self.cur.execute("""CREATE TABLE IF NOT EXISTS addresses(
           addressid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
           country TEXT,
           city TEXT,
           street TEXT,
           house TEXT,
           flat TEXT,
           postindex INTEGER NOT NULL,
           commentary TEXT);
        """)
        self.cur.execute("""CREATE TABLE IF NOT EXISTS orders(
           orderid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
           info TEXT NOT NULL,
           description TEXT,
           senderid INTEGER NOT NULL,
           courierid INTEGER NOT NULL,
           addressid INTEGER NOT NULL);
        """)

        # cur.execute("""ALTER TABLE users ADD COLUMN status INTEGER""")
        # cur.execute("""ALTER TABLE orders ADD COLUMN status INTEGER""")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS orderstatuses(
           id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
           status TEXT NOT NULL UNIQUE);
        """)

        self.cur.execute("""CREATE TABLE IF NOT EXISTS userstatuses(
           id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
           status TEXT NOT NULL UNIQUE);
        """)

    def setup_interface(self) -> None:
        window = Window(self)
        window.mainloop()

    def get_all_users(self) -> list:
        self.cur.execute("SELECT * FROM users")
        rows = self.cur.fetchall()
        for row in rows:
            user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            user._id = row[0]
            user._login = row[1]
            user._password = row[2]
            user._name = row[3]
            user._surname = row[4]
            user._phone = row[5]
            user._email = row[6]
            user._birthdate = row[7]
            user._status = row[8]
            yield user

    def add_new_user(self, user: User) -> None:
        self.cur.execute(
            "INSERT INTO users (login, password, name, surname, phone, email, birthdate, status) values (?,?,?,?,?,?,?,?)",
            (user.login, user.password, user.name, user.surname, user.phone, user.email, user.birthdate,
             user.status))
        self.conn.commit()

    def get_user_statuses(self) -> dict[str: int]:
        self.cur.execute("SELECT * FROM userstatuses")
        return dict((v, k) for k, v in self.cur.fetchall())

    def edit_user(self, user: User) -> None:
        self.cur.execute(
            "UPDATE users SET login=?, password=?, name=?, surname=?, phone=?, email=?, birthdate=?, status=? WHERE userid=?",
            (user.login, user.password, user.name, user.surname, user.phone, user.email, user.birthdate,
             user.status, user.id))

    def get_user_by_id(self, id: int) -> User:
        self.cur.execute("SELECT * FROM users WHERE userid=?", (id,))
        return User(*self.cur.fetchone())

    def delete_user_by_id(self, id: int) -> None:
        self.get_user_by_id(id)  # check id in db
        self.cur.execute("DELETE FROM users WHERE userid=?", (id,))
        self.conn.commit()

    def add_address(self, address: Address) -> None:
        self.cur.execute(
            "INSERT INTO addresses (country, city, street, house, flat, postindex, commentary) values (?, ?, ?, ?, ?, ?, ?)",
            (
                address.country, address.city, address.street, address.house, address.flat, address.post_index,
                address.commentary))
        self.conn.commit()

    def get_address_by_id(self, id: int) -> Address:
        self.cur.execute("SELECT * FROM addresses WHERE addressid=?", (id,))
        return Address(*self.cur.fetchone())

    def delete_address_by_id(self, id: int) -> None:
        self.get_address_by_id(id)  # check id in db
        self.cur.execute("DELETE FROM addresses WHERE addressid=?", (id,))
        self.conn.commit()

    def get_all_addresses(self) -> list[Address]:
        self.cur.execute("SELECT * FROM addresses")
        rows = self.cur.fetchall()
        for row in rows:
            address = Address(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            yield address

    def get_order_statuses(self) -> dict[str: int]:
        self.cur.execute("SELECT * FROM orderstatuses")
        return dict((v, k) for k, v in self.cur.fetchall())

    def get_all_orders(self) -> list[Order]:
        self.cur.execute("SELECT * FROM orders")
        rows = self.cur.fetchall()
        for row in rows:
            order = Order(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            yield order

    def get_order_by_id(self, id: int) -> Order:
        self.cur.execute("SELECT * FROM orders WHERE orderid=?", (id,))
        return Order(*self.cur.fetchone())

    def add_order(self, order: Order) -> None:
        self.cur.execute(
            "INSERT INTO orders (info, description, senderid, courierid, addressid, status) values (?, ?, ?, ?, ?, ?)",
            (order.info, order.description, order.sender_id, order.courier_id, order.address_id, order.status))
        self.conn.commit()

    def delete_order_by_id(self, id: int) -> None:
        self.get_order_by_id(id)  # check id in db
        self.cur.execute("DELETE FROM orders WHERE orderid=?", (id,))
        self.conn.commit()

    def change_order_status(self, id: int, status: int) -> None:
        self.cur.execute(
            "UPDATE orders SET status=? WHERE orderid=?", (status, id))


API = PostServiceAPI()
API.setup_interface()
