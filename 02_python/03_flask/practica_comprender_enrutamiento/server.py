from flask import Flask

app = Flask(__name__)

# Ruta raíz (“/”) que responde “¡Hola desde Flask!”

@app.route('/')

def hola_flask():
    return '¡Hola desde Flask!'

# Ruta que responde con “¿Qué ruta estás buscando?”

@app.route('/ruta')

def ruta():
    return "¿Qué ruta estás buscando?"

# Ruta que responde con “Bienvenid@ a esta ruta” y el nombre que esté en la URL después de /bienvenido/

@app.route('/bienvenido/<cadena>')

def bienvenida(cadena):
    print(cadena) #Imprime en la terminal el nombre enviado a través de la URL
    return (f'Bienvenida@ a esta ruta {cadena}!')

# Ruta que responde con “Repite después de mi: ” y la palabra dada repetida tantas veces como se especifique en la URL

@app.route('/repite/<int:numero>/<cadena>')

def repite(numero, cadena):
    print(numero)
    print(cadena)
    return f'Repite después de mi: {cadena*numero}'

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "¡Sobrecarga de rutas! No encontramos a donde quieres ir, inténtalo de nuevo.", 404

if __name__=="__main__":  
    app.run(debug=True)