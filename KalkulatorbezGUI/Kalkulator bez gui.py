#!usr/bin/python
# coding: utf-8

import numpy as np
import sys
import time
import math
import os
from math import sqrt

def Kalkulator():  
	print('\033[91m' "██╗  ██╗ █████╗ ██╗     ██╗  ██╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗")
	print('\033[91m' "██║ ██╔╝██╔══██╗██║     ██║ ██╔╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗")
	print('\033[91m' "█████╔╝ ███████║██║     █████╔╝ ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝")
	print('\033[91m' "██╔═██╗ ██╔══██║██║     ██╔═██╗ ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗")
	print('\033[91m' "██║  ██╗██║  ██║███████╗██║  ██╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║")
	print('\033[91m' "╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝")

def dodawanie():
	print("██████╗  ██████╗ ██████╗  █████╗ ██╗    ██╗ █████╗ ███╗   ██╗██╗███████╗")
	print("██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██║    ██║██╔══██╗████╗  ██║██║██╔════╝")
	print("██║  ██║██║   ██║██║  ██║███████║██║ █╗ ██║███████║██╔██╗ ██║██║█████╗")
	print("██║  ██║██║   ██║██║  ██║██╔══██║██║███╗██║██╔══██║██║╚██╗██║██║██╔══╝")
	print("██████╔╝╚██████╔╝██████╔╝██║  ██║╚███╔███╔╝██║  ██║██║ ╚████║██║███████╗")
	print("╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝")
    	a = raw_input("Podaj pierwsza liczbe: ")
	b = raw_input("Podaj druga liczbe: ")
	if a == 0 or b == 0: 
		print('\033[91m' "Nic nie wybrales Wybrales zla opcje lub wpisales zero")
		time.sleep(2)
	c =  a + b
	print("Wynik Dodawania to: " + str(c))


def odejmowanie():
	print(" ██████╗ ██████╗ ███████╗     ██╗███╗   ███╗ ██████╗ ██╗    ██╗ █████╗ ███╗   ██╗██╗███████╗")
	print("██╔═══██╗██╔══██╗██╔════╝     ██║████╗ ████║██╔═══██╗██║    ██║██╔══██╗████╗  ██║██║██╔════╝")
	print("██║   ██║██║  ██║█████╗       ██║██╔████╔██║██║   ██║██║ █╗ ██║███████║██╔██╗ ██║██║█████╗")
	print("██║   ██║██║  ██║██╔══╝  ██   ██║██║╚██╔╝██║██║   ██║██║███╗██║██╔══██║██║╚██╗██║██║██╔══╝")
	print("╚██████╔╝██████╔╝███████╗╚█████╔╝██║ ╚═╝ ██║╚██████╔╝╚███╔███╔╝██║  ██║██║ ╚████║██║███████╗")
	print( "╚═════╝ ╚═════╝ ╚══════╝ ╚════╝ ╚═╝     ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝")
	a = raw_input("Podaj pierwsza liczbe: ")
	b = raw_input("Podaj druga liczbe: ")
	if a == 0 or b == 0: 
		print('\033[91m' "Nic nie wybrales Wybrales zla opcje lub wpisales zero")
		time.sleep(2)
	c = a - b
	print("Wynik Odejmowania to: " + str(c))

	       
def mnozenie():
	print("███╗   ███╗███╗   ██╗ ██████╗ ███████╗███████╗███╗   ██╗██╗███████╗")
	print("████╗ ████║████╗  ██║██╔═══██╗╚══███╔╝██╔════╝████╗  ██║██║██╔════╝")
	print("██╔████╔██║██╔██╗ ██║██║   ██║  ███╔╝ █████╗  ██╔██╗ ██║██║█████╗"  )
	print("██║╚██╔╝██║██║╚██╗██║██║   ██║ ███╔╝  ██╔══╝  ██║╚██╗██║██║██╔══╝"  )
	print("██║ ╚═╝ ██║██║ ╚████║╚██████╔╝███████╗███████╗██║ ╚████║██║███████╗")
	print("╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝╚══════╝")
	a = raw_input("Podaj pierwsza liczbe: ")
	b = raw_input("Podaj druga liczbe: ")
	if a == 0 or b == 0: 
		print('\033[91m' "Nic nie wybrales Wybrales zla opcje lub wpisales zero")
		time.sleep(2)
	c = a * b
	print("Wynik Mnozenia to: " + str(c))

	    
