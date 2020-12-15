#Task https://adventofcode.com/2020/day/7

import re

Input = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

def executeDaySeven(ourbag,part):
    regex = r"([0-9]+)(?:\ )([a-z\ ]+)(?:(\ bag)s{0,1})"

    rules = Input.split("\n")
    bags = {}
    nestedList = []
    colors = {}
    for rule in rules:
        formatedBag = rule.split(" bags contain ")
        # List empty bags
        if(formatedBag[1] == 'no other bags.' and formatedBag[0] not in bags):
            bags[formatedBag[0]] = {}
        # Create a dictionary of all bags
        else:
            bags[formatedBag[0]] = {}
            nestedBags = re.finditer(regex, formatedBag[1])
            for matchNum, match in enumerate(nestedBags, start=1):
                for gNumber in range(0, len(match.groups())):
                    gNumber = gNumber + 1
                    if(gNumber < 2):
                        bags[formatedBag[0]][match.group(2)] = match.group(1)
    # After all bags are listed in dict
    for entry in bags:    
        if(ourbag in bags[entry]):
            nestedList.append(entry)
            colors[entry] = {}
    new = 0
    last = len(colors)
    # After first stage of check is done (to the 2nd level) check all levels unitl there is no new parents to list
    while(new != last):
        last = new
        for entry in bags:
            for nested in bags[entry]:
                if nested in nestedList:
                    colors[entry] = {}
                    nestedList.append(entry)
                    new = len(colors)
    print("Part1: There are",len(colors),"bag colors that can eventually contain at least one",ourbag)
    if(part == True):
        iterate = 0
        total = 0
        while(iterate != -1):
            if(iterate == 0):
                parentLevel = []
                parentAdvanced = []
                #First level
                for bag in bags[ourbag]:
                    parentAdvanced.append([bag,bags[ourbag][bag]])
                    total += int(bags[ourbag][bag])
            if(iterate > 0):
                newLevelAdvanced = []
                #Other levels
                for parent in parentAdvanced:
                    for bag in bags[parent[0]]:
                        total += int(bags[parent[0]][bag])*int(parent[1])
                        newLevelAdvanced.append([bag,int(bags[parent[0]][bag])*int(parent[1])])
                parentAdvanced = []
                for previous in newLevelAdvanced:
                    parentAdvanced.append(previous)
                if(len(newLevelAdvanced) == 0):
                    iterate = -1
            if iterate != -1:
                iterate += 1
        print("Part2: There are",total,"individual bags required inside",ourbag)

executeDaySeven("shiny gold",True)
