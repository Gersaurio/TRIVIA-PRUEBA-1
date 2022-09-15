# Para la implementación de puntajes, crear una nueva variable llamada "puntaje" con valor inicial 0
puntaje = 0
MAGENTA = '\033[35m'
CYAN = '\033[36m'
YELLOW = '\033[33m'
GREEN = '\033[32m'
RED = '\033[31m'
RESET = '\033[39m'
import time
# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print (MAGENTA+"Bienvenido a mi trivia sobre historia universal."+RESET)
print (GREEN+"Por ahora tienes",puntaje,"puntos"+RESET)
nombre = input(YELLOW+"Escribe tu nombre: "+RESET)
print ("\nBien",nombre,",pondré a prueba tus conocimientos.")
for numero_carga in range(1,6,1):
  print (numero_carga)
  time.sleep(1)
# Instrucciones sobre cómo jugar:
print (MAGENTA+"\nResponde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar su respuesta:\n"+RESET)
time.sleep(5)
# El \n es para dar un "salto de línea"

# Pregunta 1
print (CYAN+"1) Considerado el padre de la historia:"+RESET)
print ("   a) Estrabón")
print ("   b) Arquímedes")
print ("   c) Galeno")
print ("   d) Heródoto")
#El jugador tendrá un tiempo de 3 segundos para leer la pregunta y alternativa
time.sleep(3)
# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input("\nTu respuesta: ")
while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
if respuesta_1=="d":
  puntaje += 10
  print (GREEN+"Correcto", nombre,"!"+RESET)
else:
  puntaje -= 10
  print (RED+"Incorrecto", nombre,"!"+RESET)
time.sleep(2)

#Pregunta 2
print (CYAN+"\n2) Batalla naval en la que se enfrentaron las fuerzas griegas y el imperio persa de Jerjes I:"+RESET)
print ("    a) Salamina")
print ("    b) Gaugamela")
print ("    c) Termópilas")
print ("    d) Qadesh")
time.sleep(3)
# Almacenamos la respuesta del usuario en la variable "respuesta_2"
respuesta_2 = input("\nTu respuesta: ")
while respuesta_2 not in ("a","b","c","d","t"):
  respuesta_2 = input("Debes responder a,b,c o d. Ingrese nuevamente tu respuesta: ")
#Verificar la respuesta para mandar un mensaje de acierto o error 
if respuesta_2 == "b":
  puntaje -= 10
  print (RED+"Incorrecto",nombre,".Gaugamela fue una batalla entre macedonios y persas"+RESET)
elif respuesta_2 == "c":
  puntaje -= 10
  print (RED+"Incorrecto",nombre,".Termópilas fue una batalla entre espartanos y persas"+RESET)
elif respuesta_2 == "d":
  puntaje -= 10
  print (RED+"Incorreto",nombre,".Qadesh fue la batalla entre Hititas y Egipcios"+RESET)
elif respuesta_2 == "t":
  puntaje += 20
  print (YELLOW+"Colocaste la inicial del comandante griego de la guerra, obtuviste puntaje adicional."+RESET)
else:
  puntaje += 10
  print (GREEN+"Correcto",nombre,"!"+RESET)
time.sleep(2)

#Pregunta 3
print (CYAN+"\n3) La guerra de los 100 años fue un conflicto armado entre Inglaterra y Francia que tuvo una duración de:"+RESET)
print ("    a) 90 años")
print ("    b) 100 años")
print ("    c) 116 años")
print ("    d) 99 años")
time.sleep(6)
respuesta_3 = input("\nTu respuesta: ")
while respuesta_3 not in ("a","b","c","d"):
  respuesta_3 = input("Debes responder a,b,c o d. Ingrese nuevamente tu respuesta: ")
if respuesta_3 == "a":
  puntaje -= 10
  print (RED+"Incorrecto",nombre,",90 años no fue la duración."+RESET)
elif respuesta_3 == "b":
  puntaje -= 10
  print (RED+"Incorrecto",nombre,".Parecía una respuesta obvia, pero tan fácil, no lo es."+RESET)
elif respuesta_3 == "d":
  puntaje -= 10
  print (RED+"Incorrecto",nombre,".Mentiría si dijera que casi aciertas."+RESET)
else:
  puntaje += 10
  print (GREEN+"Correcto",nombre,"!"+RESET)
time.sleep(1)
print (MAGENTA+"\nGracias",nombre,"por jugar mi trivia, alcanzaste",puntaje, "puntos"+RESET)
