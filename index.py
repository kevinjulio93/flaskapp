from flask import Flask, render_template, request
from flask.ext.mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']= '172.0.0.1'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'Ormuco'
mysql.init_app(app)


@app.route("/", methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':
        
        name = request.form['Name']
        favcolor = request.form['Favcolor']
        cot = request.form['CoT']

        

        

        return render_template('age.html', age=resultado)
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
