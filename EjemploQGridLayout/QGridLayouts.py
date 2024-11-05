import sys
from random import randint

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QGridLayout

class CaixaColor (QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Principal")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

        ##self.crearCajasColor(5, 5)
        ##self.crearCajasColorIrregulares(5)

        self.layout.addWidget(CaixaColor(Qt.GlobalColor.red), 0, 0)
        self.layout.addWidget(CaixaColor(Qt.GlobalColor.green), 1, 0, 2, 1)
        self.layout.addWidget(CaixaColor(Qt.GlobalColor.blue), 0, 1, 1, 2)
        self.layout.addWidget(CaixaColor(QColor("pink")), 1, 1, 1, 2)
        self.layout.addWidget(CaixaColor(QColor("orange")), 2, 1)
        self.layout.addWidget(CaixaColor(QColor("yellow")), 2, 2)

        self.show()

    def elegirColorRandom (self):
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        return color

    def crearCajasColor (self, filas, columnas):
        for i in range(filas):
            for j in range(columnas):
                color = CaixaColor(self.elegirColorRandom())
                self.layout.addWidget(color, i, j)

    def crearCajasColorIrregulares (self, filas):
        for i in range(filas):
            random = randint(1, 5)
            for j in range(random):
                color = CaixaColor(self.elegirColorRandom())
                self.layout.addWidget(color, i, j, 1, 5-random)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())


