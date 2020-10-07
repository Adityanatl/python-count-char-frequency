# database.py
from pony.orm import Database, PrimaryKey, Required, Optional

db = Database()


class Mahasiswa(db.Entity):
    id = PrimaryKey(int, auto=True)
    nik = Optional(int)
    name = Required(str)
    address = Optional(str)
    gender_id = Optional(int)

class Gender(db.Entity):
    gender_id = Optional(int)
    name = Required(str)

# connect to mysql
db.bind('mysql', host='localhost', user='root', passwd='', db='universitas')