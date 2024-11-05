from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QLayout, QVBoxLayout, QHBoxLayout


class Interfaz (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interfaz")
        self.show()
        self.setMinimumSize(600, 400)
        self.setMaximumSize(1200, 800)

        self.container = QWidget()
        self.setCentralWidget(self.container)
        self.layout = QHBoxLayout()
        self.container.setLayout(self.layout)

        self.izquierda = Izquierda()
        self.centro = Centro()
        self.derecha = Derecha()

        self.layout.addWidget(self.izquierda)
        self.layout.addWidget(self.centro)
        self.layout.addWidget(self.derecha)


class Izquierda (QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.izquierda1 = Izquierda1()
        self.izquierda2 = Izquierda2()
        self.izquierda3 = Izquierda3()

        self.layout.addWidget(self.izquierda1)
        self.layout.addWidget(self.izquierda2)
        self.layout.addWidget(self.izquierda3)



class Centro (QWidget):
    def __init__(self):
        super().__init__()
        pallete = self.palette()
        pallete.setColor(self.backgroundRole(), Qt.GlobalColor.green)
        self.setAutoFillBackground(True)
        self.setPalette(pallete)


class Derecha (QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.derecha1 = Derecha1()
        self.derecha2 = Derecha2()

        self.layout.addWidget(self.derecha1)
        self.layout.addWidget(self.derecha2)


class Izquierda1 (QWidget):
    def __init__(self):
        super().__init__()
        pallete = self.palette()
        pallete.setColor(self.backgroundRole(), Qt.GlobalColor.red)
        self.setAutoFillBackground(True)
        self.setPalette(pallete)


class Izquierda2 (QWidget):
    def __init__(self):
        super().__init__()
        pallete = self.palette()
        pallete.setColor(self.backgroundRole(), Qt.GlobalColor.yellow)
        self.setAutoFillBackground(True)
        self.setPalette(pallete)


class Izquierda3 (QWidget):
    def __init__(self):
        super().__init__()
        pallete = self.palette()
        pallete.setColor(self.backgroundRole(), Qt.GlobalColor.blue)
        self.setAutoFillBackground(True)
        self.setPalette(pallete)


class Derecha1 (QWidget):
    def __init__(self):
        super().__init__()
        pallete = self.palette()
        pallete.setColor(self.backgroundRole(), Qt.GlobalColor.yellow)
        self.setAutoFillBackground(True)
        self.setPalette(pallete)


class Derecha2 (QWidget):
    def __init__(self):
        super().__init__()
        pallete = self.palette()
        pallete.setColor(self.backgroundRole(), Qt.GlobalColor.blue)
        self.setAutoFillBackground(True)
        self.setPalette(pallete)
