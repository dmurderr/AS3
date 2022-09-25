from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

import parametros as p


# Recuerda que estamos usando QT Designer :eyes:
# CARGAR ARCHIVO AQUÍ
window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_JUEGO)
# COMPLETAR:
class VentanaJuego(window_name, base_class):  # pylint: disable=E0602

    senal_iniciar_juego = pyqtSignal()
    senal_tecla = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        # COMPLETAR

    def mostrar_ventana(self, usuario):
        self.show()
        self.casilla_nombre.setText(usuario) 
        self.casilla_puntaje.setText(str(p.PUNTAJE_INICIAL))
        self.casilla_tiempo.setText(str(p.TIEMPO_JUEGO))
        self.senal_iniciar_juego.emit()
        pass

    def keyPressEvent(self, event):
        # COMPLETAR
        
        key = event.key()
          #w = 87 a = 65 s = 86 d = 68 
        print(key)
        if key == 87:
            self.senal_tecla.emit(p.TECLA_ARRIBA)
        elif key == 65:
            self.senal_tecla.emit(p.TECLA_IZQUIERDA)
        elif key == 83:
            self.senal_tecla.emit(p.TECLA_ABAJO)
        elif key == 68:
            self.senal_tecla.emit(p.TECLA_DERECHA)
        pass

    def init_gui(self):
        self.setWindowTitle("Ventana de Juego")
        self.boton_salir.clicked.connect(self.salir)

    def actualizar_topos(self, topos):
        for topo in topos:
            topo.topo_label.setParent(self)
            topo.topo_label.setVisible(True)
            topo.topo_label.move(topo.pos_topo.x(), topo.pos_topo.y())

    def mover_martillo(self, martillo):
        martillo.martillo_label.setParent(self)
        martillo.martillo_label.setVisible(True)
        martillo.martillo_label.move(martillo.pos_martillo.x(),
                                     martillo.pos_martillo.y())

    def actualizar_datos(self, tiempo, puntaje):
        self.casilla_tiempo.setText(tiempo)
        self.casilla_tiempo.repaint()

        self.casilla_puntaje.setText(puntaje)
        self.casilla_puntaje.repaint()

    def salir(self):
        self.close()
