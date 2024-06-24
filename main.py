import funciones

print("--- Bienvenido al programa de gestión de inventario de la tienda 'SCCOOBY DOO' ---")
while True:
    menu_salir = input("Ingrese 'm' si desea abrir el menú de opciones o ingrese 'x' para salir del programa.")

    if menu_salir == "m":
        funciones.menu()

    elif menu_salir == "x":
        funciones.salir()
