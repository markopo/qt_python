import sys
from PySide2 import QtCore, QtWidgets, QtGui
from hello_world import MyWidget

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec_())
