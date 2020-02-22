import sys, re, itertools, collections

sys.setrecursionlimit(5000)

input_file = 'Day 07\\Input.csv'
# input_file = 'Day 07\\Test.csv'
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

def return_weight(lst):
    nxt = []
    for l in lst:
        for branch in branches:
            if l in branches[branch]:
                if branch not in nxt:
                    nxt.append(branch)
                total_weight[branch] += total_weight[l]
    if 'tknk' not in nxt and 'qibuqqg' not in nxt:
        return_weight(nxt)
    return nxt

def find_mismatch(lst):
    for branch in branches:
        for l in lst:
            if l in branches[branch]:
                for a, b in itertools.combinations(branches[branch], 2):
                    if total_weight[a] != total_weight[b]:
                        return branches[branch]
    
print("Part 1: " + str(return_bottom(branches))) # Correct!

# Part 2
new = return_weight(root)
# new = return_weight(new)
ans = find_mismatch(new)
for a in ans:
    print(a, weight[a], total_weight[a]) # Correct!