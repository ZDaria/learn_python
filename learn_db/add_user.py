from db import db_session
from models import User

user = User(name="Sidorova Maria", salary="70000", email="sidorova_maria@mail.com")
db_session.add(user)
db_session.commit()
