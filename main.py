#! /bin/python

import sys
import random

from PySide2.QtCore import QAbstractTableModel, Qt, QModelIndex, Slot
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine, qmlRegisterType


class Series(QAbstractTableModel):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__calculateValues()

    def rowCount(self, parent=QModelIndex()):
        return len(self.values)

    def columnCount(self, parent=QModelIndex()):
        return 2

    def data(self, index, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return super().data(index, role)

        row = index.row()
        col = index.column()

        return self.values[row][col]

    @Slot()
    def reloadModel(self):
        self.beginResetModel()
        self.__calculateValues()
        self.endResetModel()

    def __calculateValues(self):
        self.values = [(i, random.randint(0, 20)) for i in range(20)]

if __name__ == "__main__":
    app = QApplication(sys.argv)

    qmlRegisterType(Series, "myseries", 1, 0, "Series")
    engine = QQmlApplicationEngine()
    engine.load("./main.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
