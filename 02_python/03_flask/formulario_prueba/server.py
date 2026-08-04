from flask import Flask, render_template, request, redirect 

app = Flask(__name__)

# La ruta raíz renderizará nuestro formulario
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/final')
def final():
    return render_template("entrega.html")

# /crear_usuario recibe la información
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    print("Recibiendo información")
    print(request.form)

    #JAMAS renderizamos una plantilla ante una solicitud POST
    return redirect('/mostrar_usuario') #En su lugar, redirigimos a otra ruta

@app.route('/mostrar_usuario')
def mostrar_usuario():
    print("Usuario redirigido")
    print(request.form) #Imprime un diccionario vacío, porque no tenemos acceso a esta información
    return render_template("mostrar.html")

if __name__ == "__main__":
    app.run(debug=True)