import okno
import sys
from PyQt4 import QtGui, QtCore

def Zatwierdz():
    a = int(uiplot.textEdit.toPlainText())
    b = int(uiplot.textEdit.toPlainText())
    if a > 0 and b > 0: 
        while a > 0 and b > 0: 
            if a > b : 
                a = a % b
            else: 
                b = b % a 
            if a > b: 
                print ("NWD = ", a) 
            else: 
                print ("NWD = ", b)
    else: 
        print "Podaj zmienna a i b wieksza od zera" 

def Wyjscie(gui):
    wybor = QtGui.QMessageBox.question(gui, 'Wyjscie',
        "Na Pewno chcesz wyjsc ?",
        QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
    if wybor == QtGui.QMessageBox.Yes: 
        sys.exit()

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)

    gui_plot = okno.QtGui.QMainWindow()
    uiplot = okno.Ui_MainWindow()
    uiplot.setupUi(gui_plot)

    uiplot.Zatwierdz.clicked.connect(Zatwierdz)
    uiplot.Wyjscie.clicked.connect(lambda checked, w=gui_plot:Wyjscie(gui_plot))

    gui_plot.show()
    sys.exit(app.exec_())