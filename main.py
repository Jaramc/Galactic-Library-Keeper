import auth
#from artifacts.py import artifacts.py
#from storage.py import storage.py
#from utils.py import utils.py
import visitors

def menu_principal():
    print("GALACTIC LIBRARY KEEPER - MENU")
    print("1. Módulo de Visitantes Intergalácticos")
    print("2. Módulo de Artefactos Recuperados")
    print("3. Salir")

def main():
    if auth.login():
        while True:
            try:
                menu_principal()
                seleccion = int(input("Seleccione una opción del 1-3: "))
                if seleccion == 1:
                    visitors.menu_visitantes()
                elif seleccion == 2:
                    artifacts.menu_artifactos()
                elif seleccion == 3:
                    print("Saliendo del programa. ¡Hasta luego!")
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")
            except ValueError:
                print("Entrada no válida: por favor ingrese un número entre 1 y 3.")

main()
    