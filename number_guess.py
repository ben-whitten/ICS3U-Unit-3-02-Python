#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: September 2019
# This is a program which makes you guess a number.

import constants


def main():
    print("")
    print("I am thinking of a number...")

    while True:

        guessed_number = int(input("What do you think it is?: "))

        if guessed_number == constants.ANSWER:
            print("")
            print("You did it, you won!")
            break
        else:
            print("")
            print("Wrong, try again.")


if __name__ == "__main__":
    main()
