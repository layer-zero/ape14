#!/usr/bin/env python2

from time import sleep

try:
    sleep(10)
except KeyboardInterrupt:
    print '\nCaught ^C: exiting'
