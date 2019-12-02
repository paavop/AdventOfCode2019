import operator

filepath = 'inputs/day2.txt'
with open(filepath) as fp:
    line = fp.readline().rstrip()
    cmdlist_mem = line.split(",")


# Part 1
def solve_with(cmd1, cmd2, cmdlist):
    cmdlist[1] = cmd1
    cmdlist[2] = cmd2

    ops = {
        "1": operator.add,
        "2": operator.mul
    }

    index = 0
    while(True):
        cmd = cmdlist[index]
        if cmd == '99':
            break
        operation = ops.get(cmd)
        first = int(cmdlist[index+1])
        second = int(cmdlist[index+2])
        goal = int(cmdlist[index+3])
        cmdlist[goal] = str(operation(int(cmdlist[first]), int(cmdlist[second])))
        index +=4

    return cmdlist[0]

print(solve_with('12', '2', cmdlist_mem.copy()))

# Part 2


def look_for_result(result, cmdlist):
    for i in range(99):
        for j in range(99):
            ans = solve_with(str(i), str(j), cmdlist.copy())
            if ans == result:
                return(100*i+j)

print(look_for_result('19690720', cmdlist_mem))
