# -*- coding: utf-8 -*-

from timeside.core import *
from timeside.decoder import *
from timeside.analyzer import *
from timeside.encoder import *
from timeside.api import *

import sys
if len(sys.argv) > 1:
    source = sys.argv[1]
else:
    import os.path
    source= os.path.join (os.path.dirname(__file__),  "../samples/sweep.wav")

decoder = FileDecoder(source)
print "Creating decoder with id=%s for: %s" % (decoder.id(), source)
decoder.setup()
channels  = decoder.channels()
print 'channels :', channels
samplerate = decoder.samplerate()
nframes = decoder.nframes()

dest1 = "/tmp/test.mp3"
dest2 = "/tmp/test2.mp3"
f = open(dest2,'w')

streaming=True
encoder = Mp3Encoder(dest1, streaming=streaming)
encoder.setup(channels=channels, samplerate=samplerate)

while True:
    buf, eod = encoder.process(*decoder.process())
    if streaming and buf:
        f.write(buf)
    if eod :
        break

f.close()
print encoder.pipe
