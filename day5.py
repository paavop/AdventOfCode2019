import operator

filepath = 'inputs/day5.txt'
with open(filepath) as fp:
    line = fp.readline().rstrip()
    cmdlist_mem = line.split(",")


# Part 1
def solve_with(cmdlist, inputnum):
    ops = {
        "1": operator.add,
        "2": operator.mul,
        "7": operator.lt,
        "8": operator.eq
    }

    index = 0
    while(True):
        cmd = cmdlist[index]
        opcode = str(int(cmd[-2:]))
        if opcode == '99':
            break
        if opcode in ['1', '2', '5', '6', '7', '8']:
            mode1 = '0'
            mode2 = '0'
            if len(cmd) == 3:
                mode1 = cmd[0]
            elif len(cmd) > 3:
                mode1 = cmd[1]
                mode2 = cmd[0]
            if mode1 == '0':
                parameter1 = int(cmdlist[int(cmdlist[index+1])])
            else:
                parameter1 = int(cmdlist[index+1])
            if mode2 == '0':
                print(cmdlist[index+2])
                parameter2 = int(cmdlist[int(cmdlist[index+2])])
            else:
                parameter2 = int(cmdlist[index+2])
            target = int(cmdlist[index+3])
            if opcode == '5':
                if parameter1 != 0:
                    index = parameter2
                else:
                    index += 3
            elif opcode == '6':
                if parameter1 == 0:
                    index = parameter2
                else:
                    index += 3
            else:
                operation = ops.get(opcode)
                cmdlist[target] = str(int(operation(parameter1, parameter2)))
                index += 4
        elif opcode == '3':
            cmdlist[int(cmdlist[index+1])] = inputnum
            index += 2
        elif opcode == '4':
            print(cmdlist[int(cmdlist[index + 1])])
            index += 2
            
solve_with(cmdlist_mem.copy(), '1')
solve_with(cmdlist_mem.copy(), '5')
