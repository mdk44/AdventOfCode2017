# Day 4

# input_file = 'Day 04\\Day 4 Test.txt'
input_file = 'Day 04\\Day 4 Input.txt'

text_file = open(input_file)
lines = text_file.read().split('\n')

passcodes = []
for line in lines:
    text = line.split(' ')
    passcodes.append(text)

valid = True
sum1 = 0
sum2 = 0
# Part 1
for passcode in passcodes:
    valid = True
    for i in range(0,len(passcode)):
        for j in range(i+1,len(passcode)):
            if passcode[i] == passcode[j]:
                valid = False
    if valid == True:
        sum1 += 1

# Part 2
for passcode in passcodes:
    if len(set(''.join(sorted(val)) for val in passcode)) == len(passcode):
        sum2 += 1

print 'Part 1: ' + str(sum1)
print 'Part 2: ' + str(sum2)