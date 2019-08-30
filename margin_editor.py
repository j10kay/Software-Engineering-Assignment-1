import os

def obtainMargins():
    left_margin = input("Enter a value for the left margin: ")
    right_margin = input("Enter a value for the right margin: ")
    print()
    return (left_margin, right_margin)

def printPageHeader():
    for index in range(8):
        for number in range(10):
            print(number, end="")
    print()
    return

def main():
    input_ = open("input_file.txt", "r") 
    file_line_length = 80
    selected_margins = obtainMargins()
    file_line = input_.readline()
    right_padding = " " * int(selected_margins[0])
    left_padding = " " * int(selected_margins[1])
    file_line_length = 80 - int(selected_margins[0]) - int(selected_margins[1]) - len(file_line)
    if file_line_length >= 0:
        file_line = right_padding + file_line + left_padding
    else:
        available_line_length = 80 - (int(selected_margins[0]) + int(selected_margins[1]))
        counter = 0
        file_line_words = file_line.split()
        file_line = right_padding + file_line_words[counter] + " "
        available_line_length -= (1 + len(file_line_words[counter]))
        while available_line_length >= 0:
            counter += 1
            file_line += file_line_words[counter] + " "
            available_line_length -= 1 + len(file_line_words[counter])
        file_line += left_padding
    printPageHeader()
    print(file_line)
    print(file_line_length)
    return 

main()
