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
    msg_s = ""  # to show message data saved or not
    msg_er = ""  # to show message data saved or not
    val_m = ""  # to display validation message

    val = re.compile("^[a-zA-Z ]*$")

    if request.method == 'POST':

        _name = request.form['Name']
        _favcolor = request.form['Favcolor']
        _cot = request.form['CoT']

        if not val.match(_name):
            val_m = "Enter text only, don't enter characters"
        else:
            if not val.match(_favcolor):
                val_m = "Enter text only, don't enter characters"
            else:
                if _cot == "none":
                    val_m = "Please select one pet cat or dog "
                else:

                    data = User(_name, _favcolor, _cot)

                    try:
                        db.session.add(data)
                        db.session.commit()
                        msg_s = 'Saved Sucesfully, Click Here'
                    except exc.IntegrityError:
                        db.session.rollback()
                        msg_er = "The name already exist, please set an other"
                    finally:
                        db.session.close()

    q = User.query.all()
    return render_template('index.html', querys=q, msn_s=msg_s, msn_er=msg_er, er=val_m)


if __name__ == '__main__':
    app.run(debug=True)
