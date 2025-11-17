# 🎬 Sistema de Gestión de Cine Nacional (Python + MySQL)

## 👤 Datos del alumno
- **Alumno:** Lucas Rosales  
- **Curso:** 6° Año "E"  
- **Especialidad:** Programación  
- **Colegio:** IPET 247 Ing. Carlos A. Cassaffousth  
- **Materia:** Base de Datos  
- **Profesor:** Moisés Tinte  

---

## 📌 Descripción del proyecto
Este proyecto consiste en un sistema de gestión de películas del cine argentino.

Permite:
- Listar películas y directores
- Agregar películas y directores
- Actualizar datos
- Eliminar registros

El sistema funciona mediante un **menú interactivo en consola**, conectado a una base de datos MySQL alojada en **Clever Cloud**.

---

## 🗄 Base de datos

### 🔹 Nombre: `Cine_Nacional`

### 🔹 Tablas

#### `directores`
| Campo | Tipo | Detalle |
|-------|------|---------|
| id_director | INT PK | Autoincremental |
| nombre | VARCHAR(100) | No nulo |
| apellido | VARCHAR(100) | No nulo |
| nacionalidad | VARCHAR(50) | Default 'Argentina' |

#### `peliculas`
| Campo | Tipo | Detalle |
|-------|------|---------|
| id_pelicula | INT PK | Autoincremental |
| titulo | VARCHAR(200) | No nulo |
| anio_estreno | INT | No nulo |
| duracion_minutos | INT | Opcional |
| genero | VARCHAR(50) | Opcional |
| id_director | INT FK | Relación con directores |

---

## 🛠 Instalación y Configuración

### 1️⃣ Clonar el proyecto o copiar los archivos

Trabajo-13/
├─ db/
│ ├─cine_nacional.sql
├─ screenshots/
│ ├─ screenshot1
│ ├─ screenshot2
├─ src/
│ ├─ app.py
├─ README.md

---

### 2️⃣ Instalar dependencias

pip install mysql-connector-python

---

### 3️⃣ Configurar conexión

Editar **src/db_config.py**:

```python
HOST = "buv9i87h4otuvwok1mt2-mysql.services.clever-cloud.com"
USER = "utxf7nsgwmmpkdq"
PASSWORD = "xgvrfzGpIjIPlP8T0HUf"
DB = "buv9i87h4otuvwok1mt2"

---

### 4️⃣ Ejecutar el programa

Desde la carpeta src:
py app.py

Ejemplo de uso del menú

=== Sistema de Gestión de Cine Argentino ===
1. Listar películas
2. Agregar película
3. Actualizar película
4. Eliminar película
5. Listar directores
6. Agregar director
0. Salir
Seleccione una opción: 1
Resultado de ejemplo:

=== LISTA DE PELÍCULAS ===
[8] Nueve Reinas (2000) – Suspenso – Dir: Fabián Bielinsky
[1] La ciénaga (2001) – Drama – Dir: Lucrecia Martel
[3] Relatos salvajes (2014) – Comedia negra – Dir: Damián Szifron

### 5️⃣ Capturas de pantalla

Las capturas de la ejecución del programa se encuentran dentro de la carpeta:

/screenshots

screenshot1.png

Muestra el menú principal del sistema y el resultado de la opción “1 – Listar películas”.

En esta captura se puede ver:

El menú con todas las opciones disponibles

La consulta a la base de datos en acción

La lista completa de películas obtenidas desde MySQL junto con:

Año de estreno

Género

Nombre del director

Esto confirma que:
La conexión funciona correctamente
El programa consulta y muestra los datos reales desde la base remota

screenshot2.png

Muestra dos procesos consecutivos:

1️⃣ Listado de directores existentes
2️⃣ Ingreso de un nuevo director (Mariano Cohn)
3️⃣ Nueva consulta que confirma que fue agregado correctamente

Se observa:

La ejecución de la opción “6 – Agregar director”

El ingreso de nombre, apellido y nacionalidad

Un mensaje de confirmación: “Director agregado correctamente.”

Una nueva lista actualizada mostrando el ID asignado

Esto demuestra que:
El sistema inserta datos en MySQL
Las operaciones CRUD funcionan correctamente
El usuario visualiza los cambios en tiempo real