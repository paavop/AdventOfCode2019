import re

filepath = 'inputs/day4.txt'

with open(filepath) as fp:
    line = fp.readline().rstrip()
rangelist = line.split("-")
start = int(rangelist[0])
end = int(rangelist[1])

# Part 1

def two_adjacent(number):
    return bool(re.search(r"(.)\1", str(number)))

def no_decrease(number):
    ref = -1
    decreases = False
    for num in str(number):
        if int(num) < ref:
            decreases = True
        ref = int(num)
    return not decreases


matches = []
for number in range(start, end+1):
    if two_adjacent(number) and no_decrease(number):
        matches.append(number)
print(len(matches))

# Part 2

def only_two_adjacent(number):
    twofound = False
    for match in re.finditer(r"(.)\1+", str(number)):
        if len(match.group()) == 2:
            twofound = True
    return twofound

bettermatches = []
for number in matches:
    if only_two_adjacent(number):
        bettermatches.append(number)
print(len(bettermatches))
