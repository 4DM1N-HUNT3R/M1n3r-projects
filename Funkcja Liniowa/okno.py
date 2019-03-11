from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 60, 361, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 270, 361, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 360, 711, 71))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.Zatwierdz = QtGui.QPushButton(self.centralwidget)
        self.Zatwierdz.setGeometry(QtCore.QRect(560, 500, 200, 28))
        self.Zatwierdz.setObjectName(_fromUtf8("Zatwierdz"))
        self.Wyjscie = QtGui.QPushButton(self.centralwidget)
        self.Wyjscie.setGeometry(QtCore.QRect(350, 500, 201, 28))
        self.Wyjscie.setObjectName(_fromUtf8("Wyjscie"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 160, 701, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Funkcja Trygonometryczna", None))
        self.label_2.setText(_translate("MainWindow", "Podaj wspolczynnik a: ", None))
        self.Zatwierdz.setText(_translate("MainWindow", "Zatwierdz", None))
        self.Wyjscie.setText(_translate("MainWindow", "Wyjscie", None))
        self.label_3.setText(_translate("MainWindow", "Skrypt wyswietli wykres funkcji po wpisaniu wartosci ", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())