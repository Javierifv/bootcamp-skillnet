from flask import Flask, render_template

app = Flask(__name__)

@app.route('/juega')
def juego():
    return render_template('index.html', cantidad=3, color="red")

@app.route('/juega/<int:cantidad>')
def juego_cantidad(cantidad):
    return render_template('index.html', cantidad=cantidad, color="red")

@app.route('/juega/<int:cantidad>/<color>')
def juego_cantidad_color(cantidad, color):
    return render_template('index.html', cantidad=cantidad, color=color)

if __name__=="__main__":  
    app.run(debug=True)