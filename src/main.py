#!/usr/bin/python

import sys
import salt_event_forwarder

if (len(sys.argv) != 3):
  print "Usage: main.py <Salt-api-event-url> <sumologic-hosted-collector-url>"
else:
  f = salt_event_forwarder.SaltEventForwarder(sys.argv[1], sys.argv[2])
  f.run()