# Day 2
import re

# input_file = 'Day 2\\Day 2 Test.txt'
input_file = 'Day 2\\Day 2 Input.txt'

text_file = open(input_file)
lines = text_file.read().split('\n')

sheet_rows = []
for line in lines:
    numbers = re.findall(r"\d+",line)
    sheet_rows.append(numbers)

# Part 1
checksum = 0
row_max = 0
row_min = 1000000
for sheet_row in sheet_rows:
    for i in range(0,len(sheet_row)):
        if int(sheet_row[i]) > row_max:
            row_max = int(sheet_row[i])
        if int(sheet_row[i]) < row_min:
            row_min = int(sheet_row[i])
    checksum = checksum + row_max - row_min
    row_max = 0
    row_min = 1000000

print 'Part 1: ' + str(checksum)