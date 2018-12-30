# Day 5

# input_file = 'Day 05\\Day 5 Test.txt'
input_file = 'Day 05\\Day 5 Input.txt'

text_file = open(input_file)
lines = text_file.read().split('\n')

maze = []
for line in lines:
    maze.append(int(line))

maze2 = []
for line in lines:
    maze2.append(int(line))

# Part 1
curr = 0
step1 = 0
while curr >= 0 and curr < len(maze):
    if maze[curr] == 0:
        maze[curr] += 1
        step1 += 1
    elif maze[curr] != 0:
        maze[curr] += 1
        curr = curr + maze[curr] - 1
        step1 += 1

# Part 2
curr = 0
step2 = 0
while curr >= 0 and curr < len(maze2):
    if maze2[curr] == 0:
        maze2[curr] += 1
        step2 += 1
    elif maze2[curr] >= 3:
        maze2[curr] -= 1
        curr = curr + maze2[curr] + 1
        step2 += 1
    elif maze2[curr] != 0:
        maze2[curr] += 1
        curr = curr + maze2[curr] - 1
        step2 += 1  

print 'Part 1: ' + str(step1)
print 'Part 2: ' + str(step2)