import sys

from PyQt4 import QtGui, QtCore
import pylab

import skrypt1

def Koniec(gui):
    wybor = QtGui.QMessageBox.question(gui, 'Koniec',
        "Na Pewno chcesz wyjsc ?",
        QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
    if wybor == QtGui.QMessageBox.Yes: 
        sys.exit()

def Zatwierdz():
    try:
        x = pylab.arange(-10, 10.5, 0.5)  
        a = int(uiplot.textEdit.toPlainText())
        y1 = [i / -3 + a for i in x if i <= 0]
        y2 = [i**2 / 3 for i in x if i >= 0]
        x1 = [i for i in x if i <= 0]
        x2 = [i for i in x if i >= 0]
        pylab.plot(x1, y1, x2, y2)
        pylab.title('Wykres f(x)')
        pylab.grid(True)
        pylab.show()
    except ValueError:
        print("Error")


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)

    gui_plot = skrypt1.QtGui.QMainWindow()
    uiplot = skrypt1.Ui_MainWindow()
    uiplot.setupUi(gui_plot)

    uiplot.Zatwierdz.clicked.connect(Zatwierdz)
    uiplot.Wyjscie.clicked.connect(lambda checked, w=gui_plot:Koniec(gui_plot))

    gui_plot.show()
    sys.exit(app.exec_())