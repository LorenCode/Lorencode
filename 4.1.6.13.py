#Juego del tres en raya
# Edición prueba
# prueba 2
# prueba 3
# prueba 4
# prueba 5
# prueba 6

from random import randrange

filas = [["1","2","3"],["4","X","6"],["7","8","9"]]
pos = {"1":(0,0),"2":(0,1),"3":(0,2),"4":(1,0),"5":(1,1),"6":(1,2),"7":(2,0),"8":(2,1),"9":(2,2)}
pos_vacia = []

def DisplayBoard():
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#
#

    for a in range(13):
        if a == 0:
            print("+","+","+","+",sep="-"*7)
        elif a == 2:
            print("|",filas[0][0],"|",filas[0][1],"|",filas[0][2],"|",sep=" "*3)
        elif a == 4:
            print("+-------"*3+"+")
        elif a == 6:
            print("|",filas[1][0],"|",filas[1][1],"|",filas[1][2],"|",sep=" "*3)
        elif a == 8:
            print("+-------"*3+"+")
        elif a == 10:
            print("|",filas[2][0],"|",filas[2][1],"|",filas[2][2],"|",sep=" "*3)
        elif a == 12:
            print("+-------"*3+"+")
        else:
            print("|"+" "*7+"|"+" "*7+"|"+" "*7+"|")
        
def EnterMove():
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#
    moJugador = input("Elige un movimiento indicando una posición: ")
    if moJugador in pos:
        a, b = pos[moJugador]

    while True:
        if moJugador in filas[0] or moJugador in filas[1] or moJugador in filas[2]:       
            filas[a][b]= "O"
            break
        else:   
            print("No es posible")
            moJugador = input("Elige un movimiento indicando una posición: ")
            if moJugador in pos:
                a, b = pos[moJugador]

def MakeListOfFreeFields():

# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna

    del pos_vacia[:]
    for a in pos:
        f, c = pos[a]
        if filas[f][c] == "X" or filas[f][c] == "O" :
            continue
        else:
            pos_vacia.append((f,c))
        

def VictoryFor():
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#

    
    if filas[0][0] == "O" and filas[0][1]== "O" and filas[0][2]== "O":
        print("Has ganado")
        return "1"

    elif filas[0][0] == "O" and filas[1][0]== "O" and filas[2][0]== "O":
        print("Has ganado")
        return "1"
        
    elif filas[0][2] == "O" and filas[1][2]== "O" and filas[2][2]== "O":
        print("Has ganado")
        return "1"
        
    elif filas[2][0] == "O" and filas[2][1]== "O" and filas[2][2]== "O":
        print("Has ganado")
        return "1"
        

    elif filas[0][0] == "X" and filas[0][1]== "X" and filas[0][2]== "X":
        print("Has perdido")
        return "1"
        
    elif filas[0][0] == "X" and filas[1][0]== "X" and filas[2][0]== "X":
        print("Has perdido")
        return "1"
        
    elif filas[0][2] == "X" and filas[1][2]== "X" and filas[2][2]== "X":
        print("Has perdido")
        return "1"
        
    elif filas[2][0] == "X" and filas[2][1]== "X" and filas[2][2]== "X":
        print("Has perdido")
        return "1"
        
    elif filas[0][0] == "X" and filas[1][1]== "X" and filas[2][2]== "X":
        print("Has perdido")
        return "1"
        
    elif filas[2][0] == "X" and filas[1][1]== "X" and filas[0][2]== "X":
        print("Has perdido")
        return "1"
        
    elif filas[0][1] == "X" and filas[1][1]== "X" and filas[2][1]== "X":
        print("Has perdido")
        return "1"
        
    elif filas[1][0] == "X" and filas[1][1]== "X" and filas[1][2]== "X":
        print("Has perdido")
        return "1"

       
    elif len(pos_vacia) == 0 :
        print("Empate") 
        return "1"
        
def DrawMove():
###
### la función dibuja el movimiento de la maquina y actualiza el tablero
###
    
    posicion_random = (randrange(len(pos_vacia)))
    a, b = pos_vacia[posicion_random]
    posicion = 0

    for c in range(1,len(pos)+1):
        if pos.get(str(c)) == (a,b):
            posicion = str(c)

    if posicion in filas[0] or posicion in filas[1] or posicion in filas[2]:       
        filas[a][b]= "X"

    else:   
        print("No es posible")


DisplayBoard()
while True:
    
   
    EnterMove()
    MakeListOfFreeFields()

    DisplayBoard()
    if VictoryFor() == "1":
        break
     
    DrawMove()
    MakeListOfFreeFields()

    DisplayBoard()
    if VictoryFor() == "1":
        break

