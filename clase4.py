"""""1. Input, Output y Variables
 Enunciado:
 1.Pide al usuario que introduzca su nombre y su altura en centímetros.
 2.Imprime un mensaje en el siguiente formato:
 "Hola [nombre], mides [altura] cm"
 3.Convierte la altura a metros (1 metro = 100 cm) y vuelve a imprimir un mensaje en el
siguiente formato:
 "Hola [nombre], mides [altura_en_metros] metros"
 2. Programa de Ejemplo: Calculadora
 Enunciado:
 1.Crea un programa que pida al usuario dos números enteros.
 2.Muestra la multiplicación y la división entre ellos.
 3.Si el divisor (segundo número) es 0, muestra un mensaje que indique que la división no
es posible.
 3. Condicionales (if, elif, else)
 Enunciado:
 1.Pide al usuario que introduzca una nota en una escala de 0 a 10.
 2.Según la nota, muestra:
 Menor que 5: "Suspendido"
 Entre 5 y 6 (inclusive 5 y menor o igual a 6): "Aprobado"
 Entre 7 y 8: "Notable"
 Mayor que 8 hasta 10: "Sobresaliente"
 3.Si la nota es menor que 0 o mayor que 10, muestra un mensaje indicando que la nota
está fuera de rango.
 4. Bucles For
 Enunciado:
 1.Crea una lista de 5 números, por ejemplo: [5, 2, 7, 1, 9].
 2.Utilizando un bucle for, recorre la lista y calcula la suma total de los elementos.
 3.Imprime el resultado de la suma.
 5. Bucles While
 Enunciado:
 1.Utiliza un bucle while para pedir al usuario que introduzca números.
 2.El programa deberá seguir pidiendo números mientras el número ingresado sea mayor o
 igual a cero.
 3.Cuando el usuario introduzca un número negativo, el programa finaliza y muestra todos
los números introducidos (puedes mostrarlos en una lista).
 6. Funciones, Variables Locales y Globales
 Enunciado:
 1.Define una función llamada cuadrado que reciba un número y retorne el cuadrado de
ese número. Utiliza una variable local en la función.
 2.Declara una variable global llamada mensaje_global y escribe otra función que la
modifique.
 3.Muestra por pantalla el resultado de la función cuadrado y el valor de la variable global
tras la modificación.
 7. Funciones Lambda
Enunciado:
 1.Define una función lambda que reciba un número y lo multiplique por 10.
 2.Aplica esa lambda a cada elemento de la lista [1, 2, 3, 4, 5] para generar una nueva lista.
 3.Imprime la nueva lista resultante.
 8. Recursividad (Factorial)
 Enunciado:
 1.Define una función recursiva factorial(n) que calcule y retorne el factorial del número n.
 2.Recuerda que el factorial de 0 es 1 y para n > 0, se cumple que:
 factorial(n) = n * factorial(n - 1)
 3.Demuestra el funcionamiento de la función llamándola, por ejemplo, con n = 5.
 9. Manejo de Errores (try/except)
 Enunciado:
 1.Pide al usuario que introduzca un número entero.
 2.Divide 10 entre ese número.
 3.Utiliza bloques try/except para manejar:
 El error al convertir el dato a entero.
 El error de división por cero.
 4.Asegúrate de incluir un bloque finally que imprima un mensaje final, indicando que se
ha finalizado la operación."""

def ejercicio1():
    nombre = input("Dime tu nombre:")
    alturacm = float(input("Dime tu altura: "))
    print(f"Te llamas {nombre} y mides {alturacm} en metros")
    alturam=alturacm/10
    print(f"Hola {nombre} mides {alturam} metros")
def ejercicio2():
    try:
        num1=float(input("Dime el primer número"))
        num2=float(input("Dime el segundo número"))
        if num1<0 or num2<0:
            print("debes introducir números positivos")
        multiplicacion=num1*num2
        return multiplicacion
        division=num1/num2
        return division
    except ValueError:
        print("debes introducir solo numeros")
    except: ZeroDivisionError:
        print("No puedes dividir por 0")


