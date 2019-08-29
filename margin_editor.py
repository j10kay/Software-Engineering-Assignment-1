import os

def obtainMargins():
    left_margin = input("Enter a value for the left margin: ")
    right_margin = input("Enter a value for the right margin: ")
    return (left_margin, right_margin)

def printPageHeader():
    for index in range(8):
        for number in range(10):
            print(number, end="")
    print()
    return

def main():
    input = open("input_file.txt", r)
    selected_margins = obtainMargins()
