
import random


#width = 20
#height = 20

#print a row duh
def printRow(row):
    a = ''.join(row)
    b = ('|' + a + '|')
    return str(b)

#print "roof" of the maze = first row
def printRoofRow(size):
    a = ["__" for i in range(size*2 -1)]
    a[random.randrange(0, (size*2 -1))] = '  '
    b = ('_' + ''.join(a)+'__')
    return str(b)

#print "floor" of the maze = last row
def printFloorRow(size):
    a = ["__" for i in range(size*2 -1)]
    a[random.randrange(0, (size*2 -1))] = '   '
    b = ('|' + ''.join(a)+'|')
    return str(b)

#create empty row (list) from 1 to (width * 2 - 1)
#L[n] = [n +1 , '_'], where n can be either floor, hole or wall
def createRow(size):
    row = sum([[i+1, '_'] for i in range(size * 2)], [])[:-1]
    return row

#place a wall on a random n in list
#all n between walls are the same value so we know length of a segment
def putWall(row):
    startPoint = row[0]
    for i in range(0, len(row)-1, 2):
        row[i] = startPoint
        choice = random.getrandbits(1)
        if(choice):
            row[i+1] = '|'
            startPoint = row[i+2]
    row[len(row)-1] = startPoint
    return row

#put a 1 hole in every segment else it n is floor
#if segment len = 1 then always put hole
def putFloor(row):
    lenSet = 1
    startPoint = 0
    for i in range(0, len(row) - 1, 2):
        if(row[i+2] == row[i]):
            row[i] = '_'
            lenSet+=1
        else:
            row[i] = '_'
            row[random.randrange(startPoint, (startPoint + (lenSet * 2)), 2)] = ' '
            lenSet = 1
            startPoint = i + 2
    row[len(row) - 1] = '_'
    row[random.randrange(startPoint, (startPoint + (lenSet * 2)), 2)] = ' '
    return row

#put everything together and create a random maze

def createMaze(size, width):
    fuck = []
    for i in range(size-1):
        fuck.append(printRow(putFloor(putWall(createRow(width)))) + "+")
    fuck.insert(0, printRoofRow(width) + "+")
    fuck.append(printFloorRow(width))
    print('\n')

    return fuck

