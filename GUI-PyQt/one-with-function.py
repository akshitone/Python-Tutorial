from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def clicked_btn():
    print("Clicked...")


def window():
    # just giving config setup via sys.argv to GUI
    app = QApplication(sys.argv)
    window_gui = QMainWindow()
    window_gui.setGeometry(500, 300, 500, 300)
    window_gui.setWindowTitle("one.py - Python-Tutorial - Akshit Mithaiwala")

    label = QtWidgets.QLabel(window_gui)
    label.setText("GUI programming with PyQt5 - Python 3")
    label.move(50, 30)

    button_1 = QtWidgets.QPushButton(window_gui)
    button_1.setText("Click Here!")
    button_1.clicked.connect(clicked_btn)

    window_gui.show()
    sys.exit(app.exec_())


window()
