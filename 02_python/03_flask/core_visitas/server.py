from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'Esta es tu clave secreta!'

@app.route('/')
def index():
    if 'visitas' in session:
        session['visitas'] += 1
    else:
        print("No existe la propiedad")
        session['visitas'] = 1

    if 'reinicios' not in session:
        session['reinicios'] = 0

    return render_template("index.html")

@app.route('/destruir_sesion')
def destruir_sesion():
    if 'reinicios' in session:
        session['reinicios'] += 1
    else:
        session['reinicios'] = 1

    session.pop('visitas', None) 
    return redirect('/')

@app.route('/mas_dos', methods=['POST'])
def mas_dos():
    if 'visitas' in session:
        session['visitas'] += 1 
    return redirect('/')    

@app.route('/incrementar', methods=['POST'])
def incrementar():
    cantidad = int(request.form['incremento'])
    if 'visitas' in session:
        session['visitas'] += (cantidad - 1)
    return redirect('/')  

if __name__ == "__main__":
    app.run(debug=True)
