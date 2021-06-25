import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.on_click()
    def initUI(self):
        self.button = QPushButton('PyQt5 button', self)
        self.button.move(100,200)
        self.button.clicked.connect(self.on_click)
        self.text = QTextEdit(self)
        insideText = "Text"
        self.text.document().setPlainText(insideText)
        self.text.resize(100,25)


    def on_click(self):
        print('PyQt5 button click')
        position = self.text.pos()
        self.text.move(position.x()+50,position.y()+0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