def dzielenie():
	print("██████╗ ███████╗██╗███████╗██╗     ███████╗███╗   ██╗██╗███████╗")
	print("██╔══██╗╚══███╔╝██║██╔════╝██║     ██╔════╝████╗  ██║██║██╔════╝")
	print("██║  ██║  ███╔╝ ██║█████╗  ██║     █████╗  ██╔██╗ ██║██║█████╗")
	print("██║  ██║ ███╔╝  ██║██╔══╝  ██║     ██╔══╝  ██║╚██╗██║██║██╔══╝")
	print("██████╔╝███████╗██║███████╗███████╗███████╗██║ ╚████║██║███████╗")
	print("╚═════╝ ╚══════╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝╚══════╝")
	a = raw_input("Podaj pierwsza liczbe: ")
	b = raw_input("Podaj druga liczbe: ")
	if a == 0 or b == 0: 
		print('\033[91m' "Nie dzieli sie przez zero")
		time.sleep(2)
	c = a / b
	print("Wynik Dzielenia to: " + str(c))


def potegowanie(): 
	print("██████╗  ██████╗ ████████╗███████╗ ██████╗  ██████╗ ██╗    ██╗ █████╗ ███╗   ██╗██╗███████╗")
	print("██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝██╔════╝ ██╔═══██╗██║    ██║██╔══██╗████╗  ██║██║██╔════╝")
	print("██████╔╝██║   ██║   ██║   █████╗  ██║  ███╗██║   ██║██║ █╗ ██║███████║██╔██╗ ██║██║█████╗  ")
	print("██╔═══╝ ██║   ██║   ██║   ██╔══╝  ██║   ██║██║   ██║██║███╗██║██╔══██║██║╚██╗██║██║██╔══╝  ")
	print("██║     ╚██████╔╝   ██║   ███████╗╚██████╔╝╚██████╔╝╚███╔███╔╝██║  ██║██║ ╚████║██║███████╗")
	print("╚═╝      ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝")
	a = raw_input("Podaj liczbe do spotegowania")
	if (a == 0): 
		print('\033[91m' "Nic nie wybrales Wybrales zla opcje lub wpisales zero")
	c = a * a 
	print("Wynik Potegowania to: " + str(c))


def pierwiastkowanie(): 
	print("██████╗ ██╗███████╗██████╗ ██╗    ██╗██╗ █████╗ ███████╗████████╗██╗  ██╗ ██████╗ ██╗    ██╗ █████╗ ███╗   ██╗██╗███████╗")
	print("██╔══██╗██║██╔════╝██╔══██╗██║    ██║██║██╔══██╗██╔════╝╚══██╔══╝██║ ██╔╝██╔═══██╗██║    ██║██╔══██╗████╗  ██║██║██╔════╝")
	print("██████╔╝██║█████╗  ██████╔╝██║ █╗ ██║██║███████║███████╗   ██║   █████╔╝ ██║   ██║██║ █╗ ██║███████║██╔██╗ ██║██║█████╗")
	print("██╔═══╝ ██║██╔══╝  ██╔══██╗██║███╗██║██║██╔══██║╚════██║   ██║   ██╔═██╗ ██║   ██║██║███╗██║██╔══██║██║╚██╗██║██║██╔══╝")
	print("██║     ██║███████╗██║  ██║╚███╔███╔╝██║██║  ██║███████║   ██║   ██║  ██╗╚██████╔╝╚███╔███╔╝██║  ██║██║ ╚████║██║███████╗")
	print("╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝")
	number = raw_input("Podaj liczbe do spierwiastkowania: ")
	float_number = float(number)
	print ("Pierwiastek liczby to: " + str(math.sqrt(float_number)))


def pole(): 
	print("   ____   ____   __     ______   ______ ____   ____       __ __ __  ___   ______ ___ ")
	print("  / __ \ / __ \ / /    / ____/  /_  __// __ \ / __ \     / // //_/ /   | /_  __//   |")
	print(" / /_/ // / / // /    / __/      / /  / /_/ // / / /__  / // ,<   / /| |  / /  / /| |")
	print("/ ____// /_/ // /___ / /___     / /  / _, _// /_/ // /_/ // /| | / ___ | / /  / ___ |")
	print("/_/     \____//_____//_____/    /_/  /_/ |_| \____/ \____//_/ |_|/_/  |_|/_/  /_/  |_|")
	print("    ____   ____  _       __ _   __ ____   ____   ____   ______ _____    _   __ ______ ______ ____  ")
	print("   / __ \ / __ \| |     / // | / // __ \ / __ ) / __ \ / ____//__  /   / | / // ____// ____// __ \ ")
	print("  / /_/ // / / /| | /| / //  |/ // / / // __  |/ / / // /       / /   /  |/ // __/  / / __ / / / /")
	print(" / _, _// /_/ / | |/ |/ // /|  // /_/ // /_/ // /_/ // /___    / /__ / /|  // /___ / /_/ // /_/ /")
	print("/_/ |_| \____/  |__/|__//_/ |_/ \____//_____/ \____/ \____/   /____//_/ |_//_____/ \____/ \____/")
	number = raw_input("Podaj bok trojkata: ")
	liczba_number = number * number  
	number2 = math.sqrt(9)  
	number3 = 4
	time.sleep(0.4)
	print("Pole trojkata rownobocznego wynosi: ")
	print(liczba_number)
	print("Pierwiastek z: " + str (number2))
	print("Na " + str (number3))
def twierdzeniepitagorasa():
    	a = raw_input("Podaj przyprostokatna a: ")
	b = raw_input("Podaj przyprostokatna b: ")
	c = a * a + b * b  
	if c % 2 == 0 : 
		d = c / 2
		print ("Przeciwprostokatna c wynosi: ", d)  
	else: 
		print ("Trzeciego boku nie mozna podzielic wiec przeciwprostokatna wynosi: ", d)

def nwd():
    os.system("python skrypt.py")

def poleprostokata():
	a = int(raw_input("Podaj pierwszy bok: "))
	b = int(raw_input("Podaj drugi bok: "))
	c = a * b
	if a == 0 or b == 0: 
		print('\033[91m' "Podaj liczbe wieksza od zera!!")
	else: 
		print ("Pole prostokata wynosi: ", c)

def polekwadratu(): 
	a = int(raw_input("Podaj bok: "))
	b = a * a 
	if a == 0: 
		print('\033[91m' "Podaj liczbe wieksza od zera!!")
	else:
		print("Pole kwadratu wynosi: ", b)

def pole_rombu():
	a = int(raw_input("Podaj krotszy bok: "))
	h = int(raw_input("Podaj wysokosc: "))
	if a == 0 or h == 0:
		print ("Podaj liczbe wieksza od zera!")
	else:	
		P = a * h
		print ("Pole rombu wynosi: ", P)
		Obw = a * a * a * a
		print ("Obwod rombu wynosi: ", Obw)

def funkcje_trygonometryczne():
	#tworz zmienna x
	x = np.pi/3
	#oblicz wartosci funkcji trygonometrycznych
	print("sinus wynosi(%f)%f" % (x,np.sin(x)))
	print("cosinus wynosi(%f)%f" % (x,np.cos(x)))
	print("tangens wynosi(%f)%f" % (x,np.tan(x)))
	print("cotangens wynosi(%f)%f" % (x,1.0/np.tan(x)))

