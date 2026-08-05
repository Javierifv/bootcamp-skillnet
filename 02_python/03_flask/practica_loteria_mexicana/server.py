from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'clave_secreta_loteria_2'

cartas = [
    "0 - Carta no válida", "1  El Gallo", "2  El Diablito", "3  La Dama", "4  El catrín", 
    "5  El paraguas", "6  La sirena", "7  La escalera", "8  La botella", "9  El barril", 
    "10 El árbol", "11 El melón", "12 El valiente", "13 El gorrito", "14 La muerte", 
    "15 La pera", "16 La bandera", "17 El bandolón", "18 El violoncello", "19 La garza", 
    "20 El pájaro", "21 La mano", "22 La bota", "23 La luna", "24 El cotorro", 
    "25 El borracho", "26 El negrito", "27 El corazón", "28 La sandía", "29 El tambor", 
    "30 El camarón", "31 Las jaras", "32 El músico", "33 La araña", "34 El soldado", 
    "35 La estrella", "36 El cazo", "37 El mundo", "38 El apache", "39 El nopal", 
    "40 El alacrán", "41 La rosa", "42 La calavera", "43 La campana", "44 El cantarito", 
    "45 El venado", "46 El sol", "47 La corona", "48 La chalupa", "49 El pino", 
    "50 El pescado", "51 La palma", "52 La maceta", "53 El arpa", "54 La rana"
]

@app.route('/')
def index():
    if 'numero_secreto' not in session:
        session['numero_secreto'] = random.randint(1, 54)
    if 'intentos' not in session:
        session['intentos'] = 0
    return render_template("index.html")

@app.route('/adivinar', methods=['POST'])
def adivinar():
    suposicion = int(request.form['suposicion'])
    session['intentos'] += 1
    numero_secreto = session['numero_secreto']

    if suposicion == numero_secreto:
        session['resultado'] = 'correcto'
        session['carta_ganadora'] = cartas[numero_secreto]
    elif session['intentos'] >= 5:
        session['resultado'] = 'perdio'
        session['carta_ganadora'] = cartas[numero_secreto]
    elif suposicion < numero_secreto:
        session['resultado'] = 'menor'
    else:
        session['resultado'] = 'mayor'

    return redirect('/')

@app.route('/reiniciar')
def reiniciar():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)