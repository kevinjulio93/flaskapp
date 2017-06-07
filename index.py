from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/send", methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        num1 = int(request.form['numero1'])
        num2 = int(request.form['numero2'])

        a = num1 + num2

        resultado = str(a)

        return render_template('age.html', age=resultado)
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
