with open('02\\input.txt') as fp:
    lines = [line.rstrip() for line in fp]

depth = 0
horizontal = 0
for line in lines:
    command = line.split(" ")
    if command[0] == "forward":
        horizontal += int(command[1])
    elif command[0] == "down":
        depth += int(command[1])
    elif command[0] == "up":
        depth -= int(command[1])

print("first: " + str(depth * horizontal))

depth = 0
horizontal = 0
aim = 0
for line in lines:
    command = line.split(" ")
    if command[0] == "forward":
        horizontal += int(command[1])
        depth += aim * int(command[1])
    elif command[0] == "down":
        aim += int(command[1])
    elif command[0] == "up":
        aim -= int(command[1])

print("second: " + str(depth * horizontal))