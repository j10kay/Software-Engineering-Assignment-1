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
    input_file = open("input_file.txt", "r") 
    max_file_line_length = 80
    selected_margins = obtainMargins()
    file_line = input_file.readline()
    printPageHeader()
    extraneous_words = []
    while file_line != "":
        file_line = file_line[:-1]
        file_line = " ".join(extraneous_words) + "  " + file_line
        right_padding = " " * int(selected_margins[0])
        left_padding = " " * int(selected_margins[1])
        available_file_line_length = max_file_line_length - int(selected_margins[0]) - int(selected_margins[1])
        if available_file_line_length - len(file_line) >= 0:
            file_line = right_padding + file_line + left_padding
        else:
            counter = 0
            file_line_words = file_line.split()
            if available_file_line_length - len(file_line_words[0]) >= 0:
                file_line = right_padding + file_line_words[counter] + " "
                available_file_line_length -= (1 + len(file_line_words[counter]))
            else:
                file_line = right_padding
            while available_file_line_length - len(file_line_words[counter]) -1 >= 0:
                counter += 1
                file_line += file_line_words[counter] + " "
                available_file_line_length -= 1 + len(file_line_words[counter])
            file_line += left_padding
            extraneous_words = file_line_words[counter+1:]
        print(file_line)
        file_line = input_file.readline()
    return 

main()
