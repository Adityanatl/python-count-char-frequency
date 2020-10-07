# mahasiswa.py

from database import Mahasiswa as _Mahasiswa
from pony.orm import db_session

#read data record
@db_session
def index():
      # Read a single record
      sql = "SELECT 'id', 'nik', 'name', 'address', 'gender_id'  FROM 'mahasiswa' INNER JOIN Gender ON 'gender_id'"
      cursor.execute(sql)
      result = cursor.fetchone()
      print(result)

#insert data to row
@db_session
@application.route('/tambah', methods=['GET','POST'])
def add():
   if request.method == 'POST':
      nik = request.form['nik']
      name = request.form['name']
      address = request.form['address']
      openDb()
      sql = db.insert(nik="nik", name="name", address="address", gende_id="gender_id")
      val = (nik, name, address, gender_id)
      cursor.execute(sql, val)
      db.commit()
      closeDb()
      return redirect(url_for('index'))
   else:
      return render_template('tambah.html')

#edit data row
@db_session
def edit():
      openDb()
      cursor.execute('SELECT * FROM mahasiswa WHERE id=%s', (id))
      data = cursor.fetchone()
   if request.method == 'POST':
      id = request.form['id']
      nik = request.form['nik']
      name = request.form['name']
      address = request.form['address']
      sql = "UPDATE mahasiswa SET nik=%s, name=%s, address=%s WHERE id=%s"
      val = (nik, name, address, id)
      cursor.execute(sql, val)
      db.commit()
      closeDb()
      return redirect(url_for('index'))
   else:
      closeDb()
      return render_template('edit.html', data=data)

#deleted data row
@db_session
@application.route('/hapus/<id>', methods=['GET','POST'])
def deleted():
   openDb()
   cursor.execute('DELETE FROM Mahasiswa WHERE id_=%s', (Mahasiswa))
   db.commit()
   closeDb()
   return redirect(url_for('index'))