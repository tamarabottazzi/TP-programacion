"Calculadora de división"

# En primer lugar, ¿Qué sucede cuando queremos dividir por 0? 
# ¿Qué debería suceder? Incorpore esta funcionalidad al script.

#a = 10
a = float(input('a= ')) 

#b = 2
b = float(input('b= '))

if (b == 0):
    print('El divisor no puede ser cero')
    b= float(input(' Ingrese otro b= '))


div = round(a/b,4)


print(a, '/', b, '=', div)