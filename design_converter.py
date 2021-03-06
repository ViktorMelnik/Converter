# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 200)
        MainWindow.setMinimumSize(QtCore.QSize(680, 200))
        MainWindow.setMaximumSize(QtCore.QSize(680, 200))
        MainWindow.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.convertor = QtWidgets.QWidget(MainWindow)
        self.convertor.setObjectName("convertor")
        self.l_equal = QtWidgets.QLabel(self.convertor)
        self.l_equal.setGeometry(QtCore.QRect(350, 40, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.l_equal.setFont(font)
        self.l_equal.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.l_equal.setObjectName("l_equal")
        self.l_result = QtWidgets.QLabel(self.convertor)
        self.l_result.setGeometry(QtCore.QRect(390, 40, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.l_result.setFont(font)
        self.l_result.setText("")
        self.l_result.setObjectName("l_result")
        self.pushButton = QtWidgets.QPushButton(self.convertor)
        self.pushButton.setGeometry(QtCore.QRect(20, 120, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.pushButton.setObjectName("pushButton")
        self.l_1 = QtWidgets.QLabel(self.convertor)
        self.l_1.setGeometry(QtCore.QRect(80, 10, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.l_1.setFont(font)
        self.l_1.setObjectName("l_1")
        self.enter_number = QtWidgets.QLineEdit(self.convertor)
        self.enter_number.setGeometry(QtCore.QRect(20, 40, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.enter_number.setFont(font)
        self.enter_number.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-radius: 5px")
        self.enter_number.setMaxLength(24)
        self.enter_number.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.enter_number.setObjectName("enter_number")
        self.sn = QtWidgets.QLineEdit(self.convertor)
        self.sn.setGeometry(QtCore.QRect(290, 40, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.sn.setFont(font)
        self.sn.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-radius: 5px")
        self.sn.setMaxLength(2)
        self.sn.setAlignment(QtCore.Qt.AlignCenter)
        self.sn.setObjectName("sn")
        self.l_2 = QtWidgets.QLabel(self.convertor)
        self.l_2.setGeometry(QtCore.QRect(300, 10, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.l_2.setFont(font)
        self.l_2.setObjectName("l_2")
        MainWindow.setCentralWidget(self.convertor)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Converter"))
        self.l_equal.setText(_translate("MainWindow", "="))
        self.pushButton.setText(_translate("MainWindow", "&Convert"))
        self.l_1.setText(_translate("MainWindow", "Enter a number"))
        self.l_2.setText(_translate("MainWindow", "sn"))
      
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    App_Convertor = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(App_Convertor)
    App_Convertor.show()
    sys.exit(app.exec_())
