import sys
from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QListView, QWidget, QApplication,
    QPushButton, QHBoxLayout, QLineEdit
)
from ModeloLista.QList import ModeloLista


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Ejemplo QListView con TabWidget")
        self.setFixedSize(400, 400)

        # Modelo de datos
        lista = [(False, "Ir al gym"), (False, "Hacer los deberes"), (False, "Sacar al perro")]
        self.modelo = ModeloLista(lista)

        # Configuración principal del diseño
        layout_principal = QVBoxLayout()

        # Configuración de la QListView
        self.qLista = QListView()
        self.qLista.setModel(self.modelo)
        self.qLista.setSelectionMode(QListView.SelectionMode.MultiSelection)
        layout_principal.addWidget(self.qLista)

        # Botones (Eliminar y Completar)
        layout_botones = QHBoxLayout()
        btn_del = QPushButton("Eliminar")
        btn_com = QPushButton("Completar")
        btn_del.pressed.connect(self.on_btnBorrar)
        btn_com.pressed.connect(self.on_btnCompletar)
        layout_botones.addWidget(btn_del)
        layout_botones.addWidget(btn_com)
        layout_principal.addLayout(layout_botones)

        # Campo de texto
        self.text_input = QLineEdit()
        layout_principal.addWidget(self.text_input)

        # Boton añadir elementos a la lista
        btn_add = QPushButton("Agregar")
        btn_add.pressed.connect(self.on_btnAdd)
        layout_principal.addWidget(btn_add)

        # Establecer el diseño en el widget principal
        contenedor_central = QWidget()
        contenedor_central.setLayout(layout_principal)
        self.setCentralWidget(contenedor_central)

    def on_btnBorrar(self):
        # Imprime "Borrar" en la consola para verificar que el botón está funcionando
        print("Borrar")

        # Obtiene los índices seleccionados en el QListView
        index = self.qLista.selectedIndexes()

        # Si hay elementos seleccionados
        if index:
            # Itera a través de los índices seleccionados
            for i in sorted(index, reverse=True):
                # Elimina el elemento correspondiente al índice seleccionado
                del self.modelo.lista[i.row()]

            # Notifica al modelo que los datos han cambiado, para que el QListView se actualice
            self.modelo.layoutChanged.emit()

            # Limpia la selección del QListView, para que no queden elementos resaltados
            self.qLista.clearSelection()

    def on_btnCompletar(self):
        print("Completar")
        # Obtiene los índices seleccionados en el QListView
        index = self.qLista.selectedIndexes()

        # Si hay elementos seleccionados
        if index:
            # Itera a través de los índices seleccionados
            for i in sorted(index, reverse=True):
                # Elimina el elemento correspondiente al índice seleccionado
                self.modelo.lista[i.row()] = True

            # Notifica al modelo que los datos han cambiado, para que el QListView se actualice
            self.modelo.layoutChanged.emit()

            # Limpia la selección del QListView, para que no queden elementos resaltados
            self.qLista.clearSelection()


    def on_btnAdd(self):
        print("Agregar")
        texto = self.text_input.text().strip()
        if texto != "":
            self.modelo.lista.append((False, texto))
            self.modelo.layoutChanged.emit()
            self.text_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show()
    sys.exit(app.exec())
