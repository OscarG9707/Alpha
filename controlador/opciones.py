# El controlador es el que conecta la logica del negocio con las vistas
from re import I
import logica.tripulantes as miTripu


def opcionLeerInfo(opcionExterna, vieneDeAfuera):
    if(opcionExterna == '1'):
        print('Leer info de  tripulantes')
        print()

        diccionarioActualizado = miTripu.leerInfo(vieneDeAfuera)
        return diccionarioActualizado
    else:
        return vieneDeAfuera


def opcionImprimirInfo(opcionExterna, vieneDeAfuera):
    if(opcionExterna == '2'):
        print('Infomación tripulantes')
        print()
        print(miTripu.imprimirInfo(vieneDeAfuera))

        return True
    else:
        return False


def opcionCargarInfo(opcionExterna, viendeDeAfuera):
    if(opcionExterna == '5'):
        print('Cargar información json')
        print()

        diccionarioActualizado = miTripu.cargarDatosJson()
        return diccionarioActualizado
    else:
        return viendeDeAfuera


def opcionGrabarInfor(opcionExterna, viendeDeAfuera):
    if(opcionExterna == '6'):
        print('Grabar informacion json')
        print()

        miTripu.grabarDatosJson(viendeDeAfuera)

        return viendeDeAfuera
    else: 
        return viendeDeAfuera


def opcionLeerNotas(opcionExterna, viendeDeAfuera, cantidadNotas):
    if(opcionExterna == '3'):
        print('Leer notas retos')
        print()

        basesita = miTripu.leerNotas(viendeDeAfuera, cantidadNotas)

        return basesita
    else: 
        return viendeDeAfuera