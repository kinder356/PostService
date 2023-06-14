from tkinter import *
from tkinter import ttk
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


class Address:
    _id = 0
    _country = ""
    _city = ""
    _street = ""
    _house = ""
    _flat = ""
    _post_index = ""
    _commentary = ""


class Order:
    _id = 0
    _info = ""
    _description = ""
    _sender_id = 0
    _courier_id = 0
    _address_id = 0
    _status = 1


class Window(Tk):

    def __init__(self, get_statuses_dict_func, add_user_func, load_user_func):
        super().__init__()
        self.title("Post Service")
        self.geometry("+300+100")

        # --- functions ---

        self.add_user_api_func = add_user_func
        self.load_users_api_func = load_user_func
        self.get_statuses_api_func = get_statuses_dict_func

        notebook = ttk.Notebook()
        notebook.pack(expand=True, fill=BOTH)

        # --- tabs ---

        frame1 = ttk.Frame(notebook)
        frame1.pack()
        notebook.add(frame1, text="Пользователи")

        frame2 = ttk.Frame(notebook)
        frame2.pack()
        notebook.add(frame2, text="Добавление")

        frame3 = ttk.Frame(notebook)
        frame3.pack()
        notebook.add(frame3, text="Редактирование")

        frame4 = ttk.Frame(notebook)
        frame4.pack()
        notebook.add(frame4, text="Заказы")

        # --- tab 3, edit user ---

        self.edit_id_label = Label(master=frame3, text="id пользователя: ")
        self.edit_id_label.grid(row=0, column=0, padx=(10, 3), pady=10)
        self.edit_id_input = ttk.Entry(master=frame3)
        self.edit_id_input.grid(row=0, column=1, padx=(10, 3), pady=10)
        self.edit_id_error = Label(master=frame3)
        self.edit_id_error.grid(row=0, column=2, padx=(10, 3), pady=10)

        self.find_user_button = ttk.Button(frame3, text='Найти', command=self.find_user_for_edit)
        self.find_user_button.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 10))
        
        # --- tab 2, register user ---

        self.add_user_label = Label(master=frame2, text="Добавление пользователя")
        self.add_user_label.grid(row=0, column=0, columnspan=3, padx=3, pady=3)

        self.login_label = Label(master=frame2, text="Логин*:")
        self.login_label.grid(row=1, column=0, padx=3, pady=3)
        self.login_input = ttk.Entry(master=frame2)
        self.login_input.grid(row=1, column=1, padx=3, pady=3)
        self.login_error = Label(master=frame2)
        self.login_error.grid(row=1, column=2, padx=3, pady=3)
        self.login_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'[a-zA-Z0-9!@#$%^&*()=_+?/><.,~`-]{8,}', self.login_error,
                                         'Неверная длина или символы')), '%P'))

        self.password_label = Label(master=frame2, text="Пароль*:")
        self.password_label.grid(row=2, column=0, padx=3, pady=3)
        self.password_input = ttk.Entry(master=frame2)
        self.password_input.grid(row=2, column=1, padx=3, pady=3)
        self.password_error = Label(master=frame2)
        self.password_error.grid(row=2, column=2, padx=3, pady=3)
        self.password_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'[a-zA-Z0-9!@#$%^&*()=_+?/><.,~`-]{8,}', self.password_error,
                                         'Неверная длина или неверные символы')), '%P'))

        self.name_label = Label(master=frame2, text="Имя*:")
        self.name_label.grid(row=3, column=0, padx=3, pady=3)
        self.name_input = ttk.Entry(master=frame2)
        self.name_input.grid(row=3, column=1, padx=3, pady=3)
        self.name_error = Label(master=frame2)
        self.name_error.grid(row=3, column=2, padx=3, pady=3)
        self.name_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^(?:[А-ЯЁ][а-яё]*|[A-Z][a-z]*)$', self.name_error,
                                         'Неверные символы')), '%P'))

        self.surname_label = Label(master=frame2, text="Фамилия:")
        self.surname_label.grid(row=4, column=0, padx=3, pady=3)
        self.surname_input = ttk.Entry(master=frame2)
        self.surname_input.grid(row=4, column=1, padx=3, pady=3)
        self.surname_error = Label(master=frame2)
        self.surname_error.grid(row=4, column=2, padx=3, pady=3)
        self.surname_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^(?:[А-ЯЁ][а-яё]*|[A-Z][a-z]*)$', self.surname_error,
                                         'Некорректная фамилия')), '%P'))

        self.phone_label = Label(master=frame2, text="Телефон:")
        self.phone_label.grid(row=5, column=0, padx=3, pady=3)
        self.phone_input = ttk.Entry(master=frame2)
        self.phone_input.grid(row=5, column=1, padx=3, pady=3)
        self.phone_error = Label(master=frame2)
        self.phone_error.grid(row=5, column=2, padx=3, pady=3)
        self.phone_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^(?:[8][0-9]{10}|[+][0-9]{10,})$', self.phone_error,
                                         'Некорректный номер телефон')), '%P'))

        self.email_label = Label(master=frame2, text="Почта:")
        self.email_label.grid(row=6, column=0, padx=3, pady=3)
        self.email_input = ttk.Entry(master=frame2)
        self.email_input.grid(row=6, column=1, padx=3, pady=3)
        self.email_error = Label(master=frame2)
        self.email_error.grid(row=6, column=2, padx=3, pady=3)
        self.email_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^[a-zA-Z0-9!#$%^&*()=_+?/><,~`-]{1,}[@][a-zA-Z]{1,}[.][a-zA-Z]{2,3}$',
                                         self.email_error,
                                         'Почта указана неверно')), '%P'))

        self.birthdate_label = Label(master=frame2, text="День рождения:")
        self.birthdate_label.grid(row=7, column=0, padx=3, pady=3)
        self.birthdate_input = ttk.Entry(master=frame2)
        self.birthdate_input.grid(row=7, column=1, padx=3, pady=3)
        self.birthdate_error = Label(master=frame2)
        self.birthdate_error.grid(row=7, column=2, padx=3, pady=3)
        self.birthdate_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'[1-2][0 - 9]{3}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])',
                                         self.birthdate_error,
                                         'Формат даты: ГГГГ-ММ-ДД')), '%P'))

        self.status_label = Label(master=frame2, text="Статус*:")
        self.status_label.grid(row=8, column=0, padx=3, pady=3)
        self.statuses_list = list(self.get_statuses_api_func().keys())
        self.status_combobox = ttk.Combobox(master=frame2, values=self.statuses_list)
        self.status_combobox.grid(row=8, column=1, padx=3, pady=3)
        self.status_error = Label(master=frame2)
        self.status_error.grid(row=8, column=2, padx=3, pady=3)

        self.add_user_button = ttk.Button(master=frame2, text="Добавить", command=self.add_user)
        self.add_user_button.grid(row=9, column=1, padx=3, pady=3)

        # --- tab 1, table of users ---

        columns = ["id", "login", "password", "name", "surname", "phone", "email", "birthdate", "status"]
        self.users_table = ttk.Treeview(master=frame1, columns=columns, show="headings")

        columns_properties = dict(id=("ID", 45), login=("Login", 140), password=("Password", 95), name=("Name", 95),
                                  surname=("Surname", 95), phone=("Phone", 95), email=("email", 95),
                                  birthdate=("Birthdate", 95), status=("Status", 45))
        for i, k in enumerate(columns):
            self.users_table.heading(k, text=columns_properties[k][0])
            self.users_table.column(f"#{i + 1}", stretch=NO, width=columns_properties[k][1])

        vertical_scrollbar = ttk.Scrollbar(master=frame1, orient=VERTICAL, command=self.users_table.yview)
        self.users_table.configure(yscrollcommand=vertical_scrollbar.set)

        horizontal_scrollbar = ttk.Scrollbar(master=frame1, orient=HORIZONTAL, command=self.users_table.xview)
        self.users_table.configure(xscrollcommand=horizontal_scrollbar.set)

        self.load_users_button = ttk.Button(master=frame1, text="Обновить", command=self.load_users_list)

        self.load_users_button.pack(side=BOTTOM, anchor=S)
        vertical_scrollbar.pack(side=RIGHT, fill=Y)
        self.users_table.pack(fill=BOTH, expand=True)
        horizontal_scrollbar.pack(side=BOTTOM, fill=X)

    def add_user(self):
        login = self.login_input.get()
        password = self.password_input.get()
        name = self.name_input.get()
        surname = self.surname_input.get()
        phone = self.phone_input.get() if self.phone_input.get() != '' else None
        email = self.email_input.get() if self.email_input.get() != '' else None
        birthdate = self.birthdate_input.get() if self.birthdate_input.get() != '' else None
        status = self.get_statuses_api_func().get(self.status_combobox.get())
        user = User(0, login, password, name, surname, phone, email, birthdate, status)
        self.add_user_api_func(user)

    def load_users_list(self):
        users = self.load_users_api_func()
        for i in self.users_table.get_children():
            self.users_table.delete(i)

        for user in users:
            self.users_table.insert("", END, values=(
                user.id, user.login, user.password, user.name, user.surname, user.phone, user.email, user.birthdate,
                user.status))

    def validator(self, value, pattern, error_label, error_text):
        if re.fullmatch(pattern, value) is None:
            error_label.configure(text=error_text)
            return False
        error_label.configure(text='')
        return True

    def find_user_for_edit(self):
        pass
