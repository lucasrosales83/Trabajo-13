import mysql.connector
from mysql.connector import Error

# ==============================
# CONFIGURACIÓN DE CONEXIÓN
# ==============================
HOST = "buv9i87h4otuvwok1mt2-mysql.services.clever-cloud.com"
USER = "utxf7nswgmwmpkdq"
PASSWORD = "xgvrfzGpIjIPlP8T0HUf"
DB = "buv9i87h4otuvwok1mt2"


def get_connection():
    """
    Retorna una conexión a la base de datos de Clever Cloud.
    """
    try:
        connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DB,
            port=3306,
            ssl_disabled=False,
        )
        return connection
    except Error as e:
        print("❌ ERROR DE CONEXIÓN:", e)
        return None


# ==============================
# FUNCIONES CRUD - DIRECTORES
# ==============================
def listar_directores():
    connection = get_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT id_director, nombre, apellido, nacionalidad FROM directores")
        rows = cursor.fetchall()

        print("\n=== LISTA DE DIRECTORES ===")
        if not rows:
            print("No hay directores cargados.")
        else:
            for row in rows:
                print(f"[{row[0]}] {row[1]} {row[2]} - {row[3]}")
        print()
    except Error as e:
        print(f"Error al listar directores: {e}")
    finally:
        cursor.close()
        connection.close()


def agregar_director():
    print("\n=== AGREGAR DIRECTOR ===")
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    nacionalidad = input("Nacionalidad (Enter para 'Argentina'): ").strip() or "Argentina"

    connection = get_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        sql = "INSERT INTO directores (nombre, apellido, nacionalidad) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, apellido, nacionalidad))
        connection.commit()
        print("Director agregado correctamente.\n")
    except Error as e:
        print(f"Error al agregar director: {e}")
    finally:
        cursor.close()
        connection.close()


# ==============================
# FUNCIONES CRUD - PELÍCULAS
# ==============================
def listar_peliculas():
    connection = get_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        sql = """
            SELECT p.id_pelicula, p.titulo, p.anio_estreno, p.genero,
                   d.nombre, d.apellido
            FROM peliculas p
            JOIN directores d ON p.id_director = d.id_director
            ORDER BY p.anio_estreno;
        """
        cursor.execute(sql)
        rows = cursor.fetchall()

        print("\n=== LISTA DE PELÍCULAS ===")
        if not rows:
            print("No hay películas cargadas.")
        else:
            for row in rows:
                id_pelicula, titulo, anio, genero, nom_dir, ape_dir = row
                print(f"[{id_pelicula}] {titulo} ({anio}) - {genero} - Dir: {nom_dir} {ape_dir}")
        print()
    except Error as e:
        print(f"Error al listar películas: {e}")
    finally:
        cursor.close()
        connection.close()


def agregar_pelicula():
    print("\n=== AGREGAR PELÍCULA ===")
    titulo = input("Título: ").strip()
    anio = input("Año de estreno: ").strip()
    duracion = input("Duración (minutos): ").strip()
    genero = input("Género: ").strip()

    print("\nDirectores disponibles:")
    listar_directores()
    id_director = input("ID del director: ").strip()

    if not titulo or not anio or not id_director:
        print("Título, año e ID de director son obligatorios.\n")
        return

    connection = get_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        sql = """
            INSERT INTO peliculas (titulo, anio_estreno, duracion_minutos, genero, id_director)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (titulo, int(anio), int(duracion or 0), genero, int(id_director)))
        connection.commit()
        print("Película agregada correctamente.\n")
    except Error as e:
        print(f"Error al agregar película: {e}")
    finally:
        cursor.close()
        connection.close()


def actualizar_pelicula():
    print("\n=== ACTUALIZAR PELÍCULA ===")
    listar_peliculas()
    id_pelicula = input("Ingrese el ID de la película a actualizar: ").strip()

    if not id_pelicula:
        print("Debe ingresar un ID.\n")
        return

    nuevo_titulo = input("Nuevo título (Enter para mantener): ").strip()
    nuevo_genero = input("Nuevo género (Enter para mantener): ").strip()

    connection = get_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT titulo, genero FROM peliculas WHERE id_pelicula = %s", (id_pelicula,))
        row = cursor.fetchone()
        if not row:
            print("No se encontró una película con ese ID.\n")
            return

        titulo_actual, genero_actual = row
        titulo_final = nuevo_titulo or titulo_actual
        genero_final = nuevo_genero or genero_actual

        sql = "UPDATE peliculas SET titulo = %s, genero = %s WHERE id_pelicula = %s"
        cursor.execute(sql, (titulo_final, genero_final, id_pelicula))
        connection.commit()
        print("Película actualizada correctamente.\n")
    except Error as e:
        print(f"Error al actualizar película: {e}")
    finally:
        cursor.close()
        connection.close()


def eliminar_pelicula():
    print("\n=== ELIMINAR PELÍCULA ===")
    listar_peliculas()
    id_pelicula = input("Ingrese el ID de la película a eliminar: ").strip()

    if not id_pelicula:
        print("Debe ingresar un ID.\n")
        return

    confirmar = input(f"¿Seguro que desea eliminar la película {id_pelicula}? (s/n): ").strip().lower()
    if confirmar != 's':
        print("Operación cancelada.\n")
        return

    connection = get_connection()
    if not connection:
        return

    try:
        cursor = connection.cursor()
        sql = "DELETE FROM peliculas WHERE id_pelicula = %s"
        cursor.execute(sql, (id_pelicula,))
        connection.commit()

        if cursor.rowcount == 0:
            print("No se eliminó ninguna película (verificar ID).\n")
        else:
            print("Película eliminada correctamente.\n")
    except Error as e:
        print(f"Error al eliminar película: {e}")
    finally:
        cursor.close()
        connection.close()


# ==============================
# MENÚ PRINCIPAL
# ==============================
def mostrar_menu():
    print("=== Sistema de Gestión de Cine Argentino ===")
    print("1. Listar películas")
    print("2. Agregar película")
    print("3. Actualizar película")
    print("4. Eliminar película")
    print("5. Listar directores")
    print("6. Agregar director")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            listar_peliculas()
        elif opcion == "2":
            agregar_pelicula()
        elif opcion == "3":
            actualizar_pelicula()
        elif opcion == "4":
            eliminar_pelicula()
        elif opcion == "5":
            listar_directores()
        elif opcion == "6":
            agregar_director()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")


if __name__ == "__main__":
    main()
 