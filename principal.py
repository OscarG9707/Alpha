import vistas.menu as miMenu
import controlador.opciones as miOpcion

continuar = True
miBaseDatos = {}
# miBaseDatos = dict ()

while(continuar):
    # El menu
    opcion = miMenu.mostrar()
    continuar = miMenu.continuarSistema(opcion)
    miMenu.opcionesCorrectas(opcion)
    
    # Los controladores
    miBaseDatos = miOpcion.opcionLeerInfo(opcion,miBaseDatos)
    miOpcion.opcionImprimirInfo(opcion, miBaseDatos)
    miBaseDatos = miOpcion.opcionLeerNotas(opcion, miBaseDatos, 3)
    miBaseDatos = miOpcion.opcionCargarInfo(opcion, miBaseDatos)
    miOpcion.opcionGrabarInfor(opcion, miBaseDatos)

    # La pausa 
    miMenu.enterContinuar()