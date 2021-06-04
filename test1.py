import mingus.core.notes as notes
from mingus.containers import Bar
import mingus.extra.lilypond as lilypond
import random

b = Bar()
for x in range(0,10):
    nint = random.randint(0,11)
    r = random.randint(0,2)    #for augmenting and diminishing later...
    nstr = notes.int_to_note(nint)
    print(nstr)
    b + nstr
bar = lilypond.from_Bar(b)
lilypond.to_png(bar, "my_first_bar")
