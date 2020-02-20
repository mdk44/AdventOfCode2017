import re
import itertools

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

def return_weight():
    total_weight = dict()
    for tree in weight:
        total_weight[tree] = weight[tree]
        if tree in branches:
            for branch in branches[tree]:
                total_weight[tree] += weight[branch]
    return total_weight

def find_mismatch(tree):
    total_weight = return_weight()
    if tree in branches:
        for a, b in itertools.combinations(branches[tree], 2):
            if total_weight[a] != total_weight[b]:
                return branches[tree]

def find_bad_branch(tree):
    total_weight = return_weight()
    branch = find_mismatch(tree)
    for b in branch:
        print(total_weight[b])
    
print("Part 1: " + str(return_bottom(branches))) # Correct!
print(find_mismatch('tknk'))
print(find_bad_branch('tknk'))