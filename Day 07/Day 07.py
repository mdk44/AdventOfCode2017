import re

# input_file = 'Day 07\\Input.csv'
input_file = 'Day 07\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

weight = dict()
branches = dict()
for line in lines:
    numbers = re.findall(r"\d+", line)
    tree = line.split(' ')[0]
    weight[tree] = int(numbers[0])
    if '->' in line:
        new = line.split(' -> ')[1]
        branch = new.split(', ')
        branches[tree] = branch

def return_bottom(branches):
    check = True
    for b in branches.keys():
        check = False
        for v in branches.values():
            if b in v:
                check = True
        if check == False:
            return b
                

# def return_weight(lines):
    
print("Part 1: " + str(return_bottom(branches))) # Correct!