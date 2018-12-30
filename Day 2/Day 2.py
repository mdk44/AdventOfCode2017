# Day 2
import re

# input_file = 'Day 2\\Day 2 Test.txt'
# input_file = 'Day 2\\Day 2 Test 2.txt'
input_file = 'Day 2\\Day 2 Input.txt'

text_file = open(input_file)
lines = text_file.read().split('\n')

sheet_rows = []
for line in lines:
    numbers = re.findall(r"\d+",line)
    sheet_rows.append(numbers)

# Part 1
checksum1 = 0
row_max = 0
row_min = 1000000
for sheet_row in sheet_rows:
    for i in range(0,len(sheet_row)):
        if int(sheet_row[i]) > row_max:
            row_max = int(sheet_row[i])
        if int(sheet_row[i]) < row_min:
            row_min = int(sheet_row[i])
    checksum1 = checksum1 + row_max - row_min
    row_max = 0
    row_min = 1000000

# Part 2
checksum2 = 0
num = 0
denom = 0
for sheet_row in sheet_rows:
    for i in range(0,len(sheet_row)):
        for j in range(i,len(sheet_row)):
            if i != j:
                if int(sheet_row[i]) % int(sheet_row[j]) == 0:
                    num = int(sheet_row[i])
                    denom = int(sheet_row[j])
                if int(sheet_row[j]) % int(sheet_row[i]) == 0:
                    denom = int(sheet_row[i])
                    num = int(sheet_row[j])
            
    checksum2 = checksum2 + (num/denom)

print 'Part 1: ' + str(checksum1)
print 'Part 2: ' + str(checksum2)