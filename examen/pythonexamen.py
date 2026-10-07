"""
Nombre: Mia Karolina Lujan Villavicencio
Fecha: 24 de septiembre de 2026
Cómo usar este programa:
    -i / --input   Archivo CSV de entrada con columnas "Frase" y "Pelicula"
    -o / --output  Archivo CSV de salida donde se guardan los cambios

Uso de IA: 
Me apoyé en la autocompletación del copilot integrado en VSC, al igual que para
revision del codigo y simplificar utilicé Claude (Claude Sonnet 5).


"""

"""Un archivo de python que puede leer y escribir un archivo csv que contiene un 
listado de frases célebres y la película en la que se dijo cada frase. """

import argparse
import csv

class Frase:
    """Representa una frase celebre y la pelicula en la que fue dicha."""

    def __init__(self, texto, pelicula):
        self.texto = texto.strip()
        self.pelicula = pelicula.strip()

    def __str__(self):
        return f'"{self.texto}" — {self.pelicula}'

    def contiene_palabra(self, palabra):
        """True si 'palabra' aparece en el texto (sin distinguir mayusculas)."""
        return palabra.lower() in self.texto.lower()


def leer_frases_csv(ruta):
    """Lee un archivo CSV con columnas 'Frase' y 'Pelicula' y regresa una lista de Frase."""
    frases = []
    with open(ruta, "r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            texto = (fila.get("Frase") or "").strip()
            pelicula = (fila.get("Película") or fila.get("Pelicula") or "").strip()
            if texto:
                frases.append(Frase(texto, pelicula))
    return frases


def escribir_frases_csv(ruta, frases):
    """Escribe la lista de Frase en un CSV con columnas 'Frase' y 'Pelicula'."""
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Frase", "Película"])
        for frase in frases:
            escritor.writerow([frase.texto, frase.pelicula])


def buscar_palabra(frases, palabra):
    """Regresa las frases que contienen 'palabra' en su texto."""
    return [f for f in frases if f.contiene_palabra(palabra)]


def contar_palabras_distintas(frases):
    """Cuenta cuantas palabras distintas (no repetidas) hay entre todas las frases."""
    signos = ".,;:!?¡¿'\"()—-"
    palabras = set()
    for frase in frases:
        for palabra in frase.texto.split():
            limpia = palabra.strip(signos).lower()
            if limpia:
                palabras.add(limpia)
    return len(palabras)


def contar_peliculas_distintas(frases):
    """Cuenta cuantas peliculas distintas (no repetidas) hay."""
    return len({f.pelicula for f in frases if f.pelicula})


def frases_por_pelicula(frases):
    """Regresa lista de (pelicula, cantidad) ordenada de mayor a menor."""
    conteo = {}
    for f in frases:
        if f.pelicula:
            conteo[f.pelicula] = conteo.get(f.pelicula, 0) + 1
    return sorted(conteo.items(), key=lambda par: par[1], reverse=True)


def mostrar_menu():
    print("\n===== FRASES =====")
    print("1. Buscar palabra")
    print("2. Agregar frase")
    print("3. Ver estadísticas")
    print("4. Frases por película (mayor a menor)")
    print("5. Salir")


def opcion_buscar(frases):
    palabra = input("Escribe la palabra a buscar: ").strip()
    if not palabra:
        print("Debes escribir una palabra.")
        return
    encontradas = buscar_palabra(frases, palabra)
    if not encontradas:
        print(f"No se encontraron frases con '{palabra}'.")
        return
    print(f"\nSe encontraron {len(encontradas)} frase(s):")
    for frase in encontradas:
        print(frase)


def opcion_agregar(frases, ruta_salida):
    texto = input("Escribe la frase: ").strip()
    pelicula = input("Escribe el nombre de la película: ").strip()
    if not texto or not pelicula:
        print("Debes escribir la frase y la película.")
        return
    frases.append(Frase(texto, pelicula))
    escribir_frases_csv(ruta_salida, frases)
    print(f"Frase agregada y guardada en '{ruta_salida}'.")


def opcion_estadisticas(frases):
    print(f"\nNúmero de frases:              {len(frases)}")
    print(f"Número de palabras distintas:  {contar_palabras_distintas(frases)}")
    print(f"Número de películas distintas: {contar_peliculas_distintas(frases)}")


def opcion_frases_por_pelicula(frases):
    print()
    for pelicula, cantidad in frases_por_pelicula(frases):
        print(f"{cantidad:>3}  {pelicula}")


def main():
    parser = argparse.ArgumentParser(
        description="Administrador de frases célebres (lectura/escritura de CSV)."
    )
    parser.add_argument(
        "-i", "--input", default="frases_consolidadas_ampliadas.csv",
        help="Archivo CSV de entrada (por defecto: frases_consolidadas_ampliadas.csv)"
    )
    parser.add_argument(
        "-o", "--output", default=None,
        help="Archivo CSV de salida (por defecto, el mismo de entrada)"
    )
    args = parser.parse_args()
    ruta_salida = args.output if args.output else args.input

    try:
        frases = leer_frases_csv(args.input)
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo de entrada '{args.input}'.")
        return

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ").strip()
        if opcion == "1":
            opcion_buscar(frases)
        elif opcion == "2":
            opcion_agregar(frases, ruta_salida)
        elif opcion == "3":
            opcion_estadisticas(frases)
        elif opcion == "4":
            opcion_frases_por_pelicula(frases)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
