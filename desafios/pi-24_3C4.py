
# CODE:18
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Deberá solicitar tres números decimales por consola,
cada nuḿero de temperatura lo debe almacenar
en variables llamadas:
-> temperatura_1
-> temperatura_2
-> temperatura_3

Utilizando el operador suma o el operador incremento
deberá almacenar la suma de todas las temperaturas
ingresadas en una nueva variable llamada "temperatura_total"

Luego, mediante el uso de la variable "temperatura_total"
y teniendo en cuenta que se ingresaron tres temperaturas.
Deberá calcular el promedio de todas las temperaturas
y almacenar el resultado en una variable llamada
"temperatura_promedio"

- Al final imprimir en pantalla la variable 
  temperatura_promedio
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

temperatura_1 = float(input('Ingrese el primer dáto térmico: \n'))

temperatura_2 = float(input('Ingrese el segúndo dáto térmico: \n'))

temperatura_3 = float(input('Ingrese el tercer dáto térmico: \n'))

temperatura_total = temperatura_1 + temperatura_2 + temperatura_3

temperatura_promedio = temperatura_total / 3

print(f'La temperatura total asciende a: {temperatura_total}º Celcius')

print(f'Mientrastanto, la temperatura promedio corresponde a: {temperatura_promedio}º Celcius')