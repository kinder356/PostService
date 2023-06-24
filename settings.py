class Settings:
    EMPTY_ERROR_LABEL_TEXT = "   "
    ERROR_COLOR = "#FF0000"

    USER_PROPERTY_COLUMN_NAMES = ("id", "login", "password", "name", "surname", "phone", "email", "birthdate", "status")
    USER_PROPERTY_COLUMN_PROPERTIES = dict(
        id=("ID", 45), login=("Login", 140), password=("Password", 95), name=("Name", 95),
        surname=("Surname", 95), phone=("Phone", 95), email=("Email", 95),
        birthdate=("Birthdate", 95), status=("Status", 45)
    )

    ADDRESS_PROPERTY_COLUMN_NAMES = ("id", "country", "city", "street", "house", "flat", "post_index", "commentary")
    ADDRESS_PROPERTY_COLUMN_PROPERTIES = dict(
        id=("ID", 45), country=("Country", 80), city=("City", 80), street=("Street", 80),
        house=("House", 80), flat=("Flat", 80), post_index=("Post index", 70),
        commentary=("Commentary", 140)
    )

    ORDER_PROPERTY_COLUMN_NAMES = ("id", "info", "description", "sender_id", "courier_id", "address_id", "status")
    ORDER_PROPERTY_COLUMN_PROPERTIES = dict(
        id=("ID", 45), info=("Info", 120), description=("Description", 140), sender_id=("Sender id", 80),
        courier_id=("Courier id", 80), address_id=("Address id", 80), status=("Status", 60)
    )

    STATUSES_PROPERTY_COLUMN_NAMES = ("id", "status")
    STATUSES_PROPERTY_COLUMN_PROPERTIES = dict(
        id=("ID", 45), status=("Status", 120)
    )


