import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout


class LoginRegister(QWidget):
    def __init__(self):
        super().__init__()

        # Configuracion de la ventana
        self.setWindowTitle('Login')

        # Crear un Layout de cuadricula
        layout = QVBoxLayout()

        # Etiquetas y cajas de texto
        tags = ["Username", "Confirm Password", "Password", "Surname", "Forename", "Secret Answer"]
        self.entradas = []



        boton_registrarse = QPushButton('Registrarse')

        layout.addWidget(boton_registrarse, len(tags), 0)

        boton_registrarse.clicked.connect(self.nada)
        self.setLayout(layout)

    def nada(self):
        print("hechp")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginRegister()
    window.show()
    sys.exit(app.exec_())