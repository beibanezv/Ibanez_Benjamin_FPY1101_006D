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
    nombre = input("Ingrese el nombre del producto a ingresar: ")
    cantidad = input("Ingrese el stock del producto a ingresar: ")
    precio = int(input("Ingrese el precio del producto a ingresar: "))

    producto = {
        'CODIGO': codigo,
        'NOMBRE': nombre,
        'CANTIDAD': cantidad,
        'PRECIO': precio
    }

def ver_productos():
    print()
def modificar_producto():
    print()
def eliminar_producto():
    print()
def guardar_archivo():
    print()
def menu():
    print()