from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')   # El decorador "@" asocia esta ruta con la función inmediatamente siguiente

def hola_mundo():
    return '¡Hola Mundo!'

@app.route('/exito')
def exito():
    return "¡Éxito!"

@app.route('/saludo/<nombre>')
def saludo(nombre):
    print(nombre)
    return f'¡Hola {nombre}!'

@app.route('/color/<nombre>/<color>')
def color_favorito(nombre, color):
    print(nombre)
    print(color)
    return f'Hola {nombre}, tu color favorito es el {color}'

@app.route('/saludo/<nombre>/<int:num>')
def hola_cantidad(nombre, num):
    return f'¡Hola {nombre}! ' * num

@app.route('/bienvenido')
def bienvenido():
    #En vez de regresar una cadena, regresamos el resultado del método render_template
    #enviando el nombre del archivo de HTML que queremos renderizar
    return render_template('index.html', cancion="dale a tu cuerpo alegría macarena", repite=5)

@app.route('/listas')
def renderizar_listas():

    #Próximamente estas listas serán extraidas de la base de datos

    listado_estudiantes = [

        {'nombre': 'Florencia', 'edad': 25},
        {'nombre': 'Valentina', 'edad': 30},
        {'nombre': 'José', 'edad': 27},
        {'nombre': 'Patricio', 'edad': 21}
    ]

    return render_template('index.html', numeros=[7, 15, 22], estudiantes=listado_estudiantes)

if __name__=="__main__": 
    app.run(debug=True)