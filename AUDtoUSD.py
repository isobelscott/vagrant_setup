#!/usr/bin/env python

import sys

def main():

    aud = float(input("Enter cost in AUD: "))
    usd = float(aud * 0.77006)
    print("You have spent $" + str(round(usd, 2)) + " USD")

if __name__ == "__main__": 
    main()
