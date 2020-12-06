#Task https://adventofcode.com/2020/day/4

inputbatch = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''

requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def checkFieldRules(p,v):
    if(p == "byr"):
        if(len(v) == 4 and int(v)>=1920 and int(v)<=2002):
            return True
    
    if(p == "iyr"):
        if(len(v) == 4 and int(v)>=2010 and int(v)<=2020):
            return True
    
    if(p == "eyr"):
        if(len(v) == 4 and int(v)>=2020 and int(v)<=2030):
            return True
    
    if(p == "hgt" and (v[-2:] in ["cm","in"])):
        if(v[-2:] == "cm" and (int(v[:-2])>=150) and (int(v[:-2])<=193)):
            return True
        if(v[-2:] == "in" and (int(v[:-2])>=59) and (int(v[:-2])<=76)):
            return True
    if(p == "hcl" and v[0] == "#" and len(v) == 7):
        hex_digits = set("0123456789abcdef")
        for char in v[1:]:
            if not (char in hex_digits):
                return False
            return True
    if(p == "ecl" and v in ["amb","blu","brn","gry","grn","hzl","oth"]):
        return True
    if(p == "pid" and len(v)==9 and v.isnumeric()):
        return True

def checkPassports(inputbatch,requiredFields):
    inputarray = inputbatch.split("\n\n")
    vp = 0
    for passport in inputarray:
        foundFields = []
        validateFields = []
        cleanPassport = (passport.replace("\n"," ")).split(" ")
        for property in cleanPassport:
            foundFields.append(property[:3])
        rc = 0
        for req in requiredFields:
            if req in foundFields:
                rc += 1
            if rc == len(requiredFields):
                for property in cleanPassport:
                    validateFields.append([property[:3],property[4:]])
                vf = 0
                for field in validateFields:
                    if(checkFieldRules(field[0],field[1])):
                        vf += 1
                if(vf == len(requiredFields)):
                    vp += 1
                
    return(vp)

print(checkPassports(inputbatch,requiredFields))
