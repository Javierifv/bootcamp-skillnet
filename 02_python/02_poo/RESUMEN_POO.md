# 📚 Resumen Completo: Programación Orientada a Objetos (POO) en Python

---

## 1. Conceptos Fundamentales
* **Clase (*Class*)**: Moldes o plantillas que definen cómo se comportarán y qué datos tendrán los objetos (nombre en `PascalCase`: `TarjetaCredito`, `Usuario`).
* **Instancia u Objeto**: El elemento concreto fabricado a partir del molde (ej: `usuario1 = Usuario("Elena", ...)`).
* **`self`**: Referencia implícita al objeto específico que está ejecutando el código. Se usa para acceder a sus propios atributos (`self.saldo`).

---

## 2. Componentes de una Clase en Python

```python
class Usuario:
    # Atributo de Clase (Compartido por todas las instancias)
    todas_las_instancias = []

    def __init__(self, nombre, email):
        # Atributos de Instancia
        self.nombre = nombre
        self.email = email
        self.saldo = 0
        Usuario.todas_las_instancias.append(self)

    # Método de Instancia (Retorna self para permitir encadenamiento / Method Chaining)
    def hacer_deposito(self, monto):
        self.saldo += monto
        return self
```

---

## 3. Tipos de Métodos en POO

| Tipo | Decorador | Parámetro | Propósito |
| :--- | :--- | :--- | :--- |
| **Instancia** | *Ninguno* | `self` | Modifica o lee atributos del objeto individual. |
| **Clase** | `@classmethod` | `cls` | Modifica datos de la Clase completa o consulta BD (`SELECT`, `INSERT`). |
| **Estático** | `@staticmethod` | *Ninguno* | Función utilitaria o validación aislada sin necesidad de `self` ni `cls`. |

---

## 4. Asociación entre Clases
Ocurre cuando un atributo de una clase contiene uno o varios objetos de otra clase.

```python
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        # Asociación con la clase TarjetaCredito
        self.tarjetas = {
            "visa": TarjetaCredito(limite_credito=1000, intereses=0.02)
        }
```

---

## 5. Los 4 Pilares de la POO

### 📦 A. Encapsulamiento
Agrupar atributos y métodos relacionados dentro de una misma Clase para mantener el código ordenado y manejable.

### 🧬 B. Herencia y `super()`
Permite que una clase hija reutilice atributos y métodos de una clase padre sin duplicar código.

```python
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_truco(self):
        print(f"{self.nombre} realiza un truco")

class Gato(Animal):
    def __init__(self, nombre, edad, tipo_pelaje):
        super().__init__(nombre, edad)  # Llama al constructor del Padre
        self.tipo_pelaje = tipo_pelaje

    def hacer_truco(self):
        print(f"{self.nombre} te ignora un momento")
        super().hacer_truco()  # Reutiliza el método del Padre
```

### 🎭 C. Polimorfismo
Permite que clases hijas utilicen el mismo nombre de método que su clase padre, pero redefiniendo o personalizando su comportamiento.

### 🕹️ D. Abstracción
Ocultar los detalles internos complejos y ofrecer una interfaz simple para interactuar.

---

## 6. Módulos, Paquetes y la variable `__name__`

* **Módulo**: Archivo individual `.py`.
* **Paquete**: Carpeta que agrupa varios módulos (en Flask incluye un `__init__.py`).
* **Sintaxis de Importación**: `from paquete.modulo import Clase`.
* **Controlador `if __name__ == "__main__":`**:
  * Si el archivo se ejecuta **directamente**, `__name__` vale `"__main__"`.
  * Si el archivo se **importa desde otro script**, `__name__` toma el nombre del módulo (ej: `"tamagotchi"`).

```python
if __name__ == "__main__":
    # Código de prueba o arranque del servidor (solo corre si ejecutas este archivo)
    print("Ejecutando script principal directamente")
```

---

## 7. Entradas y Salidas por Consola (`input()` y `print()`)

* **`input(prompt)`**: Detiene la ejecución y espera a que el usuario ingrese un valor por consola. **Importante**: Siempre retorna un string (`str`).
* **Conversión de Tipos**: Si necesitas ingresar números, debes castear la entrada con `int()` o `float()`.

```python
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))

print(f"¡Hola {nombre}! El próximo año tendrás {edad + 1} años.")
```
