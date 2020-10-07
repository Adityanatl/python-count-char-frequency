# wsgi.py

import falcon
from mahasiswa import Mahasiswa
from gender import Gender

app = falcon.API()

app.add_route("/mahasiswa", Mahasiswa())