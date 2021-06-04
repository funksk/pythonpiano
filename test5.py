import os
import mingus.core.notes as notes
from mingus.containers.instrument import Instrument
from mingus.containers import Bar
from mingus.containers import Note
from mingus.containers import Track
import mingus.extra.lilypond as lilypond

i = Instrument()
i.clef = 'bass'

t = Track(i)

b = Bar()
b + Note("C-4")
b + Note("E-3")
b + Note("C-5")
b + Note("G-4")

t+b

track = lilypond.from_Track(t)
track = "{ {\clef bass " + track[4:]
print(track)
lilypond.to_png(track, "test")
os.system('nomacs test.png')
