example='''abc

a
b
c

ab
ac

a
a
a
a

b'''

def countGroupUniqA(Input):
    Input = Input.split("\n\n")
    final = []
    for g in Input:
        final.append(g.split("\n"))    
    ansSum = 0
    for g in final:
        unique = []
        answers = []
        ganswers = []
        if(len(g)==1):
            for p in g:
                for a in p:
                    if(a not in unique):
                        unique.append(a)
            ansSum += len(unique)
        else:
            for idx,p in enumerate(g):
                if(idx == 0):
                    for a in p:
                        for l in a:
                            answers.append(l)
                else:
                    for a in p:
                        for l in a:
                            if(l in answers):
                                answers.append(l)
                            if(answers.count(l) == len(g)):
                                ansSum += 1
    print(ansSum)

countGroupUniqA(example)
