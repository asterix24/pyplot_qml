import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QUrl

import qml_rc

if __name__ == "__main__":
    app = QApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.load("./main.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
