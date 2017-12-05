#!/usr/bin/python

import sys
import salt_event_forwarder

if (len(sys.argv) < 3 or len(sys.argv) > 4):
  print "Usage: main.py <Salt-api-event-url> <sumologic-hosted-collector-url> [--ignore-ssl]"
else:
  f = salt_event_forwarder.SaltEventForwarder(sys.argv[1], sys.argv[2], len(sys.argv) == 4 and sys.argv[3] == "--ignore-ssl")
  f.run()