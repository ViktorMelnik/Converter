import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from design_converter import *

class Convertor(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.setWindowIcon(QIcon('icon1.png'))
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.convert)
        
    def convert(self):
        try:
            input_number = self.ui.enter_number.text()
            sn_number = int(self.ui.sn.text())
            rezult = int(input_number, sn_number)
            self.ui.l_result.setText(str(rezult))
        except:
            error_msg = QtWidgets.QMessageBox()
            error_msg.setWindowTitle('Ошибка ввода!')
            error_msg.setText('Введите корректные данные!')
            error_msg.setIcon(error_msg.Warning)
            error_msg.exec() 
            
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    app_convertor = Convertor()
    app_convertor.show()
    sys.exit(app.exec_())