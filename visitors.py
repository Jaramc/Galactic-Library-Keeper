import csv
import os.path

#Definimos el set
id_visitantes = set() #Variable global

#Carga los visitantes del csv para leer, retornamos la lista que esta dentro del archivo
def cargar_visitantes():
    with open("visitantes.csv", "r") as file:
        leer = csv.DictReader(file)
        return list(leer)

#CARGA LOS IDS  
def cargar_ids():
    global id_visitantes
    id_visitantes.clear
    visitantes = cargar_visitantes()
    
    for visitantes in visitantes:
        id_visitantes.add(visitantes["id"])

def obtener_ids(): #Para retornar el set
    cargar_ids()
    return id_visitantes
#Registro del visitante
def registrar_visitantes():
    print("Registrar nuevos visitantes")
    id_existente = obtener_ids()
    while True:
        nuevo_id = input("Ingresa id del visitante: ")
        if nuevo_id in id_existente:
            print(f"El ID {nuevo_id} ya se encuetra registrado, verifica tu id")
        else:
            break
    nombre = input("Ingrese el nombre del visitante: ")
    especie = input("Ingrese la especie del visitante: ")
    while True:
        try:
            estado = int(input("Ingrese estado del visitante (1:activo/2:retirado)"))
            break
        except ValueError:
            print("Ingrese 1 para activo y 2 para retirado")
            
    visitante = {
        "id": nuevo_id,
        "nombre": nombre,
        "especie": especie,
        "estado": estado,
    }
    with open("visitantes.csv", "a") as file: #el "a" es para agregar contenido al final, uno debajo del otro
        campo = ["id", "nombre", "especie", "estado"]
        escribir = csv.DictWriter(file, fieldnames=campo)
        escribir.writerow(visitante)
    print(f"Visitante registrado satisfactoriamente {nuevo_id}")
    
def lista_visitantes():
    print("LISTA DE VISITANTES")
    visitantes = cargar_visitantes
    if not visitantes:
        print("Visitante no registrado")
        return
    
    for visitante in visitante:
        campos = (visitante["id"], visitante["nombre"], visitante["especie"], visitante["estado"])
        print(f"ID: {campos[0]} \n Nombre: {campos[1]} \n Especie: {campos[2]} \n Estado: {campos[3]}")
        

def busqueda_visitante():
    print("BUSCAR VISITANTE")
    buscar_id  = input("Ingrese el id del visitante que desea buscar: ")
    visitantes = cargar_visitantes()
    for visitante in  visitantes:
        if visitante["id"] == buscar_id:
            print(f"ID: {visitante["id"]}")
            print(f"Nombre: {visitante["nombre"]}")
            print(f"Especie: {visitante["especie"]}")
            print(f"Estado: {visitante["estado"]}")
            return
    print("El ID de el visitante noo fue encontrado")
    
def actualizar_estado():
    print("ACTUALIZAR ESTADO DEL VISITANTE")
    buscar_id  = input("Ingrese el id del visitante que desea buscar: ")
    visitantes = cargar_visitantes()
    if not visitantes:
        print("Visitante no registrado")
        return
    buscar = False
    for visitante in  visitantes:
        if visitante["id"] == buscar_id:
            buscar = True
            estado_actual = visitante["estado"]
            print(f"Estado actual: {visitante["estado"]}")
            
            if estado_actual == "1":
                print("Cambiar a retirado?")
                cambiar = input("Presione 2 para confirmar: ")
                if cambiar == "2":
                    visitante["estado"] = 2
                    print("El estado se ha actualizado")
                else:
                    print("El estado fue cancelado")
                    return
            elif estado_actual == "2":
                print("Cambiar a activo?")
                cambiar = input("Presione 1 para confirmar")
                if cambiar == "1":
                    visitante["estado"] = 1
                    print("El estado se ha actualizado")
                else:
                    print("El estado fue cancelado")
                    return
            break
    if not buscar:
        print("El id es incorrecro")
        return
    with open("visitantes.csv", "w") as file:
        campo = ["id", "nombre", "especie", "estado"]
        
        rellenar = csv.DictWriter(file, fieldnames= campo)
        rellenar.writeheader()
        rellenar.writerows(visitantes)
    print("Estado actualizado")

