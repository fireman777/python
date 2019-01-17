#!/usr/bin/env python36

#work with argument parser

import argparse

parser = argparse.ArgumentParser(description='Great Description To Be Here')

parser.add_argument("square", type=int, help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")


args = parser.parse_args()
answer = args.square**2

if args.verbose:
    print("The square of {} = {}.".format(args.square, answer))
else:
    print(answer)
