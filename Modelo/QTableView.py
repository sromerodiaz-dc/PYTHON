import sys

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTableView, QLineEdit, QComboBox, \
    QCheckBox, QHBoxLayout, QPushButton, QGridLayout, QLabel, QApplication

from Modelo.Conn import DatabaseConnection
from Modelo.Tabla import ModeloTabla

class EjemploQTableView(QMainWindow):
    estado_operacion = 0
    def __init__(self):
        super().__init__()
        self.conexion = DatabaseConnection()
        self.conexion.crear_tabla("personas", "nome TEXT, dni TEXT, genero TEXT, fallecido BOOLEAN")
        self.setWindowTitle("Ejemplo QTableView")

        self.datos = [['Nome','DNI','Genero','Fallecido']]
        self.datos.extend(self.conexion.leer("personas"))

        caja_h = QHBoxLayout()
        self.tvw_tabla = QTableView()
        self.modelo = ModeloTabla(self.datos)
        self.tvw_tabla.setModel(self.modelo)
        self.tvw_tabla.setSelectionMode(QTableView.SelectionMode.SingleSelection)

        caja_h.addWidget(self.tvw_tabla)

        caja_v = QVBoxLayout()
        textos_g = QGridLayout()
        botones_h = QHBoxLayout()
        fallecido_h = QHBoxLayout()
        botones_aceptar_cancelar_h= QHBoxLayout()

        self.txtNome = QLineEdit()
        textos_g.addWidget(self.txtNome, 0, 0)
        self.txtDni = QLineEdit()
        textos_g.addWidget(self.txtDni, 0, 1)
        self.cmbGenero = QComboBox()
        self.cmbGenero.addItems(('Home', 'Muller', 'Outros'))
        textos_g.addWidget(self.cmbGenero , 1, 0)
        self.chkFallecido = QCheckBox()
        self.labelFallecido = QLabel("Fallecido")


        texto_boton = ("Editar", "Añadir", "Eliminar", "Aceptar", "Cancelar")
        self.boton_add = QPushButton(texto_boton[1])
        self.boton_editar = QPushButton(texto_boton[0])
        self.boton_eliminar = QPushButton(texto_boton[2])
        self.boton_aceptar = QPushButton(texto_boton[3])
        self.boton_cancelar = QPushButton(texto_boton[4])

        self.boton_add.clicked.connect(self.add)
        self.boton_editar.clicked.connect(self.editar)
        self.boton_eliminar.clicked.connect(self.eliminar)
        self.boton_aceptar.clicked.connect(self.aceptar)
        self.boton_cancelar.clicked.connect(self.cancelar)


        botones_h.addWidget(self.boton_add)
        botones_h.addWidget(self.boton_editar)
        botones_h.addWidget(self.boton_eliminar)
        fallecido_h.addWidget(self.chkFallecido)
        fallecido_h.addWidget(self.labelFallecido)
        botones_aceptar_cancelar_h.addStretch() # Añade un espacio en blanco
        botones_aceptar_cancelar_h.addWidget(self.boton_aceptar)
        botones_aceptar_cancelar_h.addWidget(self.boton_cancelar)

        textos_g.addLayout(fallecido_h, 1, 1)

        caja_v.addLayout(textos_g)
        caja_v.addLayout(botones_h)
        caja_v.addWidget(self.boton_eliminar)
        caja_v.addLayout(botones_aceptar_cancelar_h)


        caja_h.addLayout(caja_v)

        self.aceptar()

        container = QWidget()
        container.setLayout(caja_h)
        self.setCentralWidget(container)
        self.setFixedSize(800, 400)
        self.show()

    def add(self):
        print("Añadir")
        self.estado_operacion = 1
        self.estado_add()

    def editar(self):
        print("Editar")
        self.estado_operacion = 2
        self.estado_editar()
        #self.setDatosFromID()

    def eliminar(self):
        print("Eliminar")
        self.estado_operacion = 3
        self.estado_eliminar()
        #self.setDatosFromID()

    def aceptar(self):
        print("Aceptar")
        if self.estado_operacion == 1:
            self.add_action()
        elif self.estado_operacion == 2:
            self.edit_action()
        elif self.estado_operacion == 3:
            self.delete_action()
        self.repaint()
        self.estado_visualizar()
        self.estado_operacion = 0

    def cancelar(self):
        print("Cancelar")
        self.estado_visualizar()
        self.estado_operacion = 0


    def estado_visualizar(self):
        self.txtNome.setEnabled(False)
        self.txtDni.setEnabled(False)
        self.cmbGenero.setEnabled(False)
        self.chkFallecido.setEnabled(False)
        self.boton_aceptar.setEnabled(False)
        self.boton_cancelar.setEnabled(False)
        self.boton_add.setEnabled(True)
        self.boton_editar.setEnabled(True)
        self.boton_eliminar.setEnabled(True)
        self.tvw_tabla.setEnabled(True)
        self.txtNome.clear()
        self.txtDni.clear()
        self.cmbGenero.setCurrentIndex(0)
        self.chkFallecido.setChecked(False)
        self.tvw_tabla.clearSelection()

    def editar_add_aux(self):
        self.txtNome.setEnabled(True)
        self.txtDni.setEnabled(True)
        self.cmbGenero.setEnabled(True)
        self.chkFallecido.setEnabled(True)
        self.boton_aceptar.setEnabled(True)
        self.boton_cancelar.setEnabled(True)
        self.boton_add.setEnabled(False)
        self.boton_editar.setEnabled(False)
        self.boton_eliminar.setEnabled(False)

    def estado_editar(self):
        self.editar_add_aux()
        self.tvw_tabla.setEnabled(True)

    def estado_add(self):
        self.editar_add_aux()
        self.tvw_tabla.setEnabled(False)

    def estado_eliminar(self):
        self.txtNome.setEnabled(False)
        self.txtDni.setEnabled(False)
        self.cmbGenero.setEnabled(False)
        self.chkFallecido.setEnabled(False)
        self.boton_aceptar.setEnabled(True)
        self.boton_cancelar.setEnabled(True)
        self.boton_add.setEnabled(False)
        self.boton_editar.setEnabled(False)
        self.boton_eliminar.setEnabled(False)
        self.tvw_tabla.setEnabled(True)

    def aux_add_edit(self):
        nombre = self.txtNome.text()
        dni = self.txtDni.text()
        genero = self.cmbGenero.currentText()
        fallecido = self.chkFallecido.isChecked()

        if not nombre or not dni:
            print("Los campos Nome y DNI son obligatorios.")
            return

        return [nombre, dni, genero, fallecido]

    def add_action(self):
        self.modelo.add_row(self.aux_add_edit())
        self.conexion.insertar("personas", self.txtNome.text(), self.txtDni.text(), self.cmbGenero.currentText(), self.chkFallecido.isChecked())
        print("Add to database")

    def edit_action(self):
        self.modelo.update_row(self.tvw_tabla.currentIndex().row(), self.aux_add_edit())
        self.conexion.update_item("personas", self.txtNome.text(), self.txtDni.text(), self.cmbGenero.currentText(), self.chkFallecido.isChecked())
        print("Edit to database")

    def delete_action(self):
        self.conexion.delete_item("personas", self.datos[self.tvw_tabla.currentIndex().row()][1])
        self.modelo.delete_row(self.tvw_tabla.currentIndex().row())
        print("Delete to database")

    def setDatosFromID(self):
        self.modelo.delete_row(self.tvw_tabla.currentIndex().row())
        self.txtNome.setText(self.datos[self.tvw_tabla.currentIndex().row()][0])
        self.txtDni.setText(self.datos[self.tvw_tabla.currentIndex().row()][1])
        self.cmbGenero.setCurrentText(self.datos[self.tvw_tabla.currentIndex().row()][2])
        self.chkFallecido.setChecked(self.datos[self.tvw_tabla.currentIndex().row()][3])

    def repaint(self):
        self.modelo.layoutChanged.emit()
        self.tvw_tabla.repaint()
        self.tvw_tabla.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = EjemploQTableView()
    app.exec()