def eliminar_visitante():
    print("ELIMINAR VISITANTE")
    buscar_id  = input("Ingrese el id del visitante que desea buscar: ")
    visitantes = cargar_visitantes()
    if not visitantes:
        print("Visitante no registrado")
        return
    buscar = False
    for visitante in visitantes:
        if visitante ["id"] == buscar_id:
            buscar = True
            visitante ["estado"] = "Eliminado"
    if not buscar:
        print("El visitante no fue encontrado")
        return
    
    with open("visitantes.csv", "w") as file:
        campo = ["id", "nombre", "especie", "estado"]
        
        rellenar = csv.DictWriter(file, fieldnames= campo)
        rellenar.writeheader()
        rellenar.writerows(visitantes)
    print("Visitante se marco como eliminado")
    

def calcular_estadisticas():
    visitantes = cargar_visitantes()
    if not visitantes:
        print("No hay visitantes registrados.")
        return None
    ids_unicos = {visitante["id"] for visitante in visitantes}
    ids_activos = {
        visitante["id"]
        for visitante in visitantes
        if visitante["estado"] == "1"
    }
    ids_retirados = {
        visitante["id"]
        for visitante in visitantes
        if visitante["estado"] == "2"
    }
    ids_eliminados = {
        visitante["id"]
        for visitante in visitantes
        if visitante["estado"] == "Eliminado"
    }
    visitantes_por_especie = {}
    for visitante in visitantes:
        especie = visitante["especie"]
        
        if especie not in visitantes_por_especie:
            visitantes_por_especie[especie] = 0
        visitantes_por_especie[especie] += 1
    estadisticas = {
        "total_visitantes_unicos": len(ids_unicos),
        "activos": len(ids_activos),
        "retirados": len(ids_retirados),
        "eliminados": len(ids_eliminados),
        "por_especie": visitantes_por_especie,
    }
    return estadisticas

def mostrar_estadisticas():
    estadisticas = calcular_estadisticas()
    if not estadisticas:
        return
    print("ESTADÍSTICAS DE VISITANTES")
    print("Total de visitantes únicos:", estadisticas["total_visitantes_unicos"])
    print("Activos:", estadisticas["activos"])
    print("Retirados:", estadisticas["retirados"])
    print("Eliminados:", estadisticas["eliminados"])
    print("Visitantes por especie:")
    for especie, cantidad in estadisticas["por_especie"].items():
        print(f"  {especie}: {cantidad}")

def varios_registros(*datos_visitantes):
    print(f"Registrando{len(datos_visitantes)}")
    ids_existentes = obtener_ids
    registrados = 0
    for datos in datos_visitantes:
        if len(datos) != 4:
            print(f"Error {datos} se esperaba id, nombre, especie, estado")
        else:
            nuevo_id, nombre, especie, estado = datos
        if nuevo_id in ids_existentes:
            print(f"El ID ya existe {nuevo_id}")
        else:
            visitante = {
                "id": nuevo_id,
                "nombre": nombre,
                "especie": especie,
                "estado": estado,
            }
        with open ("visitantes.csv", "a") as file:
            campo = ["id", "nombre", "especie", "estado"]
            escribir = csv.DictWriter(file, fieldnames=campo)
            escribir.writerow(visitante)
        id_visitantes.add(nuevo_id)
        registrados +=1
    print(f"Los registros fueron un exito{registrados}/{len(datos_visitantes)}")

def menu_visitantes():
    while True:
        print("MENU DE VISITANTES")
        print("1. Registrar Nuevo Visitante")
        print("2. Listar Visitantes")
        print("3. Buscar Visitante")
        print("4. Actualizar Estado")
        print("5. Eliminar Visitante")
        print("6. Mostrar Estadísticas")
        print("7. Registrar Múltiples Visitantes (*args)")
        print("8. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case '1':
                registrar_visitantes()
            case '2':
                lista_visitantes()
            case '3':
                busqueda_visitante()
            case '4':
                actualizar_estado()
            case '5':
                eliminar_visitante()
            case '6':
                mostrar_estadisticas()
            case '7':
                varios_registros()
            case '8':
                print("Volviendo al menú principal...")
                break