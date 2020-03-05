import re
input_file = 'Day 16\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split(',')

prog = []
# lines = ['s1', 'x3/4', 'pe/b']
# for i in range(0, 5):
#     prog.append(chr(i + 97))
for i in range(0, 16):
    prog.append(chr(i + 97))


def s(prog, inp):
    numbers = re.findall(r"\d+",inp)
    spots = len(prog) - int(numbers[0])
    new_prog = []
    for i in range(spots, len(prog)):
        new_prog.append(prog[i])
    for i in range(0, spots):
        new_prog.append(prog[i])
    return new_prog

def x(prog, inp):
    numbers = re.findall(r"\d+",inp)
    spot1 = int(numbers[0])
    spot2 = int(numbers[1])
    let1 = prog[spot1]
    let2 = prog[spot2]
    prog[spot1] = let2
    prog[spot2] = let1
    return prog

def p(prog, inp):
    let1 = inp[1]
    let2 = inp[3]
    spot1 = prog.index(let1)
    spot2 = prog.index(let2)
    prog[spot1] = let2
    prog[spot2] = let1
    return prog

def part1(prog, lines):
    for line in lines:
        if line[0] == 's':
            prog = s(prog, line)
        elif line[0] == 'x':
            prog = x(prog, line)
        elif line[0] == 'p':
            prog = p(prog, line)
    outp = ''
    for i in prog:
        outp += i
    return outp

def part2(prog, lines):
    i = 0
    inp = part1(prog, lines)
    new_prog = []
    for j in inp:
        new_prog.append(j)
    while i < 159:
        inp = part1(new_prog, lines)
        new_prog = []
        for j in inp:
            new_prog.append(j)
        i += 1
    outp = ''
    for o in new_prog:
        outp += o
    return outp
    # Manually checking outputs, it starts repeating the cycle every 60 dances.  At dance # 160 (i = 159), our output would match i = 999999999



print("Part 1: " + part1(prog, lines)) # Correct!

prog = []
for i in range(0, 16):
    prog.append(chr(i + 97))

print("Part 2: " + part2(prog, lines)) # Correct!
