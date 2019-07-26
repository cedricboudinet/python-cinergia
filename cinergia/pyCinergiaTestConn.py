#!/usr/bin/env python
import argparse
import cinergia.client

def main():
    parser = argparse.ArgumentParser(description='Connection test')
    parser.add_argument('target_IP_address', metavar='IP', type=str)
    args = parser.parse_args()
    print("Trying to connect to %s" % args.target_IP_address)
    cinergiaClient = cinergia.client.CinergiaClient(args.target_IP_address)
    try:
        if not cinergiaClient.connect():
            raise Exception("Modbus error")
        print("Connection succesful")
    except Exception as e:
        print("Cannot connect to target: %s" % str(e))

if __name__=="__main__":
    main()
