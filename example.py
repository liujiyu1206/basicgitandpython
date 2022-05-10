
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


 

class MainWindow(QMainWindow):
    def __init__(self):
# When you subclass a Qt class 
# you must always call the super __init__ function
# to allow Qt to set up the object
        super().__init__()


        self.setWindowTitle('KanbanGUI')
    
        button = QPushButton('Press Me!')
        self.setFixedSize(QSize(400,500))

        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
        