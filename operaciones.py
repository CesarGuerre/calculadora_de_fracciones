def suma(num1,num2,den1,den2):                  #Funcion para sumar las fraciones
    if den1 == den2:                            #Condición para sumar fracciones de igual denominador
        result_numerador = num1 + num2
        result_denominador = den1
        lista = [result_numerador, result_denominador]
    else:                                       #Sumar fracciones de distinto denominador
        result_numerador = num1 * den2 + den1 * num2
        result_denominador = den1 * den2
        lista = [result_numerador, result_denominador]
    return lista

def resta(num1,num2,den1,den2):                  #Funcion para restar las fraciones
    if den1 == den2:                            #Condición para restar fracciones de igual denominador
        result_numerador = num1 - num2
        result_denominador = den1
        lista = [result_numerador, result_denominador]
    else:                                       #restar fracciones de distinto denominador
        result_numerador = num1 * den2 - den1 * num2
        result_denominador = den1 * den2
        lista = [result_numerador, result_denominador]
    return lista

def multiplicacion(num1,num2,den1,den2):                  #Funcion para multiplicar las fraciones
    result_numerador = num1 * num2
    result_denominador = den1 * den2
    lista = [result_numerador, result_denominador]
    return lista

def division(num1,num2,den1,den2):                  #Funcion para dividir las fraciones
    result_numerador = num1 * den2
    result_denominador = num2 * den1
    lista = [result_numerador, result_denominador]
    return lista
