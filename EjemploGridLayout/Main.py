import sys

from PyQt6.QtWidgets import QApplication

from Interfaz import Interfaz

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    interfaz = Interfaz()
    aplicacion.exec()
    sys.exit(aplicacion.exec())