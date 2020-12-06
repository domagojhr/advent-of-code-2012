#Task https://adventofcode.com/2020/day/1

Example = '''1721
979
366
299
675
1456'''

def multiplyEntries(Input,N):
    #use N for two or three numbers (part 1 or part 2 of the task)
    Input = Input.split("\n")
    for x,entry in enumerate(Input):
        for y,second in enumerate(Input):
            if(N == 2):
                if(x!=y and (int(second)+int(entry)) == 2020):
                    return int(entry)*int(second)
            if(N == 3):
                for z,third in enumerate(Input):
                    if(x!=y and x!=z and (int(third)+int(second)+int(entry)) == 2020):
                        return int(third)*int(second)*int(entry)

print(multiplyEntries(Example,3))
