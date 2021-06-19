#!/bin/python3
#get the input from the cmd line
#generate what they want
#	right, left or both hands
#	single, two, three, four or five notes (for each hand for now...)
#	in a key or not
#		selected key or random key
#	how many bars?? (set amount right now)
#create lilypond thing
#... what a fucking mess this program is...
#
#TODO
#implement correct bass clef
#make left/right go down the correct path
#implement multiple notes at once
#implement doing this in a key (every time??)
#
import os, sys, getopt
import mingus.core.notes as notes
import mingus.core.meter as meter
from mingus.containers.instrument import Instrument
from mingus.containers import Track
from mingus.containers import Note
from mingus.containers import Bar
from mingus.containers import Composition
import mingus.extra.lilypond as lilypond
import random

class MingusComposition():
	def __init__(self):
		self.rh = Instrument()
		self.lh = Instrument()
		self.nONotes = 0
		self.key = ''
		self.t = Track()
		self.t1 = Track()
		self.c = Composition()
		self.composition = ''

	def makecomp(self):
		self.maketracks()
		print(f'self.rh.name = {self.rh.name}')
		if self.rh.name == 'righthand':
			print("making right hand notes")
			self.c + self.t
		if self.lh.name == 'lefthand':
			print("making left hand notes")
			self.c + self.t1
		self.composition = lilypond.from_Composition(self.c)
		print(f'pre: {self.composition}')
		if (self.lh.name == 'lefthand') or (self.rh.name == 'righthand'):
			print("right and left bass clef")
			self.bassclef(self.composition, 1)
		elif (self.lh.name == 'lefthand') and (self.rh.name != 'righthand'):
			print("only left bass clef")
			self.bassclef(self.composition, 0)
		print(f'post: {self.composition}')



	def maketracks(self):
		for x in range(0,20):
			if self.rh.name == 'righthand':
				b = Bar()
				self.t + self.getbar(b, Note("C",4), Note("C", 6))
			if self.lh.name == 'lefthand':
				b = Bar()
				self.t1 + self.getbar(b, Note("C",2), Note("C",4))

	def getbar(self, b, l, h):
		for x in range(0,4):
			randint = random.randint(int(l),int(h))
			nstr = Note()
			nstr.from_int(randint)
			b + nstr
		return(b)

	def bassclef(self, composition, x):
		i = 0
		j = 2
		li = []

		for x in (range(0,len(composition))):   #we can mess with the string and add bass clef to anything
		    if (composition[i] == '{' and composition[j] == '{' and composition[j-1] == ' '):
		        li.append([i,j])
		    i+=1
		    j+=1
		for x in range(0,len(li)):
			composition = composition[:li[x][0]+(13*x)] + "{ \clef bass " + composition[li[x][1]+(13*x):] 





def processArgs(argv, comp):
	try:
		opts, args = getopt.getopt(argv,'hrlsdc:k:')	#right left single double chord <arg> key <arg>
	except getopt.GetoptError:
		print('test.py -hrlsd -c <# of chords> -k <what key or rand for random>')
		sys.exit(2)
	#parse arguments
	for opt, arg in opts:
		print(f'opt = {opt}, arg = {arg}')
		if opt == 'h':
			print('test.py -hrlsd -c <# of chords> -k <what key or rand for random>')
			sys.exit(2)
		elif opt == '-r':
			comp.rh.name = "righthand"
			print(f'self.rh.name = {comp.rh.name}')
		elif opt == '-l':
			comp.lh.name = "lefthand"
		elif opt == '-s':
			comp.nONotes = 1
		elif opt == '-d':
			comp.nONotes = 2
		elif opt == '-c':
			comp.nONotes = arg
		elif opt == '-k':
			comp.key = arg

	return comp

def main(argv):
	if argv == []:
		print("please enter args")
		exit(2)
	mingcomp = MingusComposition()
	mingcomp = processArgs(argv, mingcomp)
	mingcomp.makecomp()
	lilypond.to_png(mingcomp.composition, "test")
	os.system('nomacs test.png')


if __name__ == '__main__':
	main(sys.argv[1:])