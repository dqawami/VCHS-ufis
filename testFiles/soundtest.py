import os
import sys
from time import sleep

os.system('amixer sset PCM 1%')
while True:
    try:
        os.system('omxplayer -o both ufis.mp3')
        sleep(0.1)
    except KeyboardInterrupt:
       sys.exit(0)
