from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

app = Flask(__name__)

db = SQLAlchemy().session
from app_migrations import *

# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='252601993',
#                              db='Ormuco',
#                              charset='utf8mb4')


@app.route("/", methods=['GET', 'POST'])
def add():
    mensaje =""
    if request.method == 'POST':
        _name = request.form['Name']
        _favcolor = request.form['Favcolor']
        _cot = request.form['CoT']

        data = User(_name, _favcolor, _cot)

        try:
            db.add(data)
            db.commit()
            mensaje = 'Saved Sucesfully'
        except exc.IntegrityError:
            db.rollback()
            mensaje = "The name already exist, please set an other"
        finally:
            db.close()

    q = User.query.all()
    return render_template('index.html', querys=q, msn = mensaje)


if __name__ == '__main__':
    app.run(debug=True)

