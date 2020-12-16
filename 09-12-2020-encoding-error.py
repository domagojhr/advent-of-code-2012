#Task https://adventofcode.com/2020/day/9

Input="""35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

def parseInput(i):
    return([int(n) for n in i.split("\n")])

somearray = parseInput(Input)

def preambule(arr,size):
    for idx,n in enumerate(arr):
        if(idx+1>size):
            pairsums = []
            for i in arr[idx-size:idx+1]:
                for j in arr[idx-size:idx+1]:
                    if i+j not in pairsums:
                        pairsums.append(i+j)
            if(int(arr[idx+1]) not in pairsums):
                return int(arr[idx+1])

print("1st part:",preambule(parseInput(Input),5))

def findNumbers(invalid_num,arr,):
    numbers = []
    total = 0
    for i,a in enumerate(arr):
        numbers.append(a)
        total = sum(numbers)
        while(total > invalid_num and len(numbers)>0):
            numbers.pop(0)
            total = sum(numbers)
            if(total == invalid_num):
                return min(numbers),max(numbers),"Sum:",min(numbers)+max(numbers)

#Change 5 to your prefered size of preamble
print("2nd part:",findNumbers(preambule(parseInput(Input),5),parseInput(Input)))
