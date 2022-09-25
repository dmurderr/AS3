import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout, QPushButton)
from PyQt5.QtGui import QPixmap

class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(tuple)

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        # Geometría
        self.setGeometry(600, 200, 500, 500)
        self.setWindowTitle('Ventana de Inicio')
        self.setStyleSheet("background-color: lightblue;")
        self.crear_elementos()

    def crear_elementos(self):
        # CCOMPLETAR frontend\assets\logo.png
        self.logo = QLabel(self)
        #self.logo.setGeometry(600,200,500,500)
        pixel = QPixmap("frontend/assets/logo.png")
        
        self.logo.setPixmap(pixel)
        self.logo.setScaledContents(True)
        contenedor = QVBoxLayout()     
        
        layout_nombre = QHBoxLayout()
        
        self.nombre = QLabel("Ingresa tu nombre de usuario:" ,self)
        self.input_nombre = QLineEdit("",self)

        layout_nombre.addWidget(self.nombre)
        layout_nombre.addWidget(self.input_nombre)
        layout_nombre.addStretch(20)
        layout_nombre.setContentsMargins(10, 10, 10, 10)
        self.password = QLabel("Ingresa el la contraseña:" ,self)
        self.input_password = QLineEdit("",self)
        self.input_password.setEchoMode(QLineEdit.Password)
        
        layout_password = QHBoxLayout() 
        
        layout_password.addWidget(self.password)
        layout_password.addWidget(self.input_password)
        layout_password.addStretch(20)
        layout_password.setContentsMargins(10, 10, 10, 10)

        contenedor.addStretch(0)
        contenedor.addItem(layout_nombre)
        contenedor.addItem(layout_password)

        self.boton = QPushButton("Entrar",self)
        self.boton.resize(self.boton.sizeHint())
        self.boton.clicked.connect(self.enviar_login)
        contenedor.addWidget(self.boton)
        self.setLayout(contenedor)
        pass

    def enviar_login(self):
        # COMPLETAR
        self.senal_enviar_login.emit((self.input_nombre.text(),self.input_password.text()))
        pass

    def recibir_validacion(self, valid, errores):
        
        if valid:
            self.hide()
        else:
            if errores in "Usuario":
                self.input_nombre.text("Usuario no encontrado")
            elif errores in "Contraseña":
                self.input_password.text("Contraseña incorrecta")
        pass


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaInicio()
    ventana.show()
    sys.exit(app.exec_())
