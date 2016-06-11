#!/usr/bin/python3.5
import copy
import time
import os
import random
import shutil

class Cell(object):
	def __init__(self, alive):
		self._status=alive

	def birth(self):
		self._status=True
		#print("ACellwasborn")

	def death(self):
		self._status=False
		#print("KilledaCell")

	def areYouAlive(self):
		return self._status



def display(spielfeld):
	for lineIndex, line in enumerate(spielfeld):
		ausgabe=""
		for field in line:
				if field.areYouAlive()==True:
					ausgabe+=" O"
				else:
					ausgabe+=" ."
		if lineIndex < 10:
				print("0" + str(lineIndex) + " " + ausgabe)
				continue
		print(str(lineIndex) + " " + ausgabe)

width, length = shutil.get_terminal_size()
width = int((width - 3) / 2)
length -= 2

spielfeld=[]

for i in range(length):
	eineZeile=[]
	for i in range(width):
		if random.randint(1,5) == 1:
			eineZeile.append(Cell(True))
		else:
			eineZeile.append(Cell(False))
	spielfeld.append(eineZeile)

spielfeldNew=copy.deepcopy(spielfeld)



print("Generation 0")
display(spielfeld)

for generation in range(1,101): 
	for lineIndex, line in enumerate(spielfeld):
		if lineIndex == 0 or len(spielfeld)-1 == lineIndex:
				pass
		else:
				for fieldIndex, field in enumerate(line):
					if fieldIndex == 0 or fieldIndex == len(line) -1:
						pass
					else:
						neighbors=0
						for i in range(-1,2):
								for j in range(-1,2):
									if spielfeld[lineIndex+i][fieldIndex+j].areYouAlive() == True:
										neighbors+=1

						if field.areYouAlive()==True:
								neighbors-=1
								if neighbors == 2 or neighbors == 3:
									spielfeldNew[lineIndex][fieldIndex].birth()
#									print("Zelle"+str(lineIndex)+
#												","+
#												str(fieldIndex)+
#												"bleibtamLeben")
								else:
									spielfeldNew[lineIndex][fieldIndex].death()
						else:
								#print("Dead Cell with " + str(neighbors) + " Neighbours")
								#print("Zelle "+str(lineIndex)+", "+str(fieldIndex)+" has "
								#				+ str(neighbors) + " neighbours")
								if neighbors == 3:
									spielfeldNew[lineIndex][fieldIndex].birth()
								#	print("Zelle "+str(lineIndex)+", "+str(fieldIndex)+" was born.")
	
	os.system('clear')
	print("Generation "+str(generation))
	display(spielfeldNew)
	spielfeld=copy.deepcopy(spielfeldNew)
	time.sleep(0.2)
