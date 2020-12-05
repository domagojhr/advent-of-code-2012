import math

dummyMap = ['..##.......',
'#...#...#..',
'.#....#..#.',
'..#.#...#.#',
'.#...##..#.',
'..#.##.....',
'.#.#.#....#',
'.#........#',
'#.##...#...',
'#...##....#',
'.#..#...#.#']

patterns = [[1,1],[3,1],[5,1],[7,1],[1,2]]

def start(r,d,myMap):
    collisions=0
    x=0
    updatedMap = []
    rchars = len(someMap[0])
    mapsize = len(someMap)
    expandTimes = math.ceil((mapsize*r)/rchars)
    for row in myMap:
        newrow = row*expandTimes
        updatedMap.append(newrow)
    for l in range(len(updatedMap)):
        if(l > 0 and l%d == 0):
            x+=r
            if(updatedMap[l][x] == '#'):
                collisions+=1
    return collisions

def startExpanded(patterns,myMap):
    result = 1
    for pattern in patterns:
        result = result * start(pattern[0],pattern[1],someMap)
    return result

print(startExpanded(patterns,someMap))
