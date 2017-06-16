from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import pymysql.cursors

app = Flask(__name__)


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='252601993',
                             db='Ormuco',
                             charset='utf8mb4')
                             #cursor=pymysql.cursors.DictCursor)

@app.route("/", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':

        _name = request.form['Name']
        _favcolor = request.form['Favcolor']
        _cot = request.form['CoT']

        try :
            with connection.cursor() as cursor :
                query = ( "INSERT INTO ormuco_form (name, favcolor, pet)" "VALUES (%s,%s,%s)")
                data = (_name,_favcolor,_cot )
                cursor.execute(query,data)

            connection.commit()
        finally :
            connection.close()
            return "saved sucesfully."
        



    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug = True)
