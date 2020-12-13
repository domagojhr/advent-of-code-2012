import copy

input='''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''

def parseInput(i):
    inputArray = []
    i = i.split("\n")
    for line in i:
        line = line.split(" ")
        inputArray.append(line)
    return( inputArray)

def returnNextStep(command,accumulator,position,donePositions):
    if(position in donePositions):
        return [accumulator,False,donePositions]
    if(command[0] == "acc"):
        donePositions.append(position)
        accumulator += int(command[1])
        position += 1
        return [accumulator,position,donePositions]
    if(command[0] == "jmp"):
        donePositions.append(position)
        position = position + int(command[1])
        return [accumulator,position,donePositions]
        
    if(command[0] == "nop"):
        donePositions.append(position)
        position += 1
        return [accumulator,position,donePositions]

def executeCode():
    mapCorrupted = []
    fixed = parseInput(input)
    for idx, command in enumerate(fixed):
        if(command[0] in ["jmp","nop"]):
            mapCorrupted.append(idx)
    for ci in mapCorrupted:
        a = 0
        p = 0
        response = [0,0,0]
        donePositions = []
        modCodeArray = copy.deepcopy(fixed)
        dothis = [modCodeArray[0],a,p]
        Done = True
        while(Done):
            if(modCodeArray[ci][0] == "nop"):
                modCodeArray[ci][0] = "jmp"
            if(modCodeArray[ci][0] == "jmp"):
                modCodeArray[ci][0] = "nop"
            response = returnNextStep(dothis[0],dothis[1],dothis[2],donePositions)
            if(response[1] >= len(modCodeArray)):
                return response[0]
            donePositions = response[2]
            dothis = [modCodeArray[response[1]],response[0],response[1]]
            if(response[1] == False):
                Done = False

print("Final accumulator is",executeCode())
