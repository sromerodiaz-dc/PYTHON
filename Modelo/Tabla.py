from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6.QtGui import QBrush


class ModeloTabla (QAbstractTableModel):
    # Constructor
    def __init__(self, tabla):
        super().__init__()
        self.tabla = tabla # Guardamos la tabla en un atributo

    # Este metodo es llamado por la vista para obtener el numero de filas
    def rowCount(self, index):
        return len(self.tabla)

    # Este metodo es llamado por la vista para obtener el numero de columnas
    def columnCount(self, index):
        return len(self.tabla[0])

    # Este metodo es llamado por la vista para obtener los datos de la tabla
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.tabla[index.row()][index.column()]
        # si es hombre poner el color de fondo en azul
        if role == Qt.ItemDataRole.BackgroundRole:
            if self.tabla[index.row()][2] == 'Home' and self.tabla[index.row()][3] == False:
                return QBrush(Qt.GlobalColor.cyan)
            if self.tabla[index.row()][2] == 'Muller' and self.tabla[index.row()][3] == False:
                return QBrush(Qt.GlobalColor.lightGray)
        if role == Qt.ItemDataRole.BackgroundRole:
            if self.tabla[index.row()][3]:
                return QBrush(Qt.GlobalColor.red)
        return None

    def add_row(self, row_data):
        self.beginInsertRows(self.index(0, 0), len(self.tabla), len(self.tabla))
        self.tabla.append(row_data)
        self.endInsertRows()

    def update_row(self, index, row_data):
        self.tabla[index] = row_data
        self.dataChanged.emit(self.index(index, 0), self.index(index, len(self.tabla[0])-1))

    def delete_row(self, index):
        self.beginRemoveRows(self.index(0, 0), index, index)
        del self.tabla[index]
        self.endRemoveRows()