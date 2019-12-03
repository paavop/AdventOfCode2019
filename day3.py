import re
import operator
filepath = 'inputs/day3.txt'

with open(filepath) as fp:
    line = fp.readline().rstrip()
    movelist1 = line.split(",")
    line = fp.readline().rstrip()
    movelist2 = line.split(",")


def moves_to_coords(movelist):
    coordlist = []
    coord = (0, 0)
    for move in movelist:
        [direction, distance] = (re.split('(\d.*)', move)[:2])
        if direction == 'R':
            dircoord = (1, 0)
        elif direction == 'L':
            dircoord = (-1, 0)
        elif direction == 'U':
            dircoord = (0, 1)
        elif direction == 'D':
            dircoord = (0, -1)

        for step in range(int(distance)):
            coord = tuple(map(operator.add, coord, dircoord))
            coordlist.append(coord)
    return coordlist

def manhattan_distance(tuple1, tuple2):
    return (abs(tuple1[0]-tuple2[0])+abs(tuple1[1]-tuple2[1]))

# Step 1 Manhattan distance
coordlist1 = moves_to_coords(movelist1)
coordlist2 = moves_to_coords(movelist2)
matches = set(coordlist1).intersection(coordlist2)
shortest = 9999999999
for match in matches:
    dist = manhattan_distance((0,0), match)
    if dist < shortest:
        shortest = dist
print(shortest)
# Step 2 Distance travelled
shortest = 9999999999
for match in matches:
    dist = coordlist1.index(match) + coordlist2.index(match) + 2
    if dist < shortest:
        shortest = dist
print(shortest)
