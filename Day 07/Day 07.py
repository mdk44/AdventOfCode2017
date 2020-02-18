import re

input_file = 'Day 07\\Input.csv'
# input_file = 'Day 07\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def return_bottom(lines):
    branches = []
    tree = []
    for line in lines:
        tree.append(line.split(' ')[0])
        if '->' in line:
            new = line.split(' -> ')[1]
            branch = new.split(', ')
            for b in branch:
                branches.append(b)
    for t in tree:
        if t not in branches:
            return t


print("Part 1: " + return_bottom(lines)) # Correct!