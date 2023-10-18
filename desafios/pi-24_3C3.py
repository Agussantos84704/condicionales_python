
# CODE:17
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Crear una variable llamada puntaje inicializada,
  en cero. Esta variable la deberá incrementar en 10
  por cada respuesta correcta.

- Deberá imprimir en consola una pregunta por vez,
  y con la función input en cada caso solicitar una respuesta
  por cada pregunta realizada.

- Utilizar condicionales para evaluar si la respuesta
  ingresada por el usuario coincide con la respuesta
  del programa (las variables).

- Cada respuesta ingresada por el usuario por consola
  la deberá pasar a minúsculas utilizando la función
  lower (cómo se vio los ejemplos de clase)
'''

print('Juego de trivia')
puntaje = 0

pregunta_1 = "¿Cuál es la capital de Argentina?"
respuesta_1 = "buenos aires"

pregunta_2 = "¿Cuál es la capital de Perú?"
respuesta_2 = "lima"

pregunta_3 = "¿Cuál es la capital de Uruguay?"
respuesta_3 = "montevideo"

pregunta_4 = "¿Cuál es la capital de Colombia?"
respuesta_4 = "bogota"

pregunta_5 = "¿Cuál es la capital de Venezuela?"
respuesta_5 = "caracas"

# Empezar aquí la resolución del ejercicio

print(f'Pregunta número 1: {pregunta_1}')

rta_1 = str(input())

if rta_1.lower() == respuesta_1:
    puntaje += 10
    print(f'CORRECTO! Continuemos...')
else:
    print(f'Incorrecto! La respuesta correcta es {respuesta_1}')

print(f'Pregunta número 2: {pregunta_2}')

rta_2 = str(input())

if rta_2.lower() == respuesta_2:
    puntaje += 10
    print(f'CORRECTO! Continuemos...')
else:
    print(f'Incorrecto! La respuesta correcta es {respuesta_2}')

print(f'Pregunta número 3: {pregunta_3}')

rta_3 = str(input())

if rta_3.lower() == respuesta_3:
    puntaje += 10
    print(f'CORRECTO! Continuemos...')
else:
    print(f'Incorrecto! La respuesta correcta es {respuesta_3}')

print(f'Pregunta número 4: {pregunta_4}')

rta_4 = str(input())

if rta_4.lower() == respuesta_4:
    puntaje += 10
    print(f'CORRECTO! Continuemos...')
else:
    print(f'Incorrecto! La respuesta correcta es {respuesta_4}')

print(f'Pregunta número 5: {pregunta_5}')

rta_5 = str(input())

if rta_5.lower() == respuesta_5:
    puntaje += 10
    print(f'CORRECTO! Continuemos...')
else:
    print(f'Incorrecto! La respuesta correcta es {respuesta_5}')

print(f'Excelente, sus resultados han sido: {puntaje} puntos; Gracias por participar!')