import mingus.core.notes as notes
import mingus.core.meter as meter
from mingus.containers.instrument import Instrument, Piano
from mingus.containers import Track
from mingus.containers import Note
from mingus.containers import Bar
import mingus.extra.lilypond as lilypond
import random

b = Bar()
t = Track(Piano())
for x in range(0,10):
    randoct = random.randint(3,6)    #
    nint = random.randint(0,11)
    r = random.randint(0,2)    #for augmenting and diminishing later...
    nstr = notes.int_to_note(nint)
    nstr = Note(nstr, randoct)
    print(nstr)
    b + nstr
    t.add_bar(b)
#bar = lilypond.from_Bar(b)
track = lilypond.from_Track(t)
lilypond.to_png(track, "my_first_track")
