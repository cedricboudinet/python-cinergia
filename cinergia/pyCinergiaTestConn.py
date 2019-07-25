#!/usr/bin/env python
import argparse
import cinergia.client
parser = argparse.ArgumentParser(description='Connection test')
parser.add_argument('target_IP_address', metavar='IP', type=str, nargs='+',
                    help='an integer for the accumulator')

args = parser.parse_args()

cinergiaClient = cinergia.client.CinergiaClient(args.target_IP_address)
try:
    cinergiaClient.connect()
except:
    print("Cannot connect to target")
