from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    
    # 1. Capturamos los datos del formulario
    fresa = request.form['fresa']
    frambuesa = request.form['frambuesa']
    manzana = request.form['manzana']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    
    # 2. Calculamos el total (convirtiendo a int)
    total_frutas = int(fresa) + int(frambuesa) + int(manzana)
    print(f"Cobrando a {nombre} {apellido} por {total_frutas} frutas")
    
    # 3. Enviamos las variables al HTML
    return render_template("checkout.html", 
                        fresa=fresa, 
                        frambuesa=frambuesa, 
                        manzana=manzana, 
                        nombre=nombre, 
                        apellido=apellido, 
                        email=email, 
                        total=total_frutas)

@app.route('/frutas')         
def fruits():
    return render_template("frutas.html")

if __name__=="__main__":   
    app.run(debug=True)    