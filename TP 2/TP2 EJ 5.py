# Escribir un programa que indique si un número ingresado por teclado es positivo, igual a cero o negativo.

# Ingresar número por teclado
x = float(input("Ingrese un numero por teclado: "))

if (x>0):
    print(x, 'es positivo ')
elif (x<0):
    print(x, 'es negativo')
else: 
    print('es igual a cero')
    
    
 