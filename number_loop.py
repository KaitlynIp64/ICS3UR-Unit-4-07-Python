#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Nov 2022
# This program prints numbers 1000-2000

import random


def main():

    # process
    value = input("Press [Enter] to print all numbers from 1000 to 2000.")
    for num in range(1000, 2001):
        if num % 5 == 0 and num != 1000:
            print("\n{0} ".format(num), end="")
        else:
            print("{0} ".format(num), end="")
    print("")
    print("\nDone.")


if __name__ == "__main__":
    main()
