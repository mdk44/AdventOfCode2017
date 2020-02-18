import re
test = '0   2   7   0'
actual = '10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6'
numbers_test = re.findall(r"\d+", test)
numbers = re.findall(r"\d+", actual)
inp_test = [int(i) for i in numbers_test]
inp_actual = [int(i) for i in numbers]
inp_p2 = [1, 1, 0, 15, 14, 13, 12, 10, 10, 9, 8, 7, 6, 4, 3, 5]

def find_max(inp):
    num = max(inp)
    for i in range(0, len(inp)):
        if inp[i] == num:
            return num, i

def reallocate(inp):
    num, i = find_max(inp)
    inp[i] = 0
    while num > 0:
        if i + 1 == len(inp):
            i = 0
        else:
            i += 1
        inp[i] += 1
        num -= 1
    return inp

def find_cycles(inp):
    cycles = 0
    banks = []
    new = ''
    for i in range(0, len(inp)):
        new += str(inp[i])
    banks.append(new)
    cont = True
    while cont:
        new = ''
        inp = reallocate(inp)
        cycles += 1
        for i in range(0, len(inp)):
            new += str(inp[i])
        if new in banks:
            cont = False
            return cycles, inp
        else:
            banks.append(new)

print("Test: " + str(find_cycles(inp_test))) # Correct!
print("Part 1: " + str(find_cycles(inp_actual))) # Correct!
print("Part 2: " + str(find_cycles(inp_p2))) # Correct!