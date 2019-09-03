import os

def obtainMargins():
    left_margin = input("Enter a value for the left margin: ")
    right_margin = input("Enter a value for the right margin: ")
    print()
    return (left_margin, right_margin)

def printPageHeader(output_file):
    output_file.write("\n") 
    for index in range(8):
        for number in range(10):
            print(number, end="")
            output_file.write(str(number))
    print()
    output_file.write("\n")
    return

def main():
    input_file = open("input_file.txt", "r") 
    output_file = open("output_file.txt","w+")
    max_file_line_length = 80
    selected_margins = obtainMargins()
    file_line = input_file.readline()
    printPageHeader(output_file)
    extraneous_words = []
    extraneous_words_list = [[],[]]
    while file_line != "" or len(extraneous_words) > 3:
        file_line = file_line[:-1]
        if extraneous_words_list[-1] != extraneous_words_list[-2]:
            file_line = " ".join(extraneous_words) + "  " + file_line
        right_padding = " " * int(selected_margins[1])
        left_padding = " " * int(selected_margins[0])
        available_file_line_length = max_file_line_length - int(selected_margins[0]) - int(selected_margins[1])
        if available_file_line_length - len(file_line) >= 0:
            file_line = left_padding + file_line + right_padding
        else:
            counter = 0
            file_line_words = file_line.split()
            if available_file_line_length - len(file_line_words[0]) >= 0:
                file_line = left_padding + file_line_words[counter] + " "
                available_file_line_length -= (1 + len(file_line_words[counter]))
            else:
                file_line = left_padding
            while available_file_line_length - len(file_line_words[counter]) -1 >= 0:
                counter += 1
                available_file_line_length -= 1 + len(file_line_words[counter])
                if available_file_line_length < 0:
                    counter -= 1
                else:
                    file_line += file_line_words[counter] + " "
            file_line += right_padding
            extraneous_words = file_line_words[counter+1:]
        extraneous_words_list.append(extraneous_words)
        print(file_line)
        output_file.write(file_line)
        output_file.write("\n")
        file_line = input_file.readline()
    if extraneous_words_list[-1] == extraneous_words_list[-2]:
       extraneous_words = []
    if (len(extraneous_words) != 0):
        print(left_padding + " ".join(extraneous_words) + " " + right_padding)
        output_file.write(left_padding + " ".join(extraneous_words) + " " + right_padding)
        output_file.write("\n")
    output_file.close()
    return 

main()
