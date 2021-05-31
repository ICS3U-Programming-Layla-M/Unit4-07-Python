#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: May 31, 2021
# This programs displays all numbers from 1000 to 2000, 5 on each line

import constants


def main():
    for counter in range(constants.MIN_NUM, constants.MAX_NUM + 1):
        # checks if number after counter is a multiple of 5
        # if so it will go to the next line once the number is outputted
        if ((counter + 1) % 5 == 0):
            print(counter)
        else:
            # if the number after the counter is not a multiple of 5,
            # the program will continue to display numbers on the same line
            print(counter, end=" ")


if __name__ == "__main__":
    main()
