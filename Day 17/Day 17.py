step_test = 3
step = 343
spins = 2017
spins_p2 = 50000000

def insertion(inp, step, cur_pos):
    for i in range(0, step):
        if cur_pos + 1 == len(buffer):
            cur_pos = 0
        else:
            cur_pos += 1
    cur_pos += 1
    buffer.insert(cur_pos, inp)
    return cur_pos

def spin_lock(step, spins):
    cur_pos = 0
    for i in range(1, spins + 1):
        cur_pos = insertion(i, step, cur_pos)
    return buffer[cur_pos + 1]

def spin_lock_zero(step, spins):
    cur_pos = 0
    for i in range(1, spins + 1):
        cur_pos = (cur_pos + step) % i + 1
        if cur_pos == 1:
            ans = i
    return ans

buffer = []
buffer.append(0)
print("P1 Test: " + str(spin_lock(step_test, spins))) # Correct

buffer = []
buffer.append(0)
print("Part 1: " + str(spin_lock(step, spins))) # Correct

print("Part 2: " + str(spin_lock_zero(step, spins_p2)))