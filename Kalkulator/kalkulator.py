#!usr/bin/python
# coding: utf-8
import sys
import time
import math
import os 
import okno
from PyQt4 import QtGui, QtCore

def Zatwierdz():
	def Kalkulator():  
		print '\033[91m' "██╗  ██╗ █████╗ ██╗     ██╗  ██╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗"     
		print '\033[91m' "██║ ██╔╝██╔══██╗██║     ██║ ██╔╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗"    
		print '\033[91m' "█████╔╝ ███████║██║     █████╔╝ ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝"    
		print '\033[91m' "██╔═██╗ ██╔══██║██║     ██╔═██╗ ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗"   
		print '\033[91m' "██║  ██╗██║  ██║███████╗██║  ██╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║"    
		print '\033[91m' "╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝"    

	def dodawanie():
		print "██████╗  ██████╗ ██████╗  █████╗ ██╗    ██╗ █████╗ ███╗   ██╗██╗███████╗"
		print "██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██║    ██║██╔══██╗████╗  ██║██║██╔════╝"
		print "██║  ██║██║   ██║██║  ██║███████║██║ █╗ ██║███████║██╔██╗ ██║██║█████╗"
		print "██║  ██║██║   ██║██║  ██║██╔══██║██║███╗██║██╔══██║██║╚██╗██║██║██╔══╝"  
		print "██████╔╝╚██████╔╝██████╔╝██║  ██║╚███╔███╔╝██║  ██║██║ ╚████║██║███████╗"
		print "╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝" 
		a = int(uiplot.textEdit.toPlainText())
		b = int(uiplot.textEdit.toPlainText())
		if a == 0 or b == 0: 
			print '\033[91m' "Nic nie wybrales Wybrales zla opcje lub wpisales zero"
			time.sleep(2)
		c =  a + b
		print("Wynik Dodawania to: " + str(c))	


	def odejmowanie():
		print " ██████╗ ██████╗ ███████╗     ██╗███╗   ███╗ ██████╗ ██╗    ██╗ █████╗ ███╗   ██╗██╗███████╗"
		print "██╔═══██╗██╔══██╗██╔════╝     ██║████╗ ████║██╔═══██╗██║    ██║██╔══██╗████╗  ██║██║██╔════╝"
		print "██║   ██║██║  ██║█████╗       ██║██╔████╔██║██║   ██║██║ █╗ ██║███████║██╔██╗ ██║██║█████╗"  
		print "██║   ██║██║  ██║██╔══╝  ██   ██║██║╚██╔╝██║██║   ██║██║███╗██║██╔══██║██║╚██╗██║██║██╔══╝"  
		print "╚██████╔╝██████╔╝███████╗╚█████╔╝██║ ╚═╝ ██║╚██████╔╝╚███╔███╔╝██║  ██║██║ ╚████║██║███████╗"
		print  "╚═════╝ ╚═════╝ ╚══════╝ ╚════╝ ╚═╝     ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝" 
		a = int(uiplot.textEdit.toPlainText())
		b = int(uiplot.textEdit.toPlainText())
		if a == 0 or b == 0: 
			print '\033[91m' "Nic nie wybrales Wybrales zla opcje lub wpisales zero"
			time.sleep(2)
		c = a - b
		print("Wynik Odejmowania to: " + str(c))

			
	def mnozenie():
		print "███╗   ███╗███╗   ██╗ ██████╗ ███████╗███████╗███╗   ██╗██╗███████╗"
		print "████╗ ████║████╗  ██║██╔═══██╗╚══███╔╝██╔════╝████╗  ██║██║██╔════╝"
		print "██╔████╔██║██╔██╗ ██║██║   ██║  ███╔╝ █████╗  ██╔██╗ ██║██║█████╗"  
		print "██║╚██╔╝██║██║╚██╗██║██║   ██║ ███╔╝  ██╔══╝  ██║╚██╗██║██║██╔══╝"  
		print "██║ ╚═╝ ██║██║ ╚████║╚██████╔╝███████╗███████╗██║ ╚████║██║███████╗"
		print "╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝╚══════╝"
		a = int(uiplot.textEdit.toPlainText())
		b = int(uiplot.textEdit.toPlainText())
		if a == 0 or b == 0: 
			print '\033[91m' "Nic nie wybrales Wybrales zla opcje lub wpisales zero"
			time.sleep(2)
		c = a * b
		print("Wynik Mnozenia to: " + str(c))

			
	def dzielenie():
		print "██████╗ ███████╗██╗███████╗██╗     ███████╗███╗   ██╗██╗███████╗"
		print "██╔══██╗╚══███╔╝██║██╔════╝██║     ██╔════╝████╗  ██║██║██╔════╝"
		print "██║  ██║  ███╔╝ ██║█████╗  ██║     █████╗  ██╔██╗ ██║██║█████╗"  
		print "██║  ██║ ███╔╝  ██║██╔══╝  ██║     ██╔══╝  ██║╚██╗██║██║██╔══╝"  
		print "██████╔╝███████╗██║███████╗███████╗███████╗██║ ╚████║██║███████╗"
		print "╚═════╝ ╚══════╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝╚══════╝"	
		a = int(uiplot.textEdit.toPlainText())
		b = int(uiplot.textEdit.toPlainText())
		if a == 0 or b == 0: 
			print '\033[91m' "Nie dzieli sie przez zero"
			time.sleep(2)
		c = a / b
		print("Wynik Dzielenia to: " + str(c))


	def potegowanie(): 
		print "██████╗  ██████╗ ████████╗███████╗ ██████╗  ██████╗ ██╗    ██╗ █████╗ ███╗   ██╗██╗███████╗"
		print "██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝██╔════╝ ██╔═══██╗██║    ██║██╔══██╗████╗  ██║██║██╔════╝"
		print "██████╔╝██║   ██║   ██║   █████╗  ██║  ███╗██║   ██║██║ █╗ ██║███████║██╔██╗ ██║██║█████╗  "
		print "██╔═══╝ ██║   ██║   ██║   ██╔══╝  ██║   ██║██║   ██║██║███╗██║██╔══██║██║╚██╗██║██║██╔══╝  "
		print "██║     ╚██████╔╝   ██║   ███████╗╚██████╔╝╚██████╔╝╚███╔███╔╝██║  ██║██║ ╚████║██║███████╗"
		print "╚═╝      ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝"
		a = int(uiplot.textEdit.toPlainText())
		if (a == 0): 
			print '\033[91m' "Nic nie wybrales Wybrales zla opcje lub wpisales zero"
		c = a * a 
		print("Wynik Potegowania to: " + str(c))


	def pierwiastkowanie(): 
		print "██████╗ ██╗███████╗██████╗ ██╗    ██╗██╗ █████╗ ███████╗████████╗██╗  ██╗ ██████╗ ██╗    ██╗ █████╗ ███╗   ██╗██╗███████╗"
		print "██╔══██╗██║██╔════╝██╔══██╗██║    ██║██║██╔══██╗██╔════╝╚══██╔══╝██║ ██╔╝██╔═══██╗██║    ██║██╔══██╗████╗  ██║██║██╔════╝"
		print "██████╔╝██║█████╗  ██████╔╝██║ █╗ ██║██║███████║███████╗   ██║   █████╔╝ ██║   ██║██║ █╗ ██║███████║██╔██╗ ██║██║█████╗"  
		print "██╔═══╝ ██║██╔══╝  ██╔══██╗██║███╗██║██║██╔══██║╚════██║   ██║   ██╔═██╗ ██║   ██║██║███╗██║██╔══██║██║╚██╗██║██║██╔══╝"  
		print "██║     ██║███████╗██║  ██║╚███╔███╔╝██║██║  ██║███████║   ██║   ██║  ██╗╚██████╔╝╚███╔███╔╝██║  ██║██║ ╚████║██║███████╗"
		print "╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝"
		number = int(uiplot.textEdit.toPlainText())
		float_number = float(number)
		print ("Pierwiastek liczby to: " + str(math.sqrt(float_number)))


	def pole(): 
		print "   ____   ____   __     ______   ______ ____   ____       __ __ __  ___   ______ ___ "   
		print "  / __ \ / __ \ / /    / ____/  /_  __// __ \ / __ \     / // //_/ /   | /_  __//   |"      
		print " / /_/ // / / // /    / __/      / /  / /_/ // / / /__  / // ,<   / /| |  / /  / /| |"      
		print "/ ____// /_/ // /___ / /___     / /  / _, _// /_/ // /_/ // /| | / ___ | / /  / ___ |"      
		print"/_/     \____//_____//_____/    /_/  /_/ |_| \____/ \____//_/ |_|/_/  |_|/_/  /_/  |_|"  
		print"    ____   ____  _       __ _   __ ____   ____   ____   ______ _____    _   __ ______ ______ ____  "
		print"   / __ \ / __ \| |     / // | / // __ \ / __ ) / __ \ / ____//__  /   / | / // ____// ____// __ \ "
		print"  / /_/ // / / /| | /| / //  |/ // / / // __  |/ / / // /       / /   /  |/ // __/  / / __ / / / /"
		print" / _, _// /_/ / | |/ |/ // /|  // /_/ // /_/ // /_/ // /___    / /__ / /|  // /___ / /_/ // /_/ /" 
		print"/_/ |_| \____/  |__/|__//_/ |_/ \____//_____/ \____/ \____/   /____//_/ |_//_____/ \____/ \____/"  
		number = int(uiplot.textEdit.toPlainText())
		liczba_number = number * number  
		number2 = math.sqrt(9)  
		number3 = 4
		time.sleep(0.4)
		print("Pole trojkata rownobocznego wynosi: ")
		print(liczba_number)
		print("Pierwiastek z: " + str (number2))
		print("Na " + str (number3))
	def twierdzeniepitagorasa():
		a = int(uiplot.textEdit.toPlainText())
		b = int(uiplot.textEdit.toPlainText())
		c = a * a + b * b  
		if c % 2 == 0: 
			d = c / 2
			print ("Przeciwprostokatna c wynosi: ", d)  
		else: 
			print ("Trzeciego boku nie mozna podzielic wiec przeciwprostokatna wynosi: ", d)

	def nwd():
		os.system("python skrypt.py")

	while True:
		Kalkulator()
		print '\t' '\033[96m'"==================WYBIERZ OPCJE======================"
		time.sleep(0.1)
		print '\t' '\033[0m'"==================1 - DODAWANIE======================"
		time.sleep(0.1)
		print '\t'  "==================2 - ODEJMOWANIE===================="
		time.sleep(0.1)
		print '\t'  "==================3 - MNOZENIE======================="
		time.sleep(0.1)
		print '\t'  "==================4 - DZIELENIE======================"
		time.sleep(0.1)
		print '\t'  "==================5 - POTEGOWANIE===================="
		time.sleep(0.1)
		print '\t'  "==================6 - POLE TROJKATA ROWNOBOCZNEGO===="
		time.sleep(0.1)
		print '\t'  "==================7 - PIERWIASTKOWANIE==============="
		time.sleep(0.1)
		print '\t'  "==================8 - TWIERDZENIE PITAGORASA========="
		time.sleep(0.1)
		print '\t'  "==================9 - NAJWIEKSZA WSPOLNA WIELOKROTNOSC"
		time.sleep(0.1)
		print '\t'  "==================10 - WYJSCIE======================="
		wybor = int(uiplot.textEdit.toPlainText())
		odp = 0

		if wybor == "1":
			odp = dodawanie()
		elif wybor == "2":
			odp = odejmowanie() 
		elif wybor == "3":
			odp = mnozenie()
		elif wybor == "4":
			odp = dzielenie()
		elif wybor == "5": 
			odp = potegowanie()
		elif wybor == "6": 
			odp = pole()
		elif wybor == "7": 
			odp = pierwiastkowanie()
		elif wybor == "8":
			odp = twierdzeniepitagorasa()
		elif wybor == "9":	
			odp = nwd()
		elif wybor == "10":
			print '\033[91m' "Wychodzenie..."
			time.sleep(4)
			sys.exit(0)
		elif wybor != "10":
			print '\033[91m' "Nic nie wybrales Wybrales zla opcje lub wpisales zero"



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
