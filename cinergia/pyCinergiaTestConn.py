#!/usr/bin/env python
import argparse
import cinergia.client
import sys

def main(argsin):
    parser = argparse.ArgumentParser(description='Connection test')
    parser.add_argument('target_IP_address', metavar='IP', type=str)
    parser.add_argument('target_port', metavar='Port', type=int, default=502, nargs='?')
    args = parser.parse_args(argsin)
    print("Trying to connect to %s on port %d" % (args.target_IP_address, args.target_port))
    cinergiaClient = cinergia.client.CinergiaClient(args.target_IP_address, args.target_port)
    try:
        if not cinergiaClient.connect():
            raise Exception("Modbus error")
        print("Connection succesful")
        return 0
    except Exception as e:
        print("Cannot connect to target: %s" % str(e))
        return -1

if __name__=="__main__":
    main(sys.argv[1:])
