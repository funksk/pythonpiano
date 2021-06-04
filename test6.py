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
print('prefuckery ', composition)
i = 0
j = 2
li = []
for x in (range(0,len(composition))):
    if (composition[i] == '{' and composition[j] == '{' and composition[j-1] == ' '):
        li.append([i,j])
    i+=1
    j+=1

#print(i, j)
print(f'li = {li}')
#the reason for the +(13*x) is because 13 is the amount of space that the string adds, and we need to add it to
#the end of the file anyways. however many times we have instruments or it is triggered, we must add it there.
#indexing issue
for x in range(0,len(li)):
   composition = composition[:li[x][0]+(13*x)] + "{ \clef bass " + composition[li[x][1]+(13*x):] 
print('postfuckery', composition)

print('***********<lilypond starting>************')
lilypond.to_png(composition, "test")
print('*********<nomacs starting>*********')
os.system('nomacs test.png')
