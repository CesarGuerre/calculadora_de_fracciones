# Este archivo sera diseñado y editado para crear una calculadora de fracciones que sea 
# capas de comparar y realizar diversas operaciones entre fracciones


# La variable "indice" sera la responsable de señalar en que indice de las listas te encuentras
indice = 0
iteracion = 0
numerador = []
denominador = []
# La variable "indicacion_de_seguir" sera la responsable de indcar si el bucle sigue o se detiene 
indicacion_de_seguir = 'si'  

# Bucle de entrada de datos
while indicacion_de_seguir != 'no':
    numerador.append(int(input("ingrese el numerador:")))
    denominador.append(int(input("ingrese el denominador:")))
    print("¿Quieres añadir una nueva fracción?:\n")
    indicacion_de_seguir = input("Escriba 'yes' para añadir o 'no' para finalizar: ")
    indice = indice + 1 # incremento del indice en 1

# Bucle de salida de datos
while iteracion < len(numerador):
    print(f'Fracción numero #{iteracion + 1}\n{numerador[iteracion]}\n___\n{denominador[iteracion]}')
    iteracion = iteracion + 1