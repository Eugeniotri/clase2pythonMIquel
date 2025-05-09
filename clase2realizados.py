"""Crear una aplicación en Python que permita gestionar un inventario de productos. El programa debe
 ofrecer un menú interactivo para que el usuario pueda:
 1.Añadir productos (con nombre, cantidad y precio).
 2.Mostrar todos los productos registrados.
 3.Buscar un producto por su nombre.
 4.Calcular el valor total del inventario (suma de cantidad por precio de cada producto).
 5.Salir."""

inventario=[]
def agregar_producto():
    nombre = input("Introduce el nombre del producto:")

    try:
        precio = float(input("Introduce el precio del producto: "))
        cantidad=float(input("Introduce la cantidad:"))
        if precio<=0 or cantidad<=0:
         print("precio y cantidad deben ser positivos")
    except ValueError:
        print("Debes solo introducir numeros positivos")


    producto = {
        'nombre':nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    inventario.append(producto)
    print(f"El producto {producto['nombre']} ha sido añadido")

def mostrar_inventario():
    if not inventario:
        print("inventario vacio")

        for producto in inventario:
            print(f"producto {producto['nombre'] }añadido")

def buscar_producto():
    nombre=input("Introduce el nombre a buscar:")
    encontrados = []
    for producto in inventario:
        if nombre==producto['nombre']:
            print(f"El producto {producto['nombre']} está en el inventario")
            encontrados.append(nombre)
            print(f"productos encontrados totales {encontrados}")
        else:
            print("no se encontró ningún producto con ese nombre")


def calcular_valortotal():
    totalproducto=0
    for p in inventario:
        totalproducto+=p['precio']*p['cantidad']#acumulador
        print(totalproducto)

def mostrar_menu():
    print("1-Agregar mas producto")
    print("2_Mostrar inventario")
    print("3-Buscar producto")
    print("4-Calcular valor inventario")
    print("5_-Salir")


if __name__ =="__main__" :
    while True:
        opcion=input("Elige una opcion (1-5):")
        if opcion == '1':
            agregar_producto()
        elif opcion=='2':
            mostrar_inventario()
        elif opcion =='3':
            buscar_producto()
        elif opcion=='4':
            calcular_valortotal()
        elif opcion =='5':
            print("saliendo del programa")
        else:
            print("opcion no valida")




