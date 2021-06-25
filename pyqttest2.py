import sys
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout,QLineEdit,QLabel, QApplication, QTextEdit, QPushButton, QScrollArea

def main(): 
    app = QApplication(sys.argv) 
    w = MyWindow() 
    w.show() 
    sys.exit(app.exec_()) 


class MyWindow(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args)

        # create objects
        self.la = QLabel("Press tab in this box:")
        self.le = MyLineEdit()
        self.la2 = QLabel("\nLook here:")
        self.le2 = QLineEdit()

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.la)
        layout.addWidget(self.le)
        layout.addWidget(self.la2)
        layout.addWidget(self.le2)
        self.setLayout(layout)

        # connections
        self.connect(self.le, SIGNAL("tabPressed"),
                     self.update)

    def update(self):
        newtext = str(self.le2.text()) + "tab pressed "
        self.le2.setText(newtext)


class MyLineEdit(QLineEdit):
    def __init__(self, *args):
        QLineEdit.__init__(self, *args)
        
    def event(self, event):
        if (event.type()==QEvent.KeyPress) and (event.key()==Qt.Key_Tab):
            self.emit(SIGNAL("tabPressed"))
            return True

        return QLineEdit.event(self, event)


if __name__ == "__main__": 
    main()