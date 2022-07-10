# Bucles [Python]
# Ejercicios de profundización

# Autor:  Juan Emimilio Dalcol
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio



while True:
    print ("\n \n")
    print ('''A continuacion ingrese el simbolo de la operacion que desea realizar: \n
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**) \n''')
    
    print ("En caso que desee finalizar con el programa introduzca la palabra 'FIN' en el mismo:")
    simbolo = str(input("Ingrese el simbolo:\n"))
    if simbolo == "FIN":
        break
    numero1 = int(input("Ingrese su numero:\n "))
    numero2 = int(input("Ingrese su numero:\n "))

    if simbolo == "+" :
        suma = numero1 + numero2
        print(f"El resultado es {suma}")
        
    elif simbolo == "-":
        resta = numero1 - numero2
        print(f"El resultado es {resta}")
    elif simbolo == "*":
       multiplicacion = numero1 * numero2
       print(f"El resultado es {multiplicacion}")
    elif simbolo == "/":
        division = numero1 / numero2
        print(f"El resultado es {division}")
    elif simbolo == "**":
        exponente = numero1 ** numero2
        print(f"El resultado es {exponente}")
    else:
        print("El simbolo ingresado es incorrecto")
print("Programada finalizado")