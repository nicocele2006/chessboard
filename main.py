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
def valor_absoluto(valor):
    return valor*-1

def hacerMovimietoPeon(origen, destino, tablero):
    movValido = False

    if(tablero[origen] == valor_absoluto(pieza_peon)):
        if(tablero[destino] == casillero_vacio): #mover
            if(valor_absoluto(destino-origen)==mueve_dos_posiciones):
                if(origen < 16 and origen > 7 or origen < 56 and origen >48):
                    if(tablero[origen + 8] != casillero_vacio):
                        tablero[destino] = tablero[origen]
                        tablero[origen] = casillero_vacio
                        movValido = True
                    else:
                        print("movimiento no valido")
                else:
                    print("movimiento no valido")
            else:#mueve desde 1era fila
                if(valor_absoluto(valor_absoluto(destino)-valor_absoluto(origen))==mueve_una_posiciones):
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
#resultado = hacerMovimietoPeon(11, 19, tablero)
# Presentar Tablero
for pos in range(0, 63, 8):
    for posic in range(pos, pos+8):
        print('{:>2}'.format(tablero[posic]), end='')
    print("")