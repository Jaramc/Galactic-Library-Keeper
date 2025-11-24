import auth
#from artifacts.py import artifacts.py
#from storage.py import storage.py
#from utils.py import utils.py
import visitors

def menu_principal ():
    if auth.login():
        while True:
            print("Galactic Library Keeper\n1 Módulo de Visitantes Intergalácticos\n2. Módulo de Artefactos Recuperados\n3. Salir\n")
            seleccion = input("Selecione una opcion del 1-3")
    if not auth.login():
        print("Acceso denegado")
        
menu_principal()
    