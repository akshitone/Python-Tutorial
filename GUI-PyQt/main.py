from PyQt5.QtWidgets import *


class Page(QWidget):
    def __init__(self, parent=None):
        super(Page, self).__init__(parent)

        inner_label = QLabel("This is my first label in python.")
        inner_layout = QVBoxLayout()

        inner_layout.addWidget(inner_label)

        main_layout = QGridLayout()
        main_layout.addLayout(inner_layout, 0, 1)

        self.setLayout(main_layout)
        self.setWindowTitle("First GUI Qt - Python")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    window_object = Page()
    window_object.show()

    sys.exit(app.exec_())
