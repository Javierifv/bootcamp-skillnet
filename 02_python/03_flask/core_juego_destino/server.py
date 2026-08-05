from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'clave_secreta_juego_destino'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/enviar', methods=['POST'])
def enviar():
    session['nombre'] = request.form['nombre']
    session['lugar'] = request.form['lugar']
    session['numero'] = request.form['numero']
    session['comida'] = request.form['comida']
    session['profesion'] = request.form['profesion']

    session['suerte'] = random.choice(['buena', 'mala'])

    return redirect('/futuro')

@app.route('/futuro')
def futuro():
    return render_template("futuro.html")

@app.route('/reiniciar')
def reiniciar():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

