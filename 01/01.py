with open('01\\input.txt') as fp:
    lines = [line.rstrip() for line in fp]

prevNum = 0
count = -1
for line in lines:
    if int(line) > prevNum:
        count += 1
    prevNum = int(line)
print("first: " + str(count))

prevNum = 0
count = -1
for i in range(len(lines)-2):
    newNum = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
    if newNum > prevNum:
        count += 1
    prevNum = newNum
print("second: " + str(count))