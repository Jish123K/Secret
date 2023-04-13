import sys

from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(100, 100, 250, 150)

        self.setWindowTitle('MyApp')

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = MyApp()

    sys.exit(app.exec_())

