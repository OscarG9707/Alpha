# Menu del sistema
from termcolor import colored as colorear

def mostrar():
    print()
    print(colorear('********************************************************************', 'green', attrs= ['reverse','blink']))
    print(colorear('* ', 'green', attrs= ['reverse','blink']), end ='')
    print(colorear('1. Leer info tripulantes                                        ', 'blue'), end='')
    print(colorear(' *', 'green', attrs= ['reverse','blink']))
    print(colorear('* 2. Imprimir info tripulantes                                     *','yellow'))
    print(colorear('* 3. Calificaciones retos                                          *' , 'blue'))
    print('* 4. Definitiva ciclo I                                            *')
    print('* 5. Cargar información de json                                    *')
    print('* 6. Grabar información de json                                    *')
    print('*                                                                  *')
    print('* 0. Para salir                                                    *')
    print(colorear('********************************************************************', 'green', attrs= ['reverse','blink']))
    opcion = input('--> ')
    print()
    return opcion


def enterContinuar():
    print()
    input('[Enter] para continuar ')
    return True


def continuarSistema(opcionExterna):
    if(opcionExterna != '0'):
        return True
    else:
        print('Bye Bye')
        return False


def opcionesCorrectas(opcionExterna):
    listaCorrectas = ['1', '2', '3', '4', '5', '6', '0']
    if(opcionExterna not in listaCorrectas):
        print('Opción incorrecta, por favor elige una opción correcta')
        return False
    else:
        return True
