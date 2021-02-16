from array import *

# []
casillero_vacio = 0
pieza_peon = 1
pieza_torre = 2
pieza_caballo = 3
pieza_alfil = 4
pieza_dama = 5
pieza_rey = 6
pieza_peon_negro = -1
pieza_torre_negro = -2
pieza_caballo_negro = -3
pieza_alfil_negro = -4
pieza_dama_negro = -5
mueve_dos_posiciones = 16
mueve_una_posiciones = 8
def vabs(valor):
    if (valor < 0 ):
        valor = valor*-1
    return valor

def hacerMovimietoPeon(origen, destino, tablero):
    movValido = False

    if(vabs(tablero[origen])== vabs(pieza_peon)):
        if(tablero[destino] == casillero_vacio): #mover
            if(vabs(destino-origen)==mueve_dos_posiciones):
                if(origen < 16 and origen > 7 or origen < 56 and origen >48):
                    if(tablero[origen + 8] == casillero_vacio):#nadie en el camino
                        tablero[destino] = tablero[origen]
                        tablero[origen] = casillero_vacio
                        movValido = True
                    else:
                        print("movimiento no valido")
                else:
                    print("movimiento no valido")
            else:#mueve desde 1era fila
                if(vabs(vabs(destino)-vabs(origen))==mueve_una_posiciones):
                    tablero[destino] = tablero[origen]
                    tablero[origen] = casillero_vacio
                    movValido = True
                else:
                    print("movimiento no valido")
        else:#comer
            print("nada")
    else:
        print("movimiento no valido")
    return movValido


tablero = array ('i',[
 0,0,0,0,0,0,0,0,  #fila  0
 -1,-1,-1,-1,-1,-1,-1,-1,
 0,0,0,0,0,0,0,0,
 0,0,0,0,0,0,0,0,
 0,0,0,0,0,0,0,0,
 0,0,0,0,0,0,0,0,
 1,1,1,1,1,1,1,1,
 0,0,0,0,0,0,0,0  #fila 7
 ])
#mover un peon un paso adelante
resultado = hacerMovimietoPeon(8, 16, tablero)
resultado = hacerMovimietoPeon(9, 25, tablero)
resultado = hacerMovimietoPeon(10, 0, tablero)
resultado = hacerMovimietoPeon(11, 35, tablero)
# Presentar Tablero
for pos in range(0, 63, 8):
    for posic in range(pos, pos+8):
        print('{:>2}'.format(tablero[posic]), end='')
    print("")