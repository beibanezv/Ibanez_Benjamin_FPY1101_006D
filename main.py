import funciones
import time

print("--- Bienvenido al programa de gestión de inventario de la tienda 'SCOOBY DOO' ---")
menu_salir = input("Ingrese 'm' si desea abrir el menú de opciones o ingrese 'x' para salir del programa.")

while menu_salir not in ["m","x"]:
    print("No se ingresó una opción válida.")
    menu_salir = input("Ingrese 'm' si desea abrir el menú de opciones o ingrese 'x' para salir del programa.")

if menu_salir == "m":
    flag = False
    while True:
        funciones.menu()

elif menu_salir == "x":
    print("************************")
    print("Saliendo del programa...")
    print("************************")
    time.sleep(2)
    flag = False

