#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : October 2019
# This program calculates if the year is a leap year


def main():
    # this function calculates if it is a leap year

    # input
    year = int(input("Enter Year: "))

    # Process & Output
    if year % 4 == 0 and year % 100 != 0:
        print(year, "it is a Leap Year")
    elif year % 100 == 0:
        print(year, "it is a common year")
    elif year % 400 == 0:
        print(year, "it is a Leap Year")
    else:
        print(year, "it is a common year")


if __name__ == "__main__":
    main()
