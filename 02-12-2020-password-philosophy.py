#Task https://adventofcode.com/2020/day/2

inputExample = [['2-3','r','rrnr'],
['5-10','n','ltnnnknnvcnnn'],
['7-9','p','jtpptpllpj'],
['2-5','s','slssssszssssssss'],
['16-17','d','dddddddddddddddlp'],
['2-5','q','bbwqqbkmdhqmjhn'],
['7-10','m','qmpgmmsmmmmkmmkj'],
['1-3','a','abcde'],
['4-7','g','vczggdgbgxgg']]

def getValidPasswords(inputL):
    validPasswords = 0
    for row in inputL:
        ic = 0
        rule = row[0].split('-')
        #client has a last minute change request
        #occurence = row[2].count(row[1])
        #if occurence >= int(rule[0]) and occurence <= int(rule[1]):
        #    validPasswords += 1
        for idx, c in enumerate(row[2]):
            if(row[1] == c):
                if(idx == int(rule[0])-1):
                    ic += 1
                if(idx == int(rule[1])-1):
                    ic += 1
        if(ic == 1):
            validPasswords += 1
    return validPasswords

print(getValidPasswords(inputExample))
