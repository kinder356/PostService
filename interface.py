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

    def __init__(self, get_statuses_dict_func, add_user_func, load_user_func, edit_user_func, get_user_by_id_func,
                 delete_user_by_id_func):
        super().__init__()
        self.title("Post Service")
        self.geometry("+300+100")

        # --- functions ---

        self.add_user_api_func = add_user_func
        self.load_users_api_func = load_user_func
        self.get_statuses_api_func = get_statuses_dict_func
        self.edit_user_api_func = edit_user_func
        self.get_user_by_id_api_func = get_user_by_id_func
        self.delete_user_by_id_api_func = delete_user_by_id_func

        notebook = ttk.Notebook()
        notebook.pack(expand=True, fill=BOTH)

        # --- tabs init ---

        frame1 = ttk.Frame(notebook)
        frame1.pack()
        notebook.add(frame1, text="Пользователи")

        frame2 = ttk.Frame(notebook)
        frame2.pack()
        notebook.add(frame2, text="Добавление")

        frame3 = ttk.Frame(notebook)
        frame3.pack()
        notebook.add(frame3, text="Редактирование пользователя")

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

        edit_user_properties_widgets: dict = self.initialization_user_properties_widgets(frame3, 2)
        edit_user_inputs = [i["input"] for i in edit_user_properties_widgets.values()]

        self.find_user_button = ttk.Button(frame3, text='Найти',
                                           command=lambda: self.find_user_for_edit_by_id(edit_user_inputs))
        self.find_user_button.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 10))

        self.edit_user_button = ttk.Button(master=frame3, text="Сохранить",
                                           command=lambda: self.edit_user(edit_user_inputs))
        self.edit_user_button.grid(row=10, column=1, padx=3, pady=3)

        self.delete_user_button = ttk.Button(frame3, text='Удалить', command=lambda: self.delete_user(edit_user_inputs), state=DISABLED)
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

    def create_user(self, login_input, password_input, name_input, surname_input, phone_input, email_input,
                    birthdate_input, status_input, id=0) -> User:
        login = login_input.get()
        password = password_input.get()
        name = name_input.get()
        surname = surname_input.get()
        phone = phone_input.get() if phone_input.get() != '' else None
        email = email_input.get() if email_input.get() != '' else None
        birthdate = birthdate_input.get() if birthdate_input.get() != '' else None
        status = self.get_statuses_api_func().get(status_input.get()) if re.fullmatch('0-9',
                                                                                      status_input.get()) else int(
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
            self.edit_id_error.configure(text="")
            self.delete_user_button["state"] = NORMAL
        except Exception:
            self.edit_id_error.configure(text="Такого пользователя не нашлось")
            self.delete_user_button["state"] = DISABLED

    def initialization_user_properties_widgets(self, root, start_row) -> dict[str: dict[str: ttk.Widget]]:
        widgets = {}

        login_label = Label(master=root, text="Логин*:")
        login_label.grid(row=start_row, column=0, padx=3, pady=3)
        login_input = ttk.Entry(master=root)
        login_input.grid(row=start_row, column=1, padx=3, pady=3)
        login_error = Label(master=root)
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
        password_error = Label(master=root)
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
        name_error = Label(master=root)
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
        surname_error = Label(master=root)
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
        phone_error = Label(master=root)
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
        email_error = Label(master=root)
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
        birthdate_error = Label(master=root)
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
        statuses_list = list(self.get_statuses_api_func().keys())
        status_combobox = ttk.Combobox(master=root, values=statuses_list)
        status_combobox.grid(row=start_row, column=1, padx=3, pady=3)

        widgets["status"] = {}
        widgets["status"]["label"] = status_label
        widgets["status"]["input"] = status_combobox

        return widgets
