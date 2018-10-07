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
        self.Zatwierdz = QtGui.QPushButton(self.centralwidget)
        self.Zatwierdz.setGeometry(QtCore.QRect(560, 470, 90, 31))
        self.Zatwierdz.setObjectName(_fromUtf8("Zatwierdz"))
        self.Wyjscie = QtGui.QPushButton(self.centralwidget)
        self.Wyjscie.setGeometry(QtCore.QRect(660, 470, 91, 31))
        self.Wyjscie.setObjectName(_fromUtf8("Wyjscie"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 90, 691, 75))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(60, 310, 691, 75))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 691, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 270, 681, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Zatwierdz.setText(_translate("MainWindow", "Zatwierdz", None))
        self.Wyjscie.setText(_translate("MainWindow", "Wyjscie", None))
        self.label.setText(_translate("MainWindow", "Podaj pierwsza liczbe ", None))
        self.label_2.setText(_translate("MainWindow", "Podaj druga liczbe", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

