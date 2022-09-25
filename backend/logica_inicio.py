from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool, list)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, tupla_respuesta):
        errores = []
        
        if tupla_respuesta[0].isalnum() or len(tupla_respuesta[0]) <= p.MAX_CARACTERES:
            pass
        else:
            errores.append("Usuario")
        
        if tupla_respuesta[1] == p.PASSWORD:
            pass
        else:
            errores.append("Contraseña")
        
        if len(errores) == 0:
            self.senal_respuesta_validacion.emit(True,errores)
            self.senal_abrir_juego.emit(tupla_respuesta[0])
        else:
            self.senal_respuesta_validacion(False,errores)
            self.senal_abrir_juego.emit(tupla_respuesta[0])
