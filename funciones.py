def leerArchivoToken():
    file = "/home/gerardohuerta1502/Escritorio/Python/informacion.txt"
    try:
        with open(file, "r+") as archivo:
            firstLine = archivo.readline()
            return firstLine
    except FileNotFoundError:
        return f"El archivo {file} no se ha encontrado"
    except IOError:
        return f"Error al intentar leer el archivo {file}"
    except Exception as e:
        return f"Error inesperado"
