input_file = 'Day 08\\Input.csv'
# input_file = 'Day 08\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

regs = dict()
def read_regs(lines):
    for line in lines:
        inp = line.split(" ")
        inp_reg = inp[0]
        cond_reg = inp[4]
        if inp_reg not in regs:
            regs[inp_reg] = 0
        if cond_reg not in regs:
            regs[cond_reg] = 0

def call_function(line):
    inp = line.split(" ")
    funct = inp[1]
    cond_reg = inp[4]
    cond = inp[5]
    cond_val = int(inp[6])
    funct_return = False
    if cond == '>':
        if regs[cond_reg] > cond_val:
            funct_return = True
    elif cond == '>=':
        if regs[cond_reg] >= cond_val:
            funct_return = True
    elif cond == '<':
        if regs[cond_reg] < cond_val:
            funct_return = True
    elif cond == '<=':
        if regs[cond_reg] <= cond_val:
            funct_return = True
    elif cond == '==':
        if regs[cond_reg] == cond_val:
            funct_return = True
    elif cond == '!=':
        if regs[cond_reg] != cond_val:
            funct_return = True
    if funct_return == True:
        if funct == 'inc':
            return 0
        if funct == 'dec':
            return 1
    else:
        return 99

def inc(reg, val):
    regs[reg] += val
    return True

def dec(reg, val):
    regs[reg] -= val
    return True

def nothing(reg, val):
    return True

options = {
    0: inc,
    1: dec,
    99: nothing,
}

def read_line(line):
    inp = line.split(" ")
    inp_reg = inp[0]
    val = int(inp[2])
    num = call_function(line)
    options[num](inp_reg, val)
    return True

max_val = 0
read_regs(lines)
for line in lines:
    read_line(line)
    if max(regs.values()) > max_val: # For part 2
        max_val = max(regs.values())

print("Part 1: " + str(max(regs.values()))) # Correct!
print("Part 2: " + str(max_val))
