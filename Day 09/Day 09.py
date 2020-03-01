input_file = 'Day 09\\Input.csv'
# input_file = 'Day 09\\Test.csv'
text_file = open(input_file)
inp = text_file.read()
test0 = '{}' # 1 group, score = 1
test1 = '{{{}}}' # 3 groups, score = 1 + 2 + 3 = 6
test2 = '{{},{}}' # 3 groups, score = 1 + 2 + 2 = 5
test3 = '{{{},{},{{}}}}' # 6 groups, score = 1 + 2 + 3 + 3 + 3 + 4 = 16
test4 = '{<{},{},{{}}>}' # 1 group
test5 = '{<a>,<a>,<a>,<a>}' # 1 group, score = 1
test6 = '{{<a>},{<a>},{<a>},{<a>}}' # 5 groups
test7 = '{{<!>},{<!>},{<!>},{<a>}}' # 2 groups
test8 = '{{<ab>},{<ab>},{<ab>},{<ab>}}' # Score = 1 + 2 + 2 + 2 + 2 = 9
test9 = '{{<!!>},{<!!>},{<!!>},{<!!>}}' # Score = 1 + 2 + 2 + 2 + 2 = 9
test10 = '{{<a!>},{<a!>},{<a!>},{<ab>}}' # Score = 1 + 2 = 3

inputs = {
    0: test0,
    1: test1,
    2: test2,
    3: test3,
    4: test4,
    5: test5,
    6: test6,
    7: test7,
    8: test8,
    9: test9,
    10: test10,
    11: inp,
}

def count_groups(inp):
    i = 0
    garbage = False
    group = 0
    score = 0
    tot_score = 0
    garb_count = 0
    while i < len(inp):
        if inp[i] == "{":
            if garbage == False:
                score += 1
            else:
                garb_count += 1
            i += 1
        elif inp[i] == "!":
            i += 2
        elif inp[i] == "<":
            if garbage == True:
                garb_count += 1
            garbage = True
            i += 1
        elif inp[i] == ">":
            garbage = False
            i += 1
        elif inp[i] == "}":
            if garbage == False:
                group += 1
                tot_score += score
                score -= 1
            else:
                garb_count += 1
            i += 1
        else:
            if garbage == True:
                garb_count += 1
            i += 1
    return group, tot_score, garb_count

# for i in range(0, 12): # All test groups correct
for i in range(11, 12):
    groups, score, trash = count_groups(inputs[i])
    print("No. Groups: " + str(groups))
    print("Total Score: " + str(score))
    print("Trash: " + str(trash))