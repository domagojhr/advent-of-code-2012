def choseAdapter(filename):
    with open(filename, "r") as f:
        arr = [int(line.rstrip()) for line in f.readlines()]
    arr.sort()
    current = 0
    ratings = [1,2,3]
    adapters = []
    combs = {0:1}
    for i,v in enumerate(arr):
        if i == 0:
            adapters.append([v,v])
        if v - adapters[len(adapters)-1][0] in ratings:
            if v - adapters[len(adapters)-1][0] == ratings[2]:
                adapters.append([v,ratings[2]])
            elif v - adapters[len(adapters)-1][0] == ratings[1]:
                adapters.append([v,ratings[1]])
            elif v - adapters[len(adapters)-1][0] == ratings[0]:
                adapters.append([v,ratings[0]])
    count = [0,0,1]
    for d in adapters:
        count[(d[1])-1] += 1
    print("Part1 solution:",count[0]*count[2])
    for part in arr:
        combs[part] = 0
        if(part-1 in combs):
            combs[part] += combs[part-1]
        if(part-2 in combs):
            combs[part] += combs[part-2]
        if(part-3 in combs):
            combs[part] += combs[part-3]
    highest = max(combs)
    print("Part2 solution:", combs[highest])

choseAdapter("10input.txt")
