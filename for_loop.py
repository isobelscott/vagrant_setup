#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    a_str = sys.argv[1]
    b_str = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    incrementer = 1
    the_range = range(a, b+incrementer, incrementer)

    for i in the_range:
        print("a = " + str(i) + "(b=" + str(b) + ")")

