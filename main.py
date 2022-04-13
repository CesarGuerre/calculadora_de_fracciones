# Este archivo sera diseñado y editado para crear una calculadora de fracciones que sea 
# capas de comparar y realizar diversas operaciones entre fracciones

import operaciones

def main():
    # Entradas para el programa
    numerador1 = int(input('Ingrese el numerador: '))
    denominador1 = int(input('Ingrese el denominador: '))
    print('Puedes suma" + ", Restar" - ", Multipicar" * " y Dividir" / ": ')
    operacion = input('Indique que operación deseas realizar')
    numerador2 = int(input('Ingrese el numerador: '))
    denominador2 = int(input('Ingrese el denominador: '))
    
    ##########Esta condiciones se pueden simplificar concirtiendo las sentencias en una función
    if operacion == '+':           # Condición para ordenar las sumas
        resultado = operaciones.suma(numerador1, numerador2, denominador1, denominador2) #funcion que realiza las sumas
        print(f'{numerador1}  {operacion}  {numerador2}  =  {resultado[0]}')
        print('_________________')
        print(f'{denominador1}  {operacion}  {denominador2}  =  {resultado[1]}')
    
    elif operacion == '-':           # Condición para ordenar las restas
        resultado = operaciones.resta(numerador1, numerador2, denominador1, denominador2) #funcion que realiza las resta
        print(f'{numerador1}  {operacion}  {numerador2}  =  {resultado[0]}')
        print('_________________')
        print(f'{denominador1}  {operacion}  {denominador2}  =  {resultado[1]}')

    elif operacion == '*':           # Condición para ordenar las multiplicaciones
        resultado = operaciones.multiplicacion(numerador1, numerador2, denominador1, denominador2) #funcion que realiza las divisiones
        print(f'{numerador1}  {operacion}  {numerador2}  =  {resultado[0]}')
        print('_________________')
        print(f'{denominador1}  {operacion}  {denominador2}  =  {resultado[1]}')

    elif operacion == '/':           # Condición para ordenar las divisiones
        resultado = operaciones.division(numerador1, numerador2, denominador1, denominador2) #funcion que realiza las multiplicaciones
        print(f'{numerador1}  {operacion}  {numerador2}  =  {resultado[0]}')
        print('_________________')
        print(f'{denominador1}  {operacion}  {denominador2}  =  {resultado[1]}')
    
    else:
        print('Operación no identificada')

if __name__ == '__main__':
    main()