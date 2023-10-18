
# CODE:13
# IMPORTANTE: NO borrar los comentarios

puntaje = int(input("Ingrese un valor entre 0 y 100:\n"))

# Alumno:
# Deberá crear una serie de considiconales
# con if y elif de forma tal de cargar en
# la variable nota la nota del alumno según
# las siguientes condiciones:

nota = ""

# Si el puntaje es mayor igual a 90 --> nota = "A"
# Sino, si el puntaje es mayor igual a 80 --> nota = "B"
# Sino, si el puntaje es mayor igual a 70 --> nota = "C"
# Sino, si el puntaje es mayor igual a 60 --> nota = "D"
# Sino, si el puntaje es menor a  60      --> nota = "F"

if puntaje > 90 or puntaje == 90:
    nota = 'A'
    print(f'El puntaje obtenido de {puntaje} corresponde a la nota {nota}, SOBRESALIENTE')
elif puntaje > 80 and puntaje < 90 or puntaje == 80:
    nota = 'B'
    print(f'El puntaje obtenido de {puntaje} corresponde a la nota {nota}, APROBADO DESTACABLE')
elif puntaje > 70 and puntaje < 80 or puntaje == 70:
    nota = 'C'
    print(f'El puntaje obtenido de {puntaje} corresponde a la nota {nota}, APROBADO DESTACABLE')
elif puntaje > 60 and puntaje < 70 or puntaje == 60:
    nota = 'D'
    print(f'El puntaje obtenido de {puntaje} corresponde a la nota {nota}, APROBADO' )
elif puntaje < 60 and puntaje > 0 or puntaje == 0: 
    nota = 'F'
    print(f'El puntaje obtenido de {puntaje} corresponde a al anota {nota}, DESAPROBADO')
else:
    print('Algo anda mal...')

# Recuerde utilizar un solo bloque condicional
# armado de if y múltiples elif
# Puede consultar el ejemplo de clase 2 como referencia

print(f'{nota}')

# Imprimir en pantalla la variable nota
