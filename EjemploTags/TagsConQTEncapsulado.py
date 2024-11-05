import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout

class Formulario(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Formulario de Datos")

        # Crear un layout de cuadrícula
        layout = QGridLayout()

        # Crear etiquetas y cajas de texto
        etiquetas_texto = ["Nombre", "DNI", "Dirección"]
        self.entradas = []

        for i, texto in enumerate(etiquetas_texto):
            # Etiquetas
            etiqueta = QLabel(texto)
            layout.addWidget(etiqueta, i, 0)

            # Cajas de texto
            entrada = QLineEdit()
            layout.addWidget(entrada, i, 1)
            self.entradas.append(entrada)

        # Crear los botones
        boton_aceptar = QPushButton("Aceptar")
        boton_denegar = QPushButton("Denegar")
        boton_cerrar = QPushButton("Cerrar")

        # Agregar los botones al layout
        layout.addWidget(boton_aceptar, len(etiquetas_texto), 0)
        layout.addWidget(boton_denegar, len(etiquetas_texto), 1)
        layout.addWidget(boton_cerrar, len(etiquetas_texto), 2)

        # Conectar los botones a las funciones
        boton_aceptar.clicked.connect(self.aceptar)
        boton_denegar.clicked.connect(self.denegar)
        boton_cerrar.clicked.connect(self.cerrar)

        # Configurar el layout en la ventana
        self.setLayout(layout)

    def aceptar(self):
        print("Aceptar presionado")

    def denegar(self):
        print("Denegar presionado")

    def cerrar(self):
        QApplication.quit()

# Crear la aplicación y mostrar la ventana
if __name__ == "__main__":
    app = QApplication(sys.argv)
    formulario = Formulario()
    formulario.show()
    sys.exit(app.exec_())
