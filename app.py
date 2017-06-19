from flask import Flask, render_template, request
import pymysql.cursors
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy

from app_migrations import *

connection = pymysql.connect(host='localhost',
                           user='root',
                          password='252601993',
                         db='Ormuco',
                        charset='utf8mb4')

# connection = pymysql.connect(host='sql10.freemysqlhosting.net',
#                              user='sql10180646',
#                              password='CMVHyy9b3U',
#                              db='sql10180646',
#                              charset='utf8mb4')


# cursor=pymysql.cursors.DictCursor)

@app.route("/", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':

        _name = request.form['Name']
        _favcolor = request.form['Favcolor']
        _cot = request.form['CoT']

        data = User(_name, _favcolor, _cot)
        db.session.add(data)
        db.session.commit()

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
