import os
import mingus.core.notes as notes
import mingus.core.meter as meter
from mingus.containers.instrument import Instrument, Piano
from mingus.containers import Track
from mingus.containers import Note
from mingus.containers import Bar
from mingus.containers import Composition
import mingus.extra.lilypond as lilypond
import random

c = Composition()
c.set_author('My computer')
c.set_title('first composition')
Bass = Instrument()
Bass.name = "Bass"
Bass.clef = "bass"
Bass.set_range((Note("E-2"),Note("C-4")))
t = Track(Piano)
t1 = Track(Bass)
t1.clef = "bass"

def getbar(b, l, h):
    for y in range(0,4):
        randoct = random.randint(l,h)    #
        nint = random.randint(0,11)
        r = random.randint(0,2)    #for augmenting and diminishing later...
        nstr = notes.int_to_note(nint)
        nstr = Note(nstr, randoct)
#        print(nstr)
        b + nstr
    return(b)

for x in range(0,10):
    b = Bar()
    b1 = Bar()
    getbar(b1, 4,5)
    getbar(b,2,4)
    t + b
    t1 + b1
c + t
c + t1
#bar = lilypond.from_Bar(b)
#track = lilypond.from_Track(t)
composition = lilypond.from_Composition(c)
i = j = 0
while(composition[i] != '{' or j != 2):
    if(composition[i] == '{'):
        j+=1
    i+=1
print(i, j)
print(composition)
composition = composition[:i] + "\clef bass " + composition[i:]
print(composition)
lilypond.to_png(composition, "test")
os.system('nomacs test.png')
