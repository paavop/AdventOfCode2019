filepath = 'inputs/day1.txt'
module_weights = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        module_weights.append(int(line))
        line = fp.readline()

def count_fuel(weight):
    return int((int(weight)/3) - 2)

# Step 1
fuelsum = 0
for module in module_weights:
    fuelsum += count_fuel(module)
print(fuelsum)

# Step 2

def count_fuel_recursive(weight):
    fuel_addition = count_fuel(weight)
    if (fuel_addition <= 0):
        return 0
    return fuel_addition + count_fuel_recursive(fuel_addition)

fuelsum = 0
for module in module_weights:
    fuelsum += count_fuel_recursive(module)
print(fuelsum)

