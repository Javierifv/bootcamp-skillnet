from flask import Flask, render_template

app = Flask(__name__)

@app.route('/listas')

def renderizar_listas():

    #Próximamente estas listas serán extraidas de la base de datos

    listado_estudiantes = [

        {'nombre': 'Florencia', 'edad': 25},
        {'nombre': 'Valentina', 'edad': 30},
        {'nombre': 'José', 'edad': 27},
        {'nombre': 'Patricio', 'edad': 21}
    ]

    return render_template('listas.html', numeros=[7, 15, 22], estudiantes=listado_estudiantes)

@app.route("/paises")

def 

paises = [
    {'pais': 'Argentina' , 'capital': 'Buenos Aires'},
    {'pais': 'Brasil' , 'capital': 'Brasilia'},
    {'pais': 'Chile' , 'capital': 'Santiago de Chile'},
    {'pais': 'Colombia' , 'capital': 'Bogotá'},
    {'pais': 'Costa Rica' , 'capital': 'San José'},
    {'pais': 'Paraguay' , 'capital': 'Asunción'},
    {'pais': 'Perú' , 'capital': 'Lima'}
]

if __name__=="__main__": 
    app.run(debug=True)