from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QImage

tick = QImage('tick.png')

class ModeloLista(QAbstractListModel):
    def __init__(self, lista=None):
        super().__init__()
        self.lista = lista or [] # Si la lista no existe entonces la crea

    def data(self, index, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            _, texto = self.lista[index.row()]
            return texto

        if rol == Qt.ItemDataRole.DecorationRole:
            estado,_ = self.lista[index.row()]
            if estado:
                return estado

    def rowCount(self, index):
        return len(self.lista)
