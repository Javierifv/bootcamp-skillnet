from flask_app import app
from flask_app.controllers import tacos #Importamos el controlador #Importamos la app de la carpeta flask_app

if __name__=="__main__": #Ejecutamos la aplicación
    app.run(debug=True)