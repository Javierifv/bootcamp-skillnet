# 📚 Resumen Completo: Fundamentos de Flask en Python

---

## 1. ¿Qué es Flask y la Arquitectura Petición / Respuesta (*Request / Response*)

* **Flask**: Es un *micro-framework* de desarrollo web en Python. Es ligero, flexible y no impone estructuras rígidas.
* **Ciclo HTTP Request / Response**:
  1. **Cliente (Navegador)** ➔ Envía una solicitud HTTP (`GET` o `POST`) al servidor.
  2. **Servidor Flask (`server.py`)** ➔ Captura la URL en una ruta `@app.route()`, ejecuta lógica de Python y prepara la respuesta.
  3. **Respuesta** ➔ Flask envía la plantilla HTML procesada con datos dinámicos de vuelta al cliente.

---

## 2. Entornos Virtuales (`pipenv`)

Permiten aislar las librerías de cada proyecto para evitar conflictos de versiones con el sistema operativo.

```bash
# Instalación de Flask en la carpeta del proyecto
pipenv install flask

# Activar el entorno virtual
pipenv shell

# Ejecutar el servidor de Flask
python server.py

# Salir del entorno virtual
exit
```

* **`Pipfile`**: Lista de dependencias del proyecto.
* **`Pipfile.lock`**: Detalle exacto de versiones y hashes instalados.

---

## 3. Enrutamiento y Rutas Dinámicas

Flask asocia URLs a funciones de Python mediante el decorador `@app.route()`.

```python
# 1. Ruta Estática Raíz
@app.route('/')
def inicio():
    return '¡Hola Mundo!'

# 2. Rutas Dinámicas con Parámetros y Convertidores de Tipo
@app.route('/saludo/<string:nombre>/<int:veces>')
def saludo(nombre, veces):
    return f"¡Hola {nombre}! " * veces

# 3. Manejador de Errores 404 (Rutas no encontradas)
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "¡Sobrecarga de rutas! No encontramos a donde quieres ir.", 404
```

---

## 4. Motor de Plantillas (Jinja2)

Flask utiliza **Jinja2** para renderizar archivos HTML con lógica de Python.

### Importación y Renderizado en `server.py`:
```python
from flask import Flask, render_template

@app.route('/alumnos')
def mostrar_alumnos():
    lista_estudiantes = [
        {'nombre': 'Elena', 'edad': 25},
        {'nombre': 'Valentina', 'edad': 30}
    ]
    return render_template('alumnos.html', estudiantes=lista_estudiantes)
```

### Sintaxis Jinja2 en HTML:
* **`{{ variable }}`**: Imprime o inyecta el valor de una variable.
* **`{% expresión %}`**: Estructuras de control (`for`, `if`).
* **`{{ HTML_variable|safe }}`**: Permite renderizar cadenas con etiquetas HTML sin escaparlas.

```html
<h2>Listado de Estudiantes</h2>
<ul>
    {% for alumno in estudiantes %}
        <li>{{ alumno['nombre'] }} - {{ alumno['edad'] }} años</li>
    {% endfor %}
</ul>

{% if estudiantes|length > 0 %}
    <p>Hay estudiantes registrados.</p>
{% endif %}
```

---

## 5. Archivos Estáticos (`static/`)

Los archivos que no cambian en el servidor (CSS, JS, imágenes) deben alojarse dentro de la carpeta **`static/`**.

### Uso de `url_for('static', filename=...)`:
Para evitar que las rutas dinámicas rompan los enlaces de archivos estáticos, se utiliza la función `url_for`:

```html
<!-- Enlazar Hoja de Estilos CSS -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">

<!-- Enlazar JavaScript -->
<script src="{{ url_for('static', filename='js/script.js') }}"></script>

<!-- Insertar Imagen -->
<img src="{{ url_for('static', filename='img/logo.png') }}" alt="Logo">
```

---

## 6. Formularios HTTP y el Patrón POST-Redirect-Get (PRG)

### Formulario HTML (`index.html`):
```html
<form action="/crear_usuario" method="POST">
    <label>Nombre:</label>
    <input type="text" name="nombre">
    <button type="submit">Enviar</button>
</form>
```

### Procesamiento en `server.py`:
```python
from flask import Flask, render_template, request, redirect

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    # Acceso a los datos enviados por el formulario (Diccionario request.form)
    nombre = request.form['nombre']
    
    # ⚠️ REGLA DE ORO EN POST: NUNCA renderizar plantilla (render_template) en un POST.
    # SIEMPRE responder con una redirección (redirect) a una ruta GET.
    return redirect('/exito')
```

---

## 7. Sesiones (`session`) y Persistencia de Estado

El protocolo HTTP **no tiene estado** (el servidor olvida todo entre peticiones). Para recordar información a lo largo de la navegación del usuario usamos la **`session`**.

### Configuración y Uso de `session`:
```python
from flask import Flask, request, redirect, session

app = Flask(__name__)
app.secret_key = 'clave_secreta_super_segura'  # 🔑 OBLIGATORIO para cifrar las cookies

@app.route('/login', methods=['POST'])
def login():
    # Guardar en sesión
    session['usuario_nombre'] = request.form['nombre']
    session['visitas'] = session.get('visitas', 0) + 1
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    # Leer de la sesión (disponible también en Jinja2 como {{ session['usuario_nombre'] }})
    nombre = session.get('usuario_nombre')
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    # Borrar datos de la sesión
    session.pop('usuario_nombre', None) # Borra clave específica
    # session.clear() # Borra toda la sesión
    return redirect('/')
```

---

## 8. Inputs Ocultos (`<input type="hidden">`)

Permiten transmitir datos de contexto o identificadores al servidor sin mostrarlos en la pantalla del usuario.

```html
<form action="/buscar_reliquias" method="POST">
    <input type="hidden" name="lugar" value="templo">
    <input type="submit" value="Explorar Templo">
</form>
```

---

## 📁 9. Proyectos y Cores Completados en este Módulo

1. 🧪 **`hola_flask/`**: Configuración básica del servidor, rutas y renderizado con Jinja2.
2. 🛣️ **`practica_comprender_enrutamiento/`**: Rutas dinámicas, convertidores `<int:x>` y manejador de error 404 (Bonus Oro).
3. ⚽ **`practica_juego_pelotas/`**: Renderizado de pelotas/cajas de colores con 1 sola plantilla (Bonus Plata).
4. 🌎 **`core_tabla_paises/`**: Visualización de listas de diccionarios estilizada con Bootstrap (Bonus Plata).
5. 🍏 **`practica_mercado_frutas/`**: Captura de pedidos de frutas y demostración del problema de renderizar en solicitudes POST.
6. 🇲🇽 **`core_loteria_mexicana/`**: Matriz dinámica de $X \times Y$ cartas aleatorias usando `random.sample` y alternancia de colores por residuo `% 3` (Bonus Plata y Oro).
7. 🔢 **`core_visitas/`**: Contador de visitas y reinicios con `session` e incremento personalizado (Bonus Plata y Oro).
8. 🎴 **`practica_loteria_mexicana2/`**: Juego de adivinanza de cartas con `session`, `random.randint` e interfaz adaptativa por colores.
9. 🔮 **`core_juego_destino/`**: Adivino del futuro con formularios, `session`, suerte aleatoria y estilizado en CSS (Bonus Plata y Oro).
10. 🏺 **`reliquias/`**: Juego del explorador con inputs ocultos, uso del filtro `{{|safe}}` y mapeo sin condicionales `if/elif` (Bonus Plata y Oro).
