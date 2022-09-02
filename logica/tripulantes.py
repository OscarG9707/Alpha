# Logica de negocio para leer e imprimir información de tripulantes

import json
from ntpath import join


def leerInfo(diccionarioExterno):
    contador = len(diccionarioExterno)
    continuar = True
    while(continuar):
        print('Información del tripulante: ' + str(contador + 1))
        documento = input('Documento de tripulante ')

        if(documento == '0'):
            continuar = False
        else:
            nombre = input('Nombres del tripulante ')
            apellido = input('Apellidos del tripulante ')

            diccionarioExterno[documento] = [nombre, apellido]

            contador = contador + 1
            print()

    return diccionarioExterno


def imprimirInfo(vieneDeAfuera):
    acumulador = ''
    cantidad = len(vieneDeAfuera)
    if(cantidad == 0):
        acumulador = 'No hay tripulantes !!!'
    else:
        # for documento, datos in vieneDeAfuera.items():
        # for documento, datos in sorted(vieneDeAfuera.items()):
        for documento, datos in sorted(vieneDeAfuera.items(), reverse=True):
            acumulador = acumulador + 'Número de Documento: ' + documento + '-->'
            acumulador = acumulador + \
                '[' + datos[0] + ', ' + datos[1] + ']' + '\n'

            if(len(datos)==3):
                acumulador = acumulador + ' notas: '
                for miNota in datos[2]:
                    acumulador = acumulador + miNota + ' - '

                acumulador = acumulador+ '\n\n'


    return acumulador


def cargarDatosJson():
    nuevoDiccionario = {}
    with open("baseDatos/misDatos.json", encoding="UTF-8") as archivo:
        temporal = json.load(archivo)
        nuevoDiccionario = temporal["tripulantes"]

    return nuevoDiccionario


def grabarDatosJson(diccionarioExterno):
    with open("baseDatos/misDatos.json", "w", encoding="UTF-8") as archivo:
        temporal = {"tripulantes": {}}
        temporal['tripulantes'] = diccionarioExterno
        json.dump(temporal, archivo, ensure_ascii=False, indent=4)
    return True


def leerNotas(diccionarioExterno, canNotas):
    diccionarioExterno = ajustarElDiccionario(diccionarioExterno)

    for documento, datos in diccionarioExterno.items():
        arregloNotas = []
        print('Tripulante ' + documento + ', ' + datos[0] + ' ' + datos[1])
        for indice in range(0, canNotas):
            notica = input('Nota ' + str(indice + 1) + ' = ')
            arregloNotas.append(notica)

        print()
        diccionarioExterno[documento][2] = arregloNotas

    return diccionarioExterno


def ajustarElDiccionario(diccionarioPorAjustar):
    for documento, datos in diccionarioPorAjustar.items():
        filaAjustadita = [datos[0], datos[1], []]
        diccionarioPorAjustar[documento] = filaAjustadita
    return diccionarioPorAjustar
