#Task https://adventofcode.com/2020/day/5

example = ['BBFFFBBLLR', 'BBFFFFFLRL', 'BFBFFFBLRR', 'FBBFFFFRLL', 'FFBFFFBLRR', 'BFBBBFFLLL', 'BFBBBFFLRR', 'FBBFBBFRLL', 'BFFBFBBLLL', 'BFBFBBFRRR', 'FBFBFFBLLR', 'FFFBBBFRLL', 'BFBBFBBRRR', 'FBFFBFBRRR', 'BFFBFFFLLL', 'FBBBFBFLRR', 'BFBBFBFRLR', 'BFFFFFBRRL', 'BFFBFFFRLR', 'FBBBBBFRLL']

def resolveBoardPass(i,rows,columns):
    resolved = []
    for bpass in i:
        row=list(range(0,rows))
        column=list(range(0,columns))
        for index, l in enumerate(bpass):
            if(index<6):
                splitHalf=int(len(row)/2)
                if l == 'F':
                    row = row[:splitHalf]
                else:
                    #it's B
                    row = row[splitHalf:]
            if(index==6):
                if l == 'F':
                    row = row[0]
                else:
                    #it's B
                    row = row[1]
            if(index>6 and index<9):
                splitHalf=int(len(column)/2)
                if l == 'L':
                    column = column[:splitHalf]
                else:
                    #it's R
                    column = column[splitHalf:]
            if(index == 9):
                if l == 'L':
                    column = column[0]
                else:
                    #it's R
                    column = column[1]
        resolved.append([bpass,row,column,row*8+column])
    return resolved

def getHighestID(l):
    l.sort(key=lambda x: x[3], reverse=True)
    return l[0][3]

def detectMissingSeat(l):
    l.sort(key=lambda x: x[3], reverse=True)
    for i,p in enumerate(l):
        if(abs(l[i][3] - l[i-1][3])>1 and i > 1 and i < len(l)-1):
            return(l[i][3]+1)

print("Highest id:",getHighestID(resolveBoardPass(example,128,8)))
#print("Missing seat id:",detectMissingSeat(resolveBoardPass(example,128,8)))
