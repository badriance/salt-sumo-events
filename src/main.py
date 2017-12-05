#!/usr/bin/python

import argparse
import salt_event_forwarder

parser = argparse.ArgumentParser(description='Salt-Api event forwarding to SumoLogic')
parser.add_argument('salt_api_event_url', help='URL for your Salt API event end point')
parser.add_argument('sumologic_hosted_collector_url', help='URL for your sumologic hosted collector')
parser.add_argument('--ignore_ssl', action='store_true', help='Ignore any SSL complaints with HTTPS connections')
parser.add_argument('--print_only', action='store_true', help='Do not send anything to sumologic, only print output to console')
parser.add_argument('--quiet', action='store_true', help='Do not print output to console')

args = parser.parse_args()

f = salt_event_forwarder.SaltEventForwarder(args.salt_api_event_url, args.sumologic_hosted_collector_url, args.ignore_ssl, args.quiet, args.print_only)
f.run()