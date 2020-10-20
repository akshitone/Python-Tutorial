from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(500, 300, 500, 300)
        self.setWindowTitle("one.py - Python-Tutorial - Akshit Mithaiwala")
        self.init_ui()

    def init_ui(self):
        # self becuase this class contain QMainWindow already as a parent class / self argument
        self.label = QtWidgets.QLabel(self)
        self.label.setText("GUI programming with PyQt5 - Python 3")
        self.update()
        self.label.move(50, 30)

        self.button_1 = QtWidgets.QPushButton(self)
        self.button_1.setText("Click Here!")
        self.button_1.clicked.connect(self.clicked_btn)

    def clicked_btn(self):
        self.label.setText(
            "You clicked the button! GUI programming with PyQt5 - Python 3")
        self.update()

    def update(self):
        self.label.adjustSize()


def clicked_btn():
    print("Clicked...")


def window():
    # just giving config setup via sys.argv to GUI
    app = QApplication(sys.argv)
    window_gui = Window()

    window_gui.show()
    sys.exit(app.exec_())


window()
