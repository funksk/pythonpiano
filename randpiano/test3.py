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
t = Track(Piano)
t1 = Track(Bass)
for x in range(0,10):
    b = Bar()
    for y in range(0,4):
        randoct = random.randint(3,6)    #
        nint = random.randint(0,11)
        r = random.randint(0,2)    #for augmenting and diminishing later...
        nstr = notes.int_to_note(nint)
        nstr = Note(nstr, randoct)
        print(nstr)
        b + nstr
    print(b)
    t + b
    t1 + b
c + t
c + t1
#bar = lilypond.from_Bar(b)
#track = lilypond.from_Track(t)
composition = lilypond.from_Composition(c)
lilypond.to_png(composition, "test")
os.system('nomacs test.png')
