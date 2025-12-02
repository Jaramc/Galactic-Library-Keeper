import storage

# Definimos el set para IDs únicos
id_artefactos = set()  # Variable global

# Carga los artefactos del csv
def cargar_artefactos():
    return storage.leer_csv("artefactos.csv")

# Cargar los IDs
def cargar_ids():
    global id_artefactos
    id_artefactos.clear()
    artefactos = cargar_artefactos()
    
    for artefacto in artefactos:
        id_artefactos.add(artefacto["codigo"])

def obtener_ids():
    cargar_ids()
    return id_artefactos

# Registro de artefacto (reutilizando lógica de visitors)
def registrar_artefacto():
    print("Registrar nuevo artefacto")
    id_existente = obtener_ids()
    while True:
        nuevo_codigo = input("Ingresa código del artefacto: ")
        if nuevo_codigo in id_existente:
            print(f"El código {nuevo_codigo} ya se encuentra registrado, verifica tu código")
        else:
            break
    descripcion = input("Ingrese la descripción del artefacto: ")
    
    print("Nivel de rareza:")
    print("1. Bajo")
    print("2. Medio")
    print("3. Alto")
    print("4. Prohibido")
    while True:
        try:
            rareza_opcion = int(input("Ingrese nivel de rareza (1-4): "))
            if rareza_opcion == 1:
                rareza = "Bajo"
                break
            elif rareza_opcion == 2:
                rareza = "Medio"
                break
            elif rareza_opcion == 3:
                rareza = "Alto"
                break
            elif rareza_opcion == 4:
                rareza = "Prohibido"
                break
            else:
                print("Ingrese un número entre 1 y 4")
        except ValueError:
            print("Ingrese un número válido")
    
    print("Estatus del artefacto:")
    print("1. Almacenado")
    print("2. En Estudio")
    print("3. Destruido")
    while True:
        try:
            estatus_opcion = int(input("Ingrese estatus (1-3): "))
            if estatus_opcion == 1:
                estatus = "Almacenado"
                break
            elif estatus_opcion == 2:
                estatus = "En Estudio"
                break
            elif estatus_opcion == 3:
                estatus = "Destruido"
                break
            else:
                print("Ingrese un número entre 1 y 3")
        except ValueError:
            print("Ingrese un número válido")
            
    artefacto = {
        "codigo": nuevo_codigo,
        "descripcion": descripcion,
        "rareza": rareza,
        "estatus": estatus,
    }
    campo = ["codigo", "descripcion", "rareza", "estatus"]
    storage.agregar_linea_csv("artefactos.csv", artefacto, campo)
    print(f"Artefacto registrado satisfactoriamente: {nuevo_codigo}")

# Listar artefactos (reutilizando lógica de visitors)
def listar_artefactos():
    print("LISTA DE ARTEFACTOS")
    artefactos = cargar_artefactos()
    if not artefactos:
        print("No hay artefactos registrados")
        return
    
    for artefacto in artefactos:
        campos = (artefacto["codigo"], artefacto["descripcion"], artefacto["rareza"], artefacto["estatus"])
        print(f"Código: {campos[0]}\nDescripción: {campos[1]}\nRareza: {campos[2]}\nEstatus: {campos[3]}\n")

# Buscar artefacto (reutilizando lógica de visitors)
def buscar_artefacto():
    print("BUSCAR ARTEFACTO")
    buscar_codigo = input("Ingrese el código del artefacto que desea buscar: ")
    artefactos = cargar_artefactos()
    for artefacto in artefactos:
        if artefacto["codigo"] == buscar_codigo:
            print(f"Código: {artefacto['codigo']}")
            print(f"Descripción: {artefacto['descripcion']}")
            print(f"Rareza: {artefacto['rareza']}")
            print(f"Estatus: {artefacto['estatus']}")
            return
    print("El código del artefacto no fue encontrado")

