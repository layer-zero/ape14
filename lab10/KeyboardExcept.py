#!/usr/bin/env python2

import sys
from time import sleep

try:
    sleep(10)
except KeyboardInterrupt:
    print '\nCaught ^C: exiting'
    sys.exit()
