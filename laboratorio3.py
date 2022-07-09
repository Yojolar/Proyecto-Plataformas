#!/usr/bin/python
#
# Jonatán Gonzalez Salazar.
# B63098.
#
#
# Este programa calcula la serie de Fibonacci para un numero que debe ingresar obligatoriamente el usuario,
# en caso de no ingresarse el programa mostrara un mensaje de error y de la manera correcta que se debe correr el
# programa, a su vez si se ingresa un valor no numerico se mostrara otro mensaje de error como "valor incorrecto" que
# se debe ingresar un numero no una caracter distinto. Ademas, por medio de comandos de argparse se mostraran
# diferentes opciones para correr el programa. La opcion simple (sin argumentos opcionales) correra el programa y
# unicamente mostrara el resultado del calculo de la serie para el numero ingresado. Al correrse con el argumento
# opcional de "tiempo" se mostrara cuanto dura el programa al calcular la serie para el numero ingresado. Al correrse
# con el argumento opcional "completa" se mostrara la serie completa calculada hasta el numero ingresado.
#
#
# --------------- INICIO DEL CÓDIGO --------------------
import argparse
import time

# Primero se declara la variable que denotara el inicio del codigo y iniciara un contador de tiempo en segundos.
inicio = time.time()
# Se declara el ArgumentParser.
parser = argparse.ArgumentParser()

# Se declara los argumentos del argparse.
# Se declara el argumento posicional (obligatorio).
parser.add_argument(
    'posicion',
    type=int,
    help='Numero o posicion a la cual le desea calcular la secuencia de Fibonacci.'
)

# Se declara el primer argumento opcional.
parser.add_argument(
    '--tiempo',
    '-t',
    action='store_true',
    help='Imprime el tiempo transcurrido para finalizar el cálculo.'
)

# Se declara el segundo argumento opcional.
parser.add_argument(
    '--completa',
    '-c',
    action='store_true',
    help='Imprime la secuencia completa.'
)

# Se procede a obtengo los argumentos y los guardarlos en argumentos.
argumentos = parser.parse_args()


# Se procede a definir la funcion para la serie de Fibonacci.
def fibonacci(variable):
    # Condicion de salida para las 2 primeras posiciones de la serie.
    if variable == 0 or variable == 1:
        resultado = 1

    # Se hace uso de la recursividad. Se usa la misma funcion con el valor (variable -1).
    else:
        resultado = fibonacci(variable - 1) + \
                    fibonacci(variable - 2)

    # Se retorna la solucion encontrada.
    return resultado


while True:
    # Se definen las variables con las que se va a trabajar.
    # El numero ingresado como argumento de posicion se guarda en la variable numero.
    numero = argumentos.posicion

    # El calculo final del resultado de la serie se guarda en la variable solucion.
    solucion = fibonacci(numero)

    # Se define la logica segun lo que se escoja como segundo argumento opcional.
    if argumentos.completa:
        # Por medio de un ciclo se imprime la serie completa del calculo de Fibonacci.
        for j in range(numero+1):
            # Se imprime el resultado de la serie completa.
            print(
                'Fibonacci({})= {} '.format(
                    j,
                    fibonacci(j)
                )
            )

    # En caso que con el agumento opcional NO se escoja la serie comleta,
    # se imprimira solamente el resultado de la serie y el numero al que se le quizo calcular esta serie.
    else:
        # Se imprime solo el resultado de la serie para el numero del argumento posicional.
        print(
            'Solucion de la serie de Fibonacci para el numero {} es: {} '.format(
                numero,
                solucion
            )
        )

    # En caso que se selecionar el argumento opcional de tiempo,
    # se imprime el tiempo completo de duracion al correr el programa.
    if argumentos.tiempo:
        # Se define la variable que define la duracion final desde que se corrio el codigo.
        final = time.time()
        # Se imprime el delta de tiempo que define la duracion que se obtuvo desde que comenzo a correr el programa.
        print(
            'Tiempo total de ejecucion es de: {} segundos'.format(
                final-inicio
            )
        )

    # Con este break se termina y cierra el programa.
    break
