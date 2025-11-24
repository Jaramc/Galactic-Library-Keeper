import csv
import os.path

def leer_csv(archivo):
    
    if not os.path.exists(archivo):
        print(f"El archivo {archivo} no existe.")
        return []
    
    with open(archivo, "r") as file:
        lector = csv.DictReader(file)
        return list(lector)

def escribir_csv(archivo, datos, campos):

    with open(archivo, "w") as file:
        escritor = csv.DictWriter(file, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos)

def agregar_linea_csv(archivo, datos, campos):

    archivo_existe = os.path.exists(archivo)
    
    with open(archivo, "a") as file:
        escritor = csv.DictWriter(file, fieldnames=campos)
        
        # Si el archivo no existe o está vacío, escribir encabezados
        if not archivo_existe or os.path.getsize(archivo) == 0:
            escritor.writeheader()
        
        escritor.writerow(datos)

def existe_archivo(archivo):

    return os.path.exists(archivo)

def verificar_id_unico(archivo, campo_id, valor_id):

    datos = leer_csv(archivo)
    ids_existentes = {fila[campo_id] for fila in datos if campo_id in fila}
    return valor_id not in ids_existentes

def obtener_ids_set(archivo, campo_id):

    datos = leer_csv(archivo)
    return {fila[campo_id] for fila in datos if campo_id in fila}
