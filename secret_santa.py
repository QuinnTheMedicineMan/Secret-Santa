#!/usr/bin/env python

import random
import time
import argparse
import sys


def secret_santa(guestlist):

    success = False
    random.seed(time.time())    # Seed the random number generator with the time

    while not success:
        success = True

        hat    = guestlist[0:]  # Put all the guests in the hat
        santas = {}             # Output dictionary {Giver:Receiver}

        for santa in guestlist:
            if hat == [santa]:  # If the last person left in the hat is yourself start again
                success = False
                break

            present_receiver = random.choice([guest for guest in hat if guest != santa])    # Pick someone from the hat who isn't you
            hat.remove(present_receiver)                                                    # Once you've picked someone remove them from hat
            santas.update({santa:present_receiver})

    return santas


def main(argv):

    zap = argparse.ArgumentParser()

    zap.add_argument('-f', '--inputFile', type=str, required=True)
    zap.add_argument('-d', '--debug', action='store_true')

    args = zap.parse_args()

    inputFile = open(args.inputFile)
    debug     = args.debug
    guestlist = []

    for name in inputFile:
        name = name.strip()
        if name != "":
            guestlist.append(name)

    santas = secret_santa(guestlist)

    for key in santas.keys():
        if debug:                                   # Just dump all the names on the screen if I'm testing
            print key + " -> " + santas[key]
        else:
            outputFile = open(key + ".txt", 'w')    # Otherwise put the info in .txt files and don't look at them
            outputFile.write(key + ", you should buy a present for " + santas[key] + ".")
            outputFile.close()

if __name__ == "__main__":
    main(sys.argv)
