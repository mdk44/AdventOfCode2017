import re, itertools, collections

# input_file = 'Day 07\\Input.csv'
input_file = 'Day 07\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

weight = dict()
branches = dict()
total_weight = dict()
root = []
for line in lines:
    numbers = re.findall(r"\d+", line)
    tree = line.split(' ')[0]
    weight[tree] = int(numbers[0])
    total_weight[tree] = int(numbers[0])
    if '->' in line:
        new = line.split(' -> ')[1]
        branch = new.split(', ')
        branches[tree] = tuple(branch)
for b in weight:
    if b not in branches:
        root.append(b)

def return_bottom(branches):
    check = True
    for b in branches.keys():
        check = False
        for v in branches.values():
            if b in v:
                check = True
        if check == False:
            return b

def find_mismatch(tree):
    total_weight = return_weight()
    if tree in branches:
        for a, b in itertools.combinations(branches[tree], 2):
            if total_weight[a] != total_weight[b]:
                return branches[tree]

def return_weight(lst):
    nxt = []
    for l in lst:
        for branch in branches:
            if l in branches[branch]:
                if branch not in nxt:
                    nxt.append(branch)
                total_weight[branch] += weight[l]
    return nxt
    
print("Part 1: " + str(return_bottom(branches))) # Correct!

new = return_weight(root)
for n in new:
    print(n, total_weight[n])