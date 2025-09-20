import io
import re
# x = 2
# y = 3
# file = io.open("file.txt", mode="w")
# file.write("One\n")
# file.write("Two\n")
# file.write(f'{x}' + " + " + f'{y}' + " = " + f'{x+y}')
# file.close()

file = io.open("numbers.txt")
for line in file:
    for char in line:
        if char.isdigit():
            print(char)