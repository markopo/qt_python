import random
from PySide2 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):

    def get_label_font(self):
        font = QtGui.QFont()
        font.setPointSize(42)
        font.setBold(True)
        font.setItalic(True)
        return font

    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setFont(self.get_label_font())

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    def magic(self):
        self.text.setText(random.choice(self.hello))
