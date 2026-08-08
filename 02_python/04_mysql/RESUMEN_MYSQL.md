# 🗄️ Resumen Completo: MySQL & Bases de Datos Relacionales (Skillnest)

---

## 📌 PARTE 1: Diseño de Bases de Datos & Diagramas Entidad-Relación (ERD)

### 1. El Mantra Supremo: *¡No te repitas! (D.R.Y.)*
* **Objetivo de la normalización**: Evitar duplicar textos o listas en múltiples registros, reduciendo el espacio en disco y garantizando la integridad de los datos.
* **Separación de responsabilidades**: Cada tabla almacena exclusivamente datos de una sola entidad (`usuarios`, `productos`, `pedidos`).

---

### 2. Convenciones y Estándares de Industria en MySQL

| Elemento | Convención | Ejemplo Correcto | Ejemplo Incorrecto |
| :--- | :--- | :--- | :--- |
| **Nombre de Tablas** | Plural y minúsculas (*snake_case*) | `usuarios`, `publicaciones` | `Usuario`, `USUARIOS` |
| **Llave Primaria (PK)** | Se llama simplemente **`id`** con Auto-Incremento (`AI`) | `id` | `id_usuario`, `usuario_id` |
| **Llave Foránea (FK)** | Singular de la tabla padre + `_id` | `usuario_id`, `curso_id` | `usuarios_id`, `cursos_id` |
| **Timestamps** | **`created_at`** y **`updated_at`** (`DATETIME`) | `created_at`, `updated_at` | `fecha_creacion`, `fecha` |

---

### 3. Tipos de Datos Más Utilizados

* **`VARCHAR(N)`**: Cadenas de texto de longitud variable hasta 255 caracteres (`VARCHAR(45)` para nombres, `VARCHAR(100)` para emails, `VARCHAR(255)` para contraseñas encriptadas).
* **`CHAR(N)`**: Cadenas de texto de longitud fija (RUT/DNI, códigos de país `CHAR(3)`).
* **`TEXT`**: Textos largos de hasta 65,535 caracteres (contenido de posts, comentarios, biografías).
* **`INT`**: Números enteros de 4 bytes (llaves primarias `id`, cantidades, contadores).
* **`TINYINT`**: Enteros de 1 byte (0 a 255). Reemplaza al tipo `BOOLEAN` (`0` = Falso, `1` = Verdadero, roles o estrellas de valoración del 1 al 5).
* **`FLOAT` / `DECIMAL`**: Números con punto decimal (precios, promedios, calificaciones).
* **`DATETIME`**: Fechas y horas en formato `AAAA-MM-DD hh:mm:ss`.

---

### 4. Las Relaciones entre Tablas

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. Relación Uno a Uno (1:1)                                                │
│    * Un registro en A se conecta con como máximo un registro en B.         │
│    * Ejemplo: Usuario (1) ↔ Dirección (1), Vehículo (1) ↔ Póliza (1).       │
│                                                                             │
│ 2. Relación Uno a Muchos (1:N)                                              │
│    * Un registro en A se conecta con muchos registros en B.                 │
│    * REGLA DE ORO: La Llave Foránea (FK) SIEMPRE se coloca en el "MUCHOS".  │
│    * Ejemplo: Usuario (1) ➔ Pedidos (N), Curso (1) ➔ Estudiantes (N).       │
│                                                                             │
│ 3. Relación Muchos a Muchos (N:M)                                           │
│    * Muchos registros en A se conectan con muchos registros en B.          │
│    * REGLA DE ORO: Requiere una TERCERA TABLA INTERMEDIA (Junction Table).  │
│    * La tabla intermedia almacena (FK_A, FK_B) como Llave Compuesta.       │
│    * Ejemplo: Usuarios (N) ↔ Canciones (M) [Tabla intermedia: favoritos]. │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 5. Las 3 Formas Normales de la Normalización

1. **Primera Forma Normal (1FN) - Valores Atómicos**:
   * Cada celda contiene **un solo valor** (prohibido guardar listas o comas en una celda de texto).
2. **Segunda Forma Normal (2FN) - Sin Textos Repetidos**:
   * Las categorías o textos descriptivos repetidos deben extraerse a su propia tabla catálogo con un `id`.
3. **Tercera Forma Normal (3FN) - Dependencia Exclusiva de la PK**:
   * Ningún campo debe depender de otra columna secundaria. Toda columna no-clave debe depender **única y exclusivamente del `id`**.

---

### 6. Catálogo de Modelos ERD Construidos y Validados

* 👤 **`esquema_usuarios`**: Modelo base con `usuarios` y Bonus Plata de columnas adicionales.
* 🎓 **`esquema_estudiantes_cursos` (Core)**: Relación 1:N entre cursos y estudiantes.
* 🎵 **`esquema_canciones` (Core)**: Relación N:M entre usuarios y canciones con la tabla intermedia `favoritos`.
* 👥 **`esquema_seguidores` (Práctica)**: Auto-Unión (*Self-Join* N:M) de usuarios con usuarios.
* 📋 **`esquema_administrador_proyectos` (Opcional)**: Creador del proyecto (1:N) y colaboradores miembros (N:M).
* 📰 **`esquema_blog` (Opcional)**: CMS completo con blogs, co-administradores (N:M), posts, comentarios, visitas y adjuntos.
* 🛡️ **`esquema_administrador_usuarios` (Opcional)**: Doble relación 1:N simultánea entre `usuarios` y `mensajes` (`autor_id` y `receptor_id`).
* 🧹 **`esquema_normalizacion` (Opcional)**: Descomposición de tabla monolítica en 1FN, 2FN y 3FN.

---

## 📌 PARTE 2: Consultas SQL (SQL Queries)

* **SQL (*Structured Query Language*)**: Lenguaje estándar para administrar, consultar y manipular bases de datos relacionales.
* **Operaciones Principales**:
  * **C (Create)**: `INSERT INTO`
  * **R (Read)**: `SELECT ... FROM ... WHERE ...`
  * **U (Update)**: `UPDATE ... SET ... WHERE ...`
  * **D (Delete)**: `DELETE FROM ... WHERE ...`
  * **Uniones**: `INNER JOIN`, `LEFT JOIN`
