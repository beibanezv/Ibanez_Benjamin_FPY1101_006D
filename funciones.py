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
def menu(opcion):
    opcion("1")==(ver_productos)
    print("Usted eligio la opcion de ver producto")

    opcion("2")==(agregar_producto)
    print("Usted eligio la opcion agregar producto")
    
    opcion("3")==(modificar_producto)
    print("Usted eligio la opcion de modificar producto")

    opcion("4")==(eliminar_producto)
    print("Usted eligio la opcion de elimar producto")

    opcion("5")==(guardar_archivo)
    print("Usted eligio la opcion de guardar producto")
    
    opcion==(Salir_del_programa)
    print("usted eligio la opcion salir")

    