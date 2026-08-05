from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'clave_secreta_explorador_reliquias'

# Configuración de rangos por lugar (Evita el uso de condicionales if/elif en /buscar_reliquias - Bonus Oro)
LUGARES_CONFIG = {
    'templo': (10, 20),
    'piramide': (5, 10),
    'selva': (2, 5),
    'ruinas': (-50, 50)
}

@app.route('/')
def index():
    if 'reliquias' not in session:
        session['reliquias'] = 0
    if 'actividades' not in session:
        session['actividades'] = []
    if 'intentos' not in session:
        session['intentos'] = 0
    if 'gano' not in session:
        session['gano'] = False
    if 'perdio' not in session:
        session['perdio'] = False

    return render_template("index.html")

@app.route('/buscar_reliquias', methods=['POST'])
def buscar_reliquias():
    lugar = request.form['lugar']
    
    # Obtenemos los límites del diccionario sin usar if/elif (Bonus Oro)
    min_reliquias, max_reliquias = LUGARES_CONFIG[lugar]
    cambio = random.randint(min_reliquias, max_reliquias)
    
    session['reliquias'] += cambio
    session['intentos'] += 1

    # Formateamos el mensaje con color según el resultado (Bonus Plata)
    if cambio >= 0:
        mensaje = f'<p class="texto-verde">Se obtuvieron:{cambio} en:{lugar}</p>'
    else:
        mensaje = f'<p class="texto-rojo">Se derrumbó la ruina! Perdiste {abs(cambio)} en:{lugar}</p>'

    # Insertamos al inicio de la lista para mostrar la actividad más reciente primero (Bonus Oro)
    actividades = session['actividades']
    actividades.insert(0, mensaje)
    session['actividades'] = actividades

    # Condición de victoria o derrota (Bonus Oro: 500 reliquias en 15 exploraciones o menos)
    if session['reliquias'] >= 500 and session['intentos'] <= 15:
        session['gano'] = True
    elif session['intentos'] >= 15 and session['reliquias'] < 500:
        session['perdio'] = True

    return redirect('/')

@app.route('/reiniciar')
def reiniciar():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
