#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on: Nov 2019
# This program uses user defined functions


def calculate_triangle_area(base, height):
    # calculate area

    # process
    area = (base * height) / 2

    # output
    print("The area of the triangle is: {0} cm²".format(area))


def main():
    # This checks if input is an integer, then calls function

    # Input
    input_1 = input("Enter the base of the triangle: ")
    input_2 = input("Enter the height of the triangle: ")
    print("")
    try:
        base_triangle = int(input_1)
        height_triangle = int(input_2)
        # call functions
        calculate_triangle_area(base_triangle, height_triangle)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
