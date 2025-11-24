import csv
import os.path

#Funcion reutilizable
def login(intentos = 3):
    leer_credenciales = "admin_access.csv"
    
    if not os.path.exists(leer_credenciales):
        print("Credenciales incorrectas")
        return False
    elif intentos == 0:
        print("Acceso denegado")
        return False
    print(f"Numero de intentos disponibles:{intentos}")
        
    username = input("Ingrese su usuario: ")
    password = input("Ingrese la contraseña: ")
    
    with open(leer_credenciales, "r") as file:
        leer = csv.DictReader(file)
        
        for row in leer:
            if row ["username"] == username and row ["password"] == password and row ["role"] == "SUPERADMIN":
                print("Bienvenido administrador")
                return True
    print("Credenciales incorrectas") 
    return login (intentos-1)
    
if __name__ == "__main__":
    login()