def Rownanie_Kwadratowe():
	print("Rowanie kwardatowe ver 3.0\nax^2+bx+c")
	a = input("Podaj wspolczynnik rowniania a: ")
	b = input("Podaj wspolczynnik rowniania b: ")
	c = input("Podaj wspolczynnik rowniania c: ")
	if a == b == c == 0:
		print("a, b, c = 0 - brak rownania")
	else:
		print("Sprawdzam parametr a",)
		if a > 0 or a < 0:
			print("> 0\nRownanie typu ax^2+bx+c")
			delta = 4 * a * c - (b**2)
			print("Delta = %d" % (delta))
			if delta == 0:
				x0=(b*b/4*a)
				print("Delta=0, obliczam x=%d" % (x0))
			elif delta > 0:
				x1=(b*b-sqrt(delta)/4*a)
				x2=(b*b+sqrt(delta)/4*a)
				print("Obliczam x1,x2: x1=%d ; x2=%d" % (x1, x2))
			elif delta < 0:
				print("Delta<0 brak pierwiastkow")
		elif a == 0:
			print(" = 0 \n Rownanie typu bx+c")
			x=(-c/b)
			print("Wynik x=-%d/%d" % (c, b))
	print("Koniec")


 
#Wypisz kolejne liczby ciagu Fibonacciego
def fib(numbers):
	numbers =[0,1] #zdefiniuj dwa pierwsze wyrazy ciagu F(0) = 0, F(1) = 1
	new = 0
	for i in range(50):                  #dla kolejnych 50 liczb z ciagu fibonnaciego
		new = numbers[-1] + numbers[-2]  #oblicz kolejny wyraz ciagu jako sume dwoch ostatnich
		numbers.append(new)              #dodaj nowy wyraz ciagu do listy
		print new
		time.sleep(0.1)

while True:
	Kalkulator()
	print('\t' '\033[96m'"==================WYBIERZ OPCJE======================")
	time.sleep(0.1)
	print('\t' '\033[0m'"==================1 - DODAWANIE======================")
	time.sleep(0.1)
	print('\t'  "==================2 - ODEJMOWANIE====================")
	time.sleep(0.1)
	print('\t'  "==================3 - MNOZENIE=======================")
	time.sleep(0.1)
	print('\t'  "==================4 - DZIELENIE======================")
	time.sleep(0.1)
	print('\t'  "==================5 - POTEGOWANIE====================")
	time.sleep(0.1)
	print('\t'  "==================6 - POLE TROJKATA ROWNOBOCZNEGO====")
	time.sleep(0.1)
	print('\t'  "==================7 - PIERWIASTKOWANIE===============")
	time.sleep(0.1)
	print('\t'  "==================8 - TWIERDZENIE PITAGORASA=========")
	time.sleep(0.1)
	print('\t'  "==================9 - NAJWIEKSZA WSPOLNA WIELOKROTNOSC")
	time.sleep(0.1)
	print('\t'  "==================10 - POLE PROSTOKATA===============")
	time.sleep(0.1)
	print('\t'  "==================11 - POLE KWADRATU=================")
	time.sleep(0.1)
	print('\t'  "==================12 - ROWNANIE KWADRATOWE===========")
	time.sleep(0.1)
	print('\t'  "==================13 - FUNKCJE TRYGONOMETRYCZNE======")
	time.sleep(0.1)
	print('\t'  "==================14 - POLE I OBWOD ROMBU============")
	time.sleep(0.1)
	print('\t'  "==================15 - CIAG FIBONACCIEGO=============")
	time.sleep(0.1)
	print('\t'  "==================16 - WYJSCIE=======================")
	wybor = raw_input(" \033[96m wybierz opcje -> ")
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
		odp = poleprostokata()
	elif wybor == "11": 
		odp = polekwadratu()
	elif wybor == "12":
		odp = Rownanie_Kwadratowe()
	elif wybor == "13":
		odp = funkcje_trygonometryczne()
	elif wybor == "14": 
		odp = pole_rombu()
	elif wybor == "15": 
		odp = fib(50)
	elif wybor == "16":
		print('\033[91m' "Wychodzenie...")
		time.sleep(4)
		sys.exit(0)
	elif wybor != "16":
		print('\033[91m' "Nic nie wybrales Wybrales zla opcje lub wpisales zero")
	else: 
		print('\033[91m' "Nie wiem o co ci chodzi.Sprobuj ponownie!")
