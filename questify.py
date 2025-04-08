from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont,QIcon
from PyQt5.QtCore import Qt
import sys

class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        line1 = QLineEdit()
        line1.setValidator(QIntValidator())
        line1.setMaxLength(4)
        line1.setAlignment(Qt.AlignRight)
        line1.setFont(QFont("Arial",20)) 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = lineEditDemo()
    windows.resize(500,500)
    windows.move(100,100)
    windows.setWindowTitle('Questify')
    windows.show()
    sys.exit(app.exec_())
