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
    print()

def eliminar_producto():
    producto_remover = input("Ingrese el nombre del producto que quiere quitar del inventario: ").capitalize()
    for producto in inventario:
        if producto_remover == producto['NOMBRE']:
            inventario.remove(producto)

def guardar_archivo():
    with open('inventario.txt', 'w', encoding='utf-8') as f:
        for producto in inventario:
            f.write(f"{producto['CODIGO']} - {producto['NOMBRE']} - {producto['CANTIDAD']} - {producto['PRECIO']}\n")

def menu():
    print()

def salir():
    print("Saliendo del programa...")
    time.sleep(2)