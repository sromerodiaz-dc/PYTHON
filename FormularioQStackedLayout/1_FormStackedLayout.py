import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedLayout, \
    QRadioButton, QCheckBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

# Clase auxiliar para crear widgets de colores
class CaixaColor(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color};")
        label = QLabel(color, self)
        label.setStyleSheet("color: white; font-size: 24px;")
        label.setAlignment(Qt.AlignCenter)

class StakedLayout(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo StackedLayout con PyQt5")
        self.setFixedWidth(300)
        self.setFixedHeight(150)

        # Layouts principales
        cajaV = QVBoxLayout()
        cajaH = QHBoxLayout()  # 1ª fila
        cajaH2 = QHBoxLayout() # 2ª fila
        cajaH3 = QHBoxLayout() # 3ª fila

        # Agregar layout horizontal al vertical que conformará la primera fila
        cajaV.addLayout(cajaH)

        # Crear botones y conectarlos a funciones
        btn_rojo = QPushButton("Rojo")
        btn_azul = QPushButton("Azul")
        btn_verde = QPushButton("Verde")
        btn_naranja = QPushButton("Naranja")

        cajaH.addWidget(btn_rojo)
        cajaH.addWidget(btn_azul)
        cajaH.addWidget(btn_verde)
        cajaH.addWidget(btn_naranja)

        # Agrego segunda fila
        cajaV.addLayout(cajaH2)

        # Crear QRadioButton's
        rbtn_rojo = QRadioButton("Rojo")
        rbtn_azul = QRadioButton("Azul")
        rbtn_verde = QRadioButton("Verde")
        rbtn_naranja = QRadioButton("Naranja")

        cajaH2.addWidget(rbtn_rojo)
        cajaH2.addWidget(rbtn_azul)
        cajaH2.addWidget(rbtn_verde)
        cajaH2.addWidget(rbtn_naranja)

        # Agrego tercera fila
        cajaV.addLayout(cajaH3)

        # Crear QCheckBox
        cbtn_rojo = QCheckBox("Rojo")
        cbtn_azul = QCheckBox("Azul")
        cbtn_verde = QCheckBox("Verde")
        cbtn_naranja = QCheckBox("Naranja")

        cajaH3.addWidget(cbtn_rojo)
        cajaH3.addWidget(cbtn_azul)
        cajaH3.addWidget(cbtn_verde)
        cajaH3.addWidget(cbtn_naranja)

        # Crear QStackedLayout y agregar widgets de colores
        self.stack = QStackedLayout()
        self.stack.addWidget(CaixaColor("red"))
        self.stack.addWidget(CaixaColor("blue"))
        self.stack.addWidget(CaixaColor("green"))
        self.stack.addWidget(CaixaColor("orange"))

        # Configurar índice inicial
        self.stack.setCurrentIndex(2)

        # Agregar QStackedLayout al layout vertical
        cajaV.addLayout(self.stack)

        # Conectar botones a funciones para cambiar el índice
        btn_rojo.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        btn_azul.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        btn_verde.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        btn_naranja.clicked.connect(lambda: self.stack.setCurrentIndex(3))

        rbtn_rojo.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        rbtn_azul.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        rbtn_verde.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        rbtn_naranja.clicked.connect(lambda: self.stack.setCurrentIndex(3))

        cbtn_rojo.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        cbtn_azul.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        cbtn_verde.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        cbtn_naranja.clicked.connect(lambda: self.stack.setCurrentIndex(3))

        # Configurar el widget central
        control = QWidget()
        control.setLayout(cajaV)
        self.setCentralWidget(control)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = StakedLayout()
    ventana.show()
    sys.exit(app.exec())

