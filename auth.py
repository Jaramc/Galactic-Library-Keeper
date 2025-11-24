import storage

#Funcion reutilizable
def login(intentos = 3):
    leer_credenciales = "admin_access.csv"
    
    if not storage.existe_archivo(leer_credenciales):
        print("Credenciales incorrectas")
        return False
    elif intentos == 0:
        print("Acceso denegado")
        return False
    print(f"Numero de intentos disponibles:{intentos}")
        
    username = input("Ingrese su usuario: ")
    password = input("Ingrese la contraseña: ")
    
    credenciales = storage.leer_csv(leer_credenciales)
    
    for row in credenciales:
        if row ["username"] == username and row ["password"] == password and row ["role"] == "SUPERADMIN":
            print("Bienvenido administrador")
            return True
    print("Credenciales incorrectas") 
    return login (intentos-1)
    