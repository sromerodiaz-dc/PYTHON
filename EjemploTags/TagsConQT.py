import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout

# Crear la aplicación de PyQt
app = QApplication(sys.argv)

# Crear la ventana principal
window = QWidget()
window.setWindowTitle("Formulario de Datos")

# Crear un layout de cuadrícula
layout = QGridLayout()

# Crear las etiquetas y cajas de texto
etiquetas_texto = ["Nombre", "DNI", "Dirección"]
entradas = []

for i, texto in enumerate(etiquetas_texto):
    # Etiquetas
    etiqueta = QLabel(texto)
    layout.addWidget(etiqueta, i, 0)

    # Cajas de texto
    entrada = QLineEdit()
    layout.addWidget(entrada, i, 1)
    entradas.append(entrada)

# Crear los botones
boton_aceptar = QPushButton("Aceptar")
boton_denegar = QPushButton("Denegar")
boton_cerrar = QPushButton("Cerrar")

# Agregar los botones al layout
layout.addWidget(boton_aceptar, len(etiquetas_texto), 0)
layout.addWidget(boton_denegar, len(etiquetas_texto), 1)
layout.addWidget(boton_cerrar, len(etiquetas_texto), 2)

# Definir las funciones de los botones
boton_aceptar.clicked.connect(lambda: print("Aceptar presionado"))
boton_denegar.clicked.connect(lambda: print("Denegar presionado"))
boton_cerrar.clicked.connect(app.quit)

# Configurar el layout en la ventana
window.setLayout(layout)

# Mostrar la ventana
window.show()

# Ejecutar la aplicación
sys.exit(app.exec_())
