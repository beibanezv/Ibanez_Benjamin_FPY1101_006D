import time

inventario = [
    {
    'CODIGO':'CODIGO',
    'NOMBRE':'NOMBRE',
    'CANTIDAD':'CANTIDAD',
    'PRECIO':'PRECIO'
    }
]

def agregar_producto():
    codigo = input("Ingrese el código del producto a ingresar en el inventario: ")
    nombre = input("Ingrese el nombre del producto a ingresar: ").capitalize()
    cantidad = int(input("Ingrese el stock del producto a ingresar: "))
    precio = int(input("Ingrese el precio del producto a ingresar: "))

    producto = {
        'CODIGO': codigo,
        'NOMBRE': nombre,
        'CANTIDAD': cantidad,
        'PRECIO': precio
    }

    inventario.append(producto)
    print(f"Se han agregado {cantidad} {nombre} ({codigo}) con un valor unitario de {precio} exitosamente. ")

def ver_productos():
    print("** Usted eligio opción ver lista de productos **")
    for producto in inventario:
        print(f"{producto['CODIGO']} - {producto['NOMBRE']} - {producto['CANTIDAD']} - {producto['PRECIO']}\n")

def modificar_producto():
    producto_modificacion = input("Ingrese el producto a modificar  del inventario")
    dato = input("Ingrese el valor que desea cambiar")


def eliminar_producto():
    producto_remover = input("Ingrese el nombre del producto que quiere quitar del inventario: ").capitalize()
    for producto in inventario:
        if producto_remover == producto['NOMBRE']:
            inventario.remove(producto)
            print(f"Producto {producto} eliminado del inventario correctamente.")

def guardar_archivo():
    with open('inventario.txt', 'w', encoding='utf-8') as f:
        for producto in inventario:
            f.write(f"{producto['CODIGO']} - {producto['NOMBRE']} - {producto['CANTIDAD']} - {producto['PRECIO']}\n")

def menu():
    print("1. Agregar producto\n2. Ver poducto\n3. modificar producto\n4. Eliminar producto\n5. Guardar inventario\n6.Salir del programa.")
    opcion=input("ingrese la opcion que sea elegir")
    if opcion == "1":
        agregar_producto()
    
    elif opcion == "2":
        ver_productos()

    elif opcion == "3":
        modificar_producto()

    elif opcion == "4":
        eliminar_producto()

    elif opcion == "5":
        guardar_archivo()

    elif opcion == "6":
        print("************************")
        print("Saliendo del programa...")
        print("************************")
        time.sleep(2)
        flag = False

    else:
        print("Usted eligió una opción que no esta en el menú, porfavor ingrese una opcion que este en el menu del 1 al 6 ")