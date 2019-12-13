filepath = 'inputs/day6.txt'
relations = []
with open(filepath) as fp:
    line = fp.readline().rstrip()
    while line:
        relations.append(line)
        line = fp.readline().rstrip()

class Satellite:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
        self.childcount = 0

    def addChild(self, child):
        self.children.append(child)
        self.childcount += 1

    def setParent(self, parent):
        self.parent = parent

    def getName(self):
        return self.name
    
    def getParentName(self):
        if self.parent:
            return self.parent.getName()
        return str(None)

    def getChildCount(self):
        return self.childcount

    def getTotalChildCount(self):
        total = self.childcount
        for child in self.children:
            total += child.getTotalChildCount()
        return total

    def getDistanceTo(self, target, travel=0, last=None):
        #print("Looking for", target.getName(), " in ", self.getName())
        #print("Children: ", [child.getName() for child in self.children])
        #print("Parent:", self.parent.getName() if self.parent else None)
        #print("")
        if target in self.children or target == self.parent:
            return travel - 1
        else:
            fullTravel = 0
            for child in self.children:
                if child != last:
                    fullTravel += child.getDistanceTo(target, travel + 1, self)
            if self.parent != last and self.parent:
                fullTravel += self.parent.getDistanceTo(target, travel + 1, self)
            if len(self.children) == 0 and not self.parent:
                return 0
        return fullTravel
        


    def __str__(self):
        return "Object: " + self.name + ", Children: " + str(self.childcount) + ", Parent: " + self.getParentName()


satellites = {}
# Init all satellites
for relation in relations:
    for sat in relation.split(')'):
        if sat not in satellites:
            satellites[sat] = Satellite(sat)
for relation in relations:
    [sat1, sat2] = relation.split(')')
    satellites[sat1].addChild(satellites[sat2])
    satellites[sat2].setParent(satellites[sat1])
        

totalChildren = 0
for key in satellites:
    totalChildren += satellites[key].getTotalChildCount()
print(totalChildren)
print(satellites['YOU'].getDistanceTo(satellites['SAN']))


