#!/usr/bin/python

import math
import sys

number = raw_input("Podaj liczbe do spierwiastkowania\n")
float_number = float(number)
if len(number) != 0: 
	print '\033[93m' "Wpisales zero lub nic nie wpisales"
	sys.exit()

print ("Pierwiastek liczby to: " + str(math.sqrt(float_number)))