# Clasificar artefactos por rareza usando **kwargs (requisito obligatorio)
def clasificar_artefactos(**kwargs):
    print("CLASIFICAR ARTEFACTOS POR RAREZA")
    artefactos = cargar_artefactos()
    
    if not artefactos:
        print("No hay artefactos registrados")
        return
    
    # Obtener filtro de rareza desde kwargs
    rareza_filtro = kwargs.get("rareza", None)
    mostrar_estadisticas = kwargs.get("mostrar_estadisticas", False)
    
    # Si se especifica una rareza, filtrar
    if rareza_filtro:
        print(f"Filtrando artefactos por rareza: {rareza_filtro}")
        artefactos_filtrados = [art for art in artefactos if art["rareza"] == rareza_filtro]
        
        if not artefactos_filtrados:
            print(f"No hay artefactos con rareza {rareza_filtro}")
            return
        
        for artefacto in artefactos_filtrados:
            print(f"- {artefacto['codigo']}: {artefacto['descripcion']} ({artefacto['estatus']})")
    else:
        # Mostrar todos clasificados por rareza
        clasificacion = {}
        for artefacto in artefactos:
            rareza = artefacto["rareza"]
            if rareza not in clasificacion:
                clasificacion[rareza] = []
            clasificacion[rareza].append(artefacto)
        
        for rareza, arts in clasificacion.items():
            print(f"\n{rareza}: {len(arts)} artefacto(s)")
            for art in arts:
                print(f"  - {art['codigo']}: {art['descripcion']} ({art['estatus']})")
    
    if mostrar_estadisticas:
        print("\n--- ESTADÍSTICAS ---")
        print(f"Total de artefactos: {len(artefactos)}")

# Eliminar artefacto (reutilizando lógica de visitors)
def eliminar_artefacto():
    print("ELIMINAR ARTEFACTO")
    buscar_codigo = input("Ingrese el código del artefacto que desea eliminar: ")
    artefactos = cargar_artefactos()
    if not artefactos:
        print("No hay artefactos registrados")
        return
    
    buscar = False
    for artefacto in artefactos:
        if artefacto["codigo"] == buscar_codigo:
            buscar = True
            artefacto["estatus"] = "Destruido"
    
    if not buscar:
        print("El artefacto no fue encontrado")
        return
    
    campo = ["codigo", "descripcion", "rareza", "estatus"]
    storage.escribir_csv("artefactos.csv", artefactos, campo)
    print("Artefacto marcado como Destruido")

# Mostrar estadísticas (reutilizando lógica de visitors)
def mostrar_estadisticas_artefactos():
    artefactos = cargar_artefactos()
    if not artefactos:
        print("No hay artefactos registrados.")
        return
    
    codigos_unicos = {artefacto["codigo"] for artefacto in artefactos}
    almacenados = {artefacto["codigo"] for artefacto in artefactos if artefacto["estatus"] == "Almacenado"}
    en_estudio = {artefacto["codigo"] for artefacto in artefactos if artefacto["estatus"] == "En Estudio"}
    destruidos = {artefacto["codigo"] for artefacto in artefactos if artefacto["estatus"] == "Destruido"}
    
    artefactos_por_rareza = {}
    for artefacto in artefactos:
        rareza = artefacto["rareza"]
        if rareza not in artefactos_por_rareza:
            artefactos_por_rareza[rareza] = 0
        artefactos_por_rareza[rareza] += 1
    
    print("ESTADÍSTICAS DE ARTEFACTOS")
    print("Total de artefactos únicos:", len(codigos_unicos))
    print("Almacenados:", len(almacenados))
    print("En Estudio:", len(en_estudio))
    print("Destruidos:", len(destruidos))
    print("Artefactos por rareza:")
    for rareza, cantidad in artefactos_por_rareza.items():
        print(f"  {rareza}: {cantidad}")

# Menú de artefactos
def menu_artefactos():
    while True:
        print("\nMENU DE ARTEFACTOS")
        print("1. Registrar Nuevo Artefacto")
        print("2. Listar Artefactos")
        print("3. Buscar Artefacto")
        print("4. Clasificar Artefactos por Rareza (**kwargs)")
        print("5. Mostrar Estadísticas")
        print("6. Eliminar Artefacto")
        print("7. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case '1':
                registrar_artefacto()
            case '2':
                listar_artefactos()
            case '3':
                buscar_artefacto()
            case '4':
                print("Opciones de clasificación:")
                print("1. Mostrar todos clasificados")
                print("2. Filtrar por rareza específica")
                sub_opcion = input("Seleccione: ")
                if sub_opcion == "1":
                    clasificar_artefactos(mostrar_estadisticas=True)
                elif sub_opcion == "2":
                    rareza = input("Ingrese rareza (Bajo/Medio/Alto/Prohibido): ")
                    clasificar_artefactos(rareza=rareza)
                else:
                    clasificar_artefactos()
            case '5':
                mostrar_estadisticas_artefactos()
            case '6':
                eliminar_artefacto()
            case '7':
                print("Volviendo al menú principal...")
                break
            case _:
                print("Opción no válida")
