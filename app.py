from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
import re

app = Flask(__name__)

db = SQLAlchemy()
from app_migrations import *


# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='252601993',
#                              db='Ormuco',
#                              charset='utf8mb4')


@app.route("/", methods=['GET', 'POST'])
def add():

    msg = ""    # to show message data saved or not
#    val_m = ""  # to display validation message

#    val = re.compile("^[a-zA-Z ]*$")

    if request.method == 'POST':

        _name = request.form['Name']
        _favcolor = request.form['Favcolor']
        _cot = request.form['CoT']

        data = User(_name, _favcolor, _cot)

        try:
            db.session.add(data)
            db.session.commit()
            msg = 'Saved Sucesfully'
        except exc.IntegrityError:
            db.session.rollback()
            msg = "The name already exist, please set an other"
        finally:
            db.session.close()

    q = User.query.all()
    return render_template('index.html', querys=q, msn=msg)


if __name__ == '__main__':
    app.run(debug=True)
