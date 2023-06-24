from tkinter import *
from tkinter import ttk
from settings import Settings
from time import sleep
from threading import Thread
import datetime
import re


class User:
    _id = 0
    _login = ''
    _password = ''
    _name = ''
    _surname = ''
    _phone = None
    _email = None
    _birthdate = None
    _status = 2

    # ...

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if type(value) == int:
            self._id = value
        else:
            raise TypeError()

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value: str):
        if type(value) != str:
            raise TypeError()
        if len(value) < 8:
            raise TypeError()
        symbols = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+?/><.,~`'
        for i in value.lower():
            if i not in symbols:
                raise TypeError()
        self._login = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if type(value) != str:
            raise TypeError()
        if len(value) < 8:
            raise TypeError()
        symbols = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+?/><.,~`'
        for i in value.lower():
            if i not in symbols:
                raise TypeError()
        self._password = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if type(value) != str:
            raise TypeError()
        if len(value) == 0:
            raise TypeError()
        check = [True, True]
        letters_eng = 'abcdefghijklmnopqrstuvwxyz'
        letters_ru = 'абвгдежзийклмнопрстуфхцчшщьыъэюя'
        for i in value.lower():
            if i not in letters_eng:
                check[0] = False
        for i in value.lower():
            if i not in letters_ru:
                check[1] = False
        if not check[0] and not check[1]:
            raise TypeError()
        if value[0].islower():
            raise TypeError()
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        if type(value) != str:
            raise TypeError()
        if len(value) == 0:
            raise TypeError()
        check = [True, True]
        letters_eng = 'abcdefghijklmnopqrstuvwxyz'
        letters_ru = 'абвгдежзийклмнопрстуфхцчшщьыъэюя'
        for i in value.lower():
            if i not in letters_eng:
                check[0] = False
        for i in value.lower():
            if i not in letters_ru:
                check[1] = False
        if not check[0] and not check[1]:
            raise TypeError()
        if value[0].islower():
            raise TypeError()
        self._surname = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value: str):
        if value is None:
            self._phone = None
            return
        # и так далее...
        if type(value) != str:
            raise TypeError()
        if len(value) < 11:
            raise TypeError()
        if value[0] == '8':
            if not value.isnumeric() or not len(value) == 11:
                raise TypeError()
        elif value[0] == '+':
            if not value[1:].isnumeric():
                raise TypeError()
        self._phone = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        if value is None:
            self._email = None
            return
        # и так далее...
        if type(value) != str:
            raise TypeError()
        if len(value) < 7:
            raise TypeError()
        symbols = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+?/><.,~`'
        for i in value.lower():
            if i not in symbols:
                raise TypeError()
        if value.find('.', -4, -2) == -1:
            raise TypeError()
        if value.find('@', 1, -5) == -1:
            raise TypeError()
        self._email = value

    @property
    def birthdate(self):
        return self._birthdate

    @birthdate.setter
    def birthdate(self, value):
        if value is None:
            self._birthdate = None
            return
        # и так далее...
        if type(value) != str:
            raise TypeError()
        nums = list(map(int, value.split('-')))
        date = datetime.date(nums[0], nums[1], nums[2])
        if date > datetime.date.today():
            raise TypeError()
        self._birthdate = date

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if type(value) != int:
            raise TypeError()
        if value <= 0:
            raise TypeError()
        self._status = value

    def __init__(self, user_id, login, password, name, surname, phone, email, birthdate, status):
        self.id = user_id
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.birthdate = birthdate
        self.status = status

    def get_properties(self) -> tuple:
        return self.id, self.login, self.password, self.name, self.surname, self.phone, self.email, self.birthdate, self.status


class Address:
    _id = 0
    _country = ""
    _city = ""
    _street = ""
    _house = ""
    _flat = ""
    _post_index = ""
    _commentary = ""

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value):
        if value is None or type(value) != int:
            raise ValueError("invalid ID")
        self._id = value

    @property
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, value):
        if value == "":
            raise ValueError("invalid country")
        self._country = value

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, value):
        if value == "":
            raise ValueError("invalid city")
        self._city = value

    @property
    def street(self) -> str:
        return self._street

    @street.setter
    def street(self, value):
        if value == "":
            raise ValueError("invalid street")
        self._street = value

    @property
    def house(self) -> str:
        return self._house

    @house.setter
    def house(self, value):
        if value == "":
            raise ValueError("invalid house")
        self._house = value

    @property
    def flat(self) -> str:
        return self._flat

    @flat.setter
    def flat(self, value):
        if value == "":
            raise ValueError("invalid flat")
        self._flat = value

    @property
    def post_index(self) -> str:
        return self._post_index

    @post_index.setter
    def post_index(self, value):
        if value == "":
            raise ValueError("invalid post index")
        self._post_index = value

    @property
    def commentary(self) -> str:
        return self._commentary

    @commentary.setter
    def commentary(self, value):
        if value == "":
            raise ValueError("invalid commentary")
        self._commentary = value

    def __init__(self, address_id: int, country: str, city: str, street: str, house: str, flat: str, post_index: str,
                 commentary: str):
        self.id = address_id
        self.country = country
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat
        self.post_index = post_index
        self.commentary = commentary

    def get_properties(self) -> tuple:
        return self.id, self.country, self.city, self.street, self.house, self.flat, self.post_index, self.commentary


class Order:
    _id = 0
    _info = ""
    _description = ""
    _sender_id = 0
    _courier_id = 0
    _address_id = 0
    _status = 1

    @property
    def id(self) -> int:
        return self._id

    @property
    def info(self) -> str:
        return self._info

    @property
    def description(self) -> str:
        return self._description

    @property
    def sender_id(self) -> int:
        return self._sender_id

    @property
    def courier_id(self) -> int:
        return self._courier_id

    @property
    def address_id(self) -> int:
        return self._address_id

    @property
    def status(self) -> int:
        return self._status

    def __init__(self, id: int, info: str, description: str, sender_id: int, courier_id, address_id: int, status: int):
        self._id = id
        self._info = info
        self._description = description
        self._sender_id = sender_id
        self._courier_id = courier_id
        self._address_id = address_id
        self._status = status

    def get_properties(self) -> tuple:
        return self.id, self.info, self.description, self.sender_id, self.courier_id, self.address_id, self.status


class Window(Tk):

    def __init__(self, API):
        super().__init__()
        self.title("Post Service")
        self.geometry("1000x350+300+100")
        self.pack_propagate(False)

        # --- functions ---

        self.add_user_api_func = API.add_new_user
        self.get_all_users_api_func = API.get_all_users
        self.get_user_statuses_api_func = API.get_user_statuses
        self.edit_user_api_func = API.edit_user
        self.get_user_by_id_api_func = API.get_user_by_id
        self.delete_user_by_id_api_func = API.delete_user_by_id
        self.add_address_api_func = API.add_address
        self.delete_address_by_id_api_func = API.delete_address_by_id
        self.get_order_statuses_api_func = API.get_order_statuses
        self.add_order_api_func = API.add_order
        self.get_address_by_id_api_func = API.get_address_by_id
        self.delete_order_by_id_api_func = API.delete_order_by_id
        self.get_order_by_id_api_func = API.get_order_by_id
        self.change_order_status_api_func = API.change_order_status
        self.get_all_addresses_api_func = API.get_all_addresses
        self.get_all_orders_api_func = API.get_all_orders

        notebook = ttk.Notebook()
        notebook.pack(expand=True, fill=BOTH)

        # --- tabs start ---

        frame1 = ttk.Frame(notebook)
        frame1.pack()
        notebook.add(frame1, text="Просмотр базы данных")

        frame2 = ttk.Frame(notebook)
        frame2.pack()
        notebook.add(frame2, text="Добавление пользователя")

        frame3 = ttk.Frame(notebook)
        frame3.pack()
        notebook.add(frame3, text="Редактирование пользователя")

        frame4 = ttk.Frame(notebook)
        frame4.pack()
        notebook.add(frame4, text="Адреса")

        frame5 = ttk.Frame(notebook)
        frame5.pack()
        notebook.add(frame5, text="Заказы")

        # --- tab 5, add orders, delete orders ---

        order_container = Frame(frame5)
        order_container.pack()

        # - add order -

        child_frame_add_order = Frame(master=order_container)
        child_frame_add_order.pack(padx=30, side=LEFT)

        Label(child_frame_add_order, text="Добавление заказа", font=14).grid(row=0, column=0, columnspan=2, padx=20,
                                                                             pady=20)

        start_row = 1
        add_order_rows_properties = dict(info=("Информация: ", 0, False), description=("Описание: ", 1, False),
                                         sender_id=("id отправителя: ", 2, True),
                                         courier_id=("id курьера: ", 3, True),
                                         address_id=("id адреса", 4, True))
        self.add_order_properties_rows: dict = dict(
            ((k, Window.add_simple_property_row(child_frame_add_order, v[1] + start_row, v[0], v[2])) for k, v in
             add_order_rows_properties.items()))

        status_label = Label(master=child_frame_add_order, text="Статус: ")
        status_label.grid(row=5 + start_row, column=0)
        statuses_list = list(self.get_order_statuses_api_func().keys())
        status_combobox = ttk.Combobox(master=child_frame_add_order, values=statuses_list)
        status_combobox.grid(row=5 + start_row, column=1, padx=3, pady=3)
        self.add_order_properties_rows["status"] = (status_label, status_combobox)

        add_order_inputs = dict(((k, v[1]) for k, v in self.add_order_properties_rows.items()))
        self.add_address_find_user_button = ttk.Button(child_frame_add_order, text='Добавить адрес',
                                                       command=lambda: self.add_order(add_order_inputs))
        self.add_address_find_user_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        # - delete order -

        child_frame_delete_order = Frame(master=order_container)
        child_frame_delete_order.pack(padx=30, side=LEFT, anchor="n")

        Label(child_frame_delete_order, text="Удаление заказа", font=14).grid(row=0, column=0, columnspan=2, padx=20,
                                                                              pady=20)

        delete_order_id_label, self.delete_order_id_input = Window.add_simple_property_row(
            child_frame_delete_order, 1, "ID: ", False, (10, 3), 10)
        self.delete_order_id_error = Label(child_frame_delete_order, fg=Settings.ERROR_COLOR, text=Settings.EMPTY_ERROR_LABEL_TEXT)
        self.delete_order_id_error.grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Button(master=child_frame_delete_order, text="Удалить", command=self.delete_order_by_id).grid(row=2, column=0, columnspan=3, pady=10)

        # - change order status -

        child_frame_change_status_order = Frame(master=order_container)
        child_frame_change_status_order.pack(padx=30, side=LEFT, anchor="n")

        Label(child_frame_change_status_order, text="Изменение статуса", font=14).grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        change_order_status_id_label, self.change_order_status_id_input = Window.add_simple_property_row(child_frame_change_status_order, 1, "ID: ", False, (10, 3), 10)

        ttk.Button(master=child_frame_change_status_order, text="Найти", command=self.find_order_by_id_for_change_status).grid(row=2, column=0, columnspan=3, pady=5)

        change_order_status_current_order_id_label = Label(master=child_frame_change_status_order, text="Текущий id: ")
        change_order_status_current_order_id_label.grid(row=3, column=0, pady=0)

        self.change_order_status_current_order_id = Label(master=child_frame_change_status_order, text='', bg="#FFFAFA")
        self.change_order_status_current_order_id.grid(row=3, column=1, sticky='w', pady=10)

        status_label = Label(master=child_frame_change_status_order, text="Статус: ")
        status_label.grid(row=4, column=0, pady=(3, 0))
        self.change_order_status_combobox = ttk.Combobox(master=child_frame_change_status_order, values=statuses_list)
        self.change_order_status_combobox.grid(row=4, column=1, padx=3, pady=3)

        ttk.Button(master=child_frame_change_status_order, text="Изменить", command=self.save_new_order_status).grid(row=5, column=0, columnspan=3, pady=10)

        self.change_order_status_error = Label(child_frame_change_status_order, text=Settings.EMPTY_ERROR_LABEL_TEXT, fg=Settings.ERROR_COLOR)
        self.change_order_status_error.grid(row=6, column=0, columnspan=2, pady=10)

        # --- tab 4, add address, delete address ---

        address_container = Frame(frame4)
        address_container.pack()

        # - add address -

        child_frame_add_address = Frame(master=address_container)
        child_frame_add_address.pack(padx=30, side=LEFT)

        Label(child_frame_add_address, text="Добавление адреса", font=14).grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        start_row = 1
        add_address_rows_properties = dict(country=("Страна: ", 0, False), city=("Город: ", 1, False),
                                           street=("Улица: ", 2, False), house=("Дом: ", 3, False),
                                           flat=("Квартира", 4, False),
                                           post_index=("Почтовый индекс: ", 5, False),
                                           commentary=("Комментарий: ", 6, False))
        self.add_address_properties_rows: dict = dict(((k, Window.add_simple_property_row(child_frame_add_address, v[1] + start_row, v[0], v[2])) for k, v in add_address_rows_properties.items()))
        add_address_inputs = dict(((k, v[1]) for k, v in self.add_address_properties_rows.items()))
        self.add_address_find_user_button = ttk.Button(child_frame_add_address, text='Добавить адрес', command=lambda: self.add_address(add_address_inputs))
        self.add_address_find_user_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        # - delete address -

        child_frame_delete_address = Frame(master=address_container)
        child_frame_delete_address.pack(padx=30, side=LEFT, anchor="n")

        Label(child_frame_delete_address, text="Удаление адреса", font=14).grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        self.delete_address_id_label, self.delete_address_id_input = Window.add_simple_property_row(
            child_frame_delete_address, 1, "ID: ", False, (10, 3), 10)
        self.delete_address_id_error = Label(child_frame_delete_address, text=Settings.EMPTY_ERROR_LABEL_TEXT, fg=Settings.ERROR_COLOR)
        self.delete_address_id_error.grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Button(master=child_frame_delete_address, text="Удалить", command=self.delete_address_by_id).grid(row=2, column=0, columnspan=3, pady=10)

        # --- tab 3, edit user ---

        self.edit_id_label = Label(master=frame3, text="id пользователя: ")
        self.edit_id_label.grid(row=0, column=0, padx=(10, 3), pady=10)
        self.edit_id_input = ttk.Entry(master=frame3)
        self.edit_id_input.grid(row=0, column=1, padx=(10, 3), pady=10)
        self.edit_id_error = Label(master=frame3, text=Settings.EMPTY_ERROR_LABEL_TEXT, fg=Settings.ERROR_COLOR)
        self.edit_id_error.grid(row=0, column=2, padx=(10, 3), pady=10)

        edit_user_properties_widgets: dict = self.initialization_user_properties_widgets(frame3, 2)
        edit_user_inputs = [i["input"] for i in edit_user_properties_widgets.values()]

        self.edit_user_find_user_button = ttk.Button(frame3, text='Найти',
                                                     command=lambda: self.find_user_for_edit_by_id(edit_user_inputs))
        self.edit_user_find_user_button.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 10))

        self.edit_user_button = ttk.Button(master=frame3, text="Сохранить",
                                           command=lambda: self.edit_user(edit_user_inputs))
        self.edit_user_button.grid(row=10, column=1, padx=3, pady=3)

        self.delete_user_button = ttk.Button(frame3, text='Удалить', command=lambda: self.delete_user(edit_user_inputs),
                                             state=DISABLED)
        self.delete_user_button.grid(row=10, column=0, padx=3, pady=3)

        # --- tab 2, register user ---

        self.add_user_label = Label(master=frame2, text="Добавление пользователя")
        self.add_user_label.grid(row=0, column=0, columnspan=3, padx=3, pady=3)

        add_user_properties_widgets: dict = self.initialization_user_properties_widgets(frame2, 1)
        add_user_inputs = [i["input"] for i in add_user_properties_widgets.values()]

        self.add_user_button = ttk.Button(master=frame2, text="Добавить",
                                          command=lambda: self.add_user(add_user_inputs))
        self.add_user_button.grid(row=9, column=1, padx=3, pady=3)

        # --- tab 1, table of users ---

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 10))

        self.table = ttk.Treeview(master=frame1, show="headings", style="Treeview")

        # self.change_table(Settings.USER_PROPERTY_COLUMN_NAMES, Settings.USER_PROPERTY_COLUMN_PROPERTIES, self.load_users_api_func)

        vertical_scrollbar = ttk.Scrollbar(master=frame1, orient=VERTICAL, command=self.table.yview)
        self.table.configure(yscrollcommand=vertical_scrollbar.set)

        horizontal_scrollbar = ttk.Scrollbar(master=frame1, orient=HORIZONTAL, command=self.table.xview)
        self.table.configure(xscrollcommand=horizontal_scrollbar.set)

        button_container = Frame(master=frame1)

        load_users_button = ttk.Button(master=button_container, text="Пользователи",
                                       command=lambda: self.change_table(Settings.USER_PROPERTY_COLUMN_NAMES, Settings.USER_PROPERTY_COLUMN_PROPERTIES, self.get_all_users_api_func))
        load_addresses_button = ttk.Button(master=button_container, text="Адреса",
                                           command=lambda: self.change_table(Settings.ADDRESS_PROPERTY_COLUMN_NAMES, Settings.ADDRESS_PROPERTY_COLUMN_PROPERTIES, self.get_all_addresses_api_func))
        load_orders_button = ttk.Button(master=button_container, text="Заказы",
                                        command=lambda: self.change_table(Settings.ORDER_PROPERTY_COLUMN_NAMES, Settings.ORDER_PROPERTY_COLUMN_PROPERTIES, self.get_all_orders_api_func))
        load_user_statuses_button = ttk.Button(master=button_container, text="Статусы пользователей",
                                               command=lambda: self.change_table(Settings.STATUSES_PROPERTY_COLUMN_NAMES, Settings.STATUSES_PROPERTY_COLUMN_PROPERTIES,
                                                                                 self.get_user_statuses_api_func, True))
        load_order_statuses_button = ttk.Button(master=button_container, text="Статусы заказов",
                                                command=lambda: self.change_table(Settings.STATUSES_PROPERTY_COLUMN_NAMES, Settings.STATUSES_PROPERTY_COLUMN_PROPERTIES,
                                                                                  self.get_order_statuses_api_func, True))

        button_container.pack(side=BOTTOM, anchor=S)

        vertical_scrollbar.pack(side=RIGHT, fill=Y)
        self.table.pack(fill=BOTH, expand=True)
        horizontal_scrollbar.pack(side=BOTTOM, fill=X)

        load_users_button.pack(side=LEFT, anchor=S)
        load_addresses_button.pack(side=LEFT, anchor=S)
        load_orders_button.pack(side=LEFT, anchor=S)
        load_user_statuses_button.pack(side=LEFT, anchor=S)
        load_order_statuses_button.pack(side=LEFT, anchor=S)

    # --- table methods ---
    def change_table(self, names: list[str], properties: dict[str:tuple[...]], get_rows_data_function, is_dict: bool=False) -> None:
        for i in self.table.get_children():
            self.table.delete(i)

        self.table.configure(columns=names)

        for i, k in enumerate(properties):
            self.table.heading(k, text=properties[k][0])
            self.table.column(f"#{i + 1}", stretch=NO, width=properties[k][1])

        if is_dict:
            for k, v in get_rows_data_function().items():
                self.table.insert("", END, values=(v, k))
            return
        for obj in get_rows_data_function():
            self.table.insert("", END, values=obj.get_properties())

    # --- order methods ---
    def find_order_by_id_for_change_status(self):
        try:
            order = self.get_order_by_id_api_func(int(self.change_order_status_id_input.get()))
            self.change_order_status_current_order_id.configure(text=str(order.id))
            self.change_order_status_combobox.set(dict((v, k) for k, v in self.get_order_statuses_api_func().items())[order.status])
            self.change_order_status_error.configure(text=Settings.EMPTY_ERROR_LABEL_TEXT)
        except Exception as ex:
            self.change_order_status_error.configure(text="Ошибка")

    def save_new_order_status(self):
        try:
            self.change_order_status_api_func(self.change_order_status_current_order_id.cget('text'), self.get_order_statuses_api_func().get(self.change_order_status_combobox.get()))
            self.change_order_status_error.configure(text="")

        except Exception as ex:
            self.change_order_status_error.configure(text="Ошибка")

    def delete_order_by_id(self):
        try:
            self.delete_order_by_id_api_func(int(self.delete_order_id_input.get()))
            self.delete_order_id_error.configure(text=Settings.EMPTY_ERROR_LABEL_TEXT)
            self.delete_order_id_input.delete(0, END)
        except:
            self.delete_order_id_error.configure(text="Ошибка")

    def check_order_ids(self, sender_id, courier_id, address_id) -> None:
        try:
            self.get_user_by_id_api_func(sender_id)
            self.add_order_properties_rows["sender_id"][2].configure(text=Settings.EMPTY_ERROR_LABEL_TEXT)
        except:
            self.add_order_properties_rows["sender_id"][2].configure(text="!!!")
            raise ValueError("sender not found")
        try:
            courier: User = self.get_user_by_id_api_func(courier_id)
            if courier.status != self.get_user_statuses_api_func()["courier"]:
                self.add_order_properties_rows["courier_id"][2].configure(text="!!!")
                raise ValueError("The user is not a courier.")
            self.add_order_properties_rows["courier_id"][2].configure(text=Settings.EMPTY_ERROR_LABEL_TEXT)
        except:
            self.add_order_properties_rows["courier_id"][2].configure(text="!!!")
            raise ValueError("courier not found")
        try:
            self.get_address_by_id_api_func(address_id)
            self.add_order_properties_rows["address_id"][2].configure(text=Settings.EMPTY_ERROR_LABEL_TEXT)
        except:
            self.add_order_properties_rows["address_id"][2].configure(text="!!!")
            raise ValueError("address not found")

    def add_order(self, address_properties_inputs: dict[str: ...]) -> None:
        info = address_properties_inputs["info"].get()
        description = address_properties_inputs["description"].get()
        sender_id = address_properties_inputs["sender_id"].get()
        courier_id = address_properties_inputs["courier_id"].get()
        address_id = address_properties_inputs["address_id"].get()
        status_input = address_properties_inputs["status"]
        status = int(status_input.get()) if re.fullmatch('0-9',
                                                         status_input.get()) else self.get_order_statuses_api_func().get(
            status_input.get())
        self.check_order_ids(sender_id, courier_id, address_id)
        order = Order(0, info, description, sender_id, courier_id, address_id, status)
        self.add_order_api_func(order)

    # --- address methods ---
    def add_address(self, address_properties_inputs: dict[str: Entry]) -> None:
        # country, city, street, house, flat, postindex, commentary
        country = address_properties_inputs["country"].get()
        city = address_properties_inputs["city"].get()
        street = address_properties_inputs["street"].get()
        house = address_properties_inputs["house"].get()
        flat = address_properties_inputs["flat"].get()
        post_index = address_properties_inputs["post_index"].get()
        commentary = address_properties_inputs["commentary"].get()
        address = Address(0, country, city, street, house, flat, post_index, commentary)
        self.add_address_api_func(address)

    def delete_address_by_id(self) -> None:
        try:
            self.delete_address_by_id_api_func(int(self.delete_address_id_input.get()))
            self.delete_address_id_error.configure(text=Settings.EMPTY_ERROR_LABEL_TEXT)
            self.delete_address_id_input.delete(0, END)
        except:
            self.delete_address_id_error.configure(text="Ошибка")

    # --- user methods ---

    def create_user(self, login_input, password_input, name_input, surname_input, phone_input, email_input,
                    birthdate_input, status_input, id=0) -> User:
        login = login_input.get()
        password = password_input.get()
        name = name_input.get()
        surname = surname_input.get()
        phone = phone_input.get() if phone_input.get() != '' else None
        email = email_input.get() if email_input.get() != '' else None
        birthdate = birthdate_input.get() if birthdate_input.get() != '' else None
        status = int(status_input.get()) if re.fullmatch('0-9',
                                                         status_input.get()) else self.get_user_statuses_api_func().get(
            status_input.get())
        user = User(id, login, password, name, surname, phone, email, birthdate, status)
        return user

    def delete_user(self, user_properties_inputs):
        self.delete_user_by_id_api_func(int(self.edit_id_input.get()))
        self.delete_user_button["state"] = DISABLED
        for input in user_properties_inputs:
            input.delete(0, END)

    def add_user(self, user_properties_inputs):
        user = self.create_user(*user_properties_inputs)
        self.add_user_api_func(user)

    def edit_user(self, user_properties_inputs):
        user = self.create_user(*user_properties_inputs, id=int(self.edit_id_input.get()))
        self.edit_user_api_func(user)

    def validator(self, value, pattern, error_label, error_text):
        if re.fullmatch(pattern, value) is None:
            error_label.configure(text=error_text)
            return False
        error_label.configure(text=Settings.EMPTY_ERROR_LABEL_TEXT)
        return True

    def find_user_for_edit_by_id(self, user_properties_inputs):
        try:
            user = self.get_user_by_id_api_func(int(self.edit_id_input.get()))
            user_properties = (
                user.login, user.password, user.name, user.surname, user.phone, user.email, user.birthdate,
                user.status)
            for i, input in enumerate(user_properties_inputs):
                if not user_properties[i] is None:
                    input.delete(0, END)
                    input.insert(0, user_properties[i])
            self.edit_id_error.configure(text=Settings.EMPTY_ERROR_LABEL_TEXT)
            self.delete_user_button["state"] = NORMAL
        except:
            self.edit_id_error.configure(text="Такого пользователя не нашлось")
            self.delete_user_button["state"] = DISABLED

    def initialization_user_properties_widgets(self, root, start_row) -> dict[str: dict[str: ttk.Widget]]:
        widgets = {}

        login_label = Label(master=root, text="Логин*:")
        login_label.grid(row=start_row, column=0, padx=3, pady=3)
        login_input = ttk.Entry(master=root)
        login_input.grid(row=start_row, column=1, padx=3, pady=3)
        login_error = Label(master=root, fg=Settings.ERROR_COLOR, text=Settings.EMPTY_ERROR_LABEL_TEXT)
        login_error.grid(row=start_row, column=2, padx=3, pady=3)
        login_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'[a-zA-Z0-9!@#$%^&*()=_+?/><.,~`-]{8,}', login_error,
                                         'Неверная длина или символы')), '%P'))
        widgets["login"] = {}
        widgets["login"]["label"] = login_label
        widgets["login"]["input"] = login_input
        widgets["login"]["error"] = login_error
        start_row += 1

        password_label = Label(master=root, text="Пароль*:")
        password_label.grid(row=start_row, column=0, padx=3, pady=3)
        password_input = ttk.Entry(master=root)
        password_input.grid(row=start_row, column=1, padx=3, pady=3)
        password_error = Label(master=root, fg=Settings.ERROR_COLOR, text=Settings.EMPTY_ERROR_LABEL_TEXT)
        password_error.grid(row=start_row, column=2, padx=3, pady=3)
        password_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'[a-zA-Z0-9!@#$%^&*()=_+?/><.,~`-]{8,}', password_error,
                                         'Неверная длина или неверные символы')), '%P'))
        widgets["password"] = {}
        widgets["password"]["label"] = password_label
        widgets["password"]["input"] = password_input
        widgets["password"]["error"] = password_error
        start_row += 1

        name_label = Label(master=root, text="Имя*:")
        name_label.grid(row=start_row, column=0, padx=3, pady=3)
        name_input = ttk.Entry(master=root)
        name_input.grid(row=start_row, column=1, padx=3, pady=3)
        name_error = Label(master=root, fg=Settings.ERROR_COLOR, text=Settings.EMPTY_ERROR_LABEL_TEXT)
        name_error.grid(row=start_row, column=2, padx=3, pady=3)
        name_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^(?:[А-ЯЁ][а-яё]*|[A-Z][a-z]*)$', name_error,
                                         'Неверные символы')), '%P'))
        widgets["name"] = {}
        widgets["name"]["label"] = name_label
        widgets["name"]["input"] = name_input
        widgets["name"]["error"] = name_error
        start_row += 1

        surname_label = Label(master=root, text="Фамилия:")
        surname_label.grid(row=start_row, column=0, padx=3, pady=3)
        surname_input = ttk.Entry(master=root)
        surname_input.grid(row=start_row, column=1, padx=3, pady=3)
        surname_error = Label(master=root, fg=Settings.ERROR_COLOR, text=Settings.EMPTY_ERROR_LABEL_TEXT)
        surname_error.grid(row=start_row, column=2, padx=3, pady=3)
        surname_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^(?:[А-ЯЁ][а-яё]*|[A-Z][a-z]*)$', surname_error,
                                         'Некорректная фамилия')), '%P'))
        widgets["surname"] = {}
        widgets["surname"]["label"] = surname_label
        widgets["surname"]["input"] = surname_input
        widgets["surname"]["error"] = surname_error
        start_row += 1

        phone_label = Label(master=root, text="Телефон:")
        phone_label.grid(row=start_row, column=0, padx=3, pady=3)
        phone_input = ttk.Entry(master=root)
        phone_input.grid(row=start_row, column=1, padx=3, pady=3)
        phone_error = Label(master=root, fg=Settings.ERROR_COLOR, text=Settings.EMPTY_ERROR_LABEL_TEXT)
        phone_error.grid(row=start_row, column=2, padx=3, pady=3)
        phone_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^(?:[8][0-9]{10}|[+][0-9]{10,})$', phone_error,
                                         'Некорректный номер телефон')), '%P'))
        widgets["phone"] = {}
        widgets["phone"]["label"] = phone_label
        widgets["phone"]["input"] = phone_input
        widgets["phone"]["error"] = phone_error
        start_row += 1

        email_label = Label(master=root, text="Почта:")
        email_label.grid(row=start_row, column=0, padx=3, pady=3)
        email_input = ttk.Entry(master=root)
        email_input.grid(row=start_row, column=1, padx=3, pady=3)
        email_error = Label(master=root, fg=Settings.ERROR_COLOR, text=Settings.EMPTY_ERROR_LABEL_TEXT)
        email_error.grid(row=start_row, column=2, padx=3, pady=3)
        email_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^[a-zA-Z0-9!#$%^&*()=_+?/><,~`-]{1,}[@][a-zA-Z]{1,}[.][a-zA-Z]{2,3}$',
                                         email_error,
                                         'Почта указана неверно')), '%P'))
        widgets["email"] = {}
        widgets["email"]["label"] = email_label
        widgets["email"]["input"] = email_input
        widgets["email"]["error"] = email_error
        start_row += 1

        birthdate_label = Label(master=root, text="День рождения:")
        birthdate_label.grid(row=start_row, column=0, padx=3, pady=3)
        birthdate_input = ttk.Entry(master=root)
        birthdate_input.grid(row=start_row, column=1, padx=3, pady=3)
        birthdate_error = Label(master=root, fg=Settings.ERROR_COLOR, text=Settings.EMPTY_ERROR_LABEL_TEXT)
        birthdate_error.grid(row=start_row, column=2, padx=3, pady=3)
        birthdate_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'[1-2][0 - 9]{3}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])',
                                         birthdate_error,
                                         'Формат даты: ГГГГ-ММ-ДД')), '%P'))
        widgets["birthdate"] = {}
        widgets["birthdate"]["label"] = birthdate_label
        widgets["birthdate"]["input"] = birthdate_input
        widgets["birthdate"]["error"] = birthdate_error
        start_row += 1

        status_label = Label(master=root, text="Статус*:")
        status_label.grid(row=start_row, column=0, padx=3, pady=3)
        statuses_list = list(self.get_user_statuses_api_func().keys())
        status_combobox = ttk.Combobox(master=root, values=statuses_list)
        status_combobox.grid(row=start_row, column=1, padx=3, pady=3)

        widgets["status"] = {}
        widgets["status"]["label"] = status_label
        widgets["status"]["input"] = status_combobox

        return widgets

    # --- other methods ---

    @staticmethod
    def add_simple_property_row(master, row: int, text: str, has_error_label: bool, padx: ... = 3,
                                pady: ... = 3) -> tuple:
        label = Label(master=master, text=text)
        label.grid(row=row, column=0, padx=padx, pady=pady)
        entry = ttk.Entry(master=master)
        entry.grid(row=row, column=1, padx=padx, pady=pady)
        if has_error_label:
            error = Label(master=master, text=Settings.EMPTY_ERROR_LABEL_TEXT, fg=Settings.ERROR_COLOR)
            error.grid(row=row, column=2, padx=padx, pady=pady)
            return label, entry, error
        return label, entry
