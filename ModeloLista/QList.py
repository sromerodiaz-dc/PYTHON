from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QImage, QPixmap

tick = QImage('tick.png')

class ModeloLista(QAbstractListModel):
    def __init__(self, lista=None):
        super().__init__()
        self.lista = lista or [] # Si la lista no existe entonces la crea

    def data(self, index, rol):
        if not index.isValid():
            return None

        estado, texto = self.lista[index.row()] # guarda los valores de la tupla

        if rol == Qt.ItemDataRole.DisplayRole:
            return texto # return texto

        if rol == Qt.ItemDataRole.DecorationRole:
            if estado:
                return QPixmap.fromImage(tick) # return Tick Verde

        return None # rol no manejado

    def rowCount(self, index):
        return len(self.lista)
