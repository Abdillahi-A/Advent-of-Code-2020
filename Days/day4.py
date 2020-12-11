# Day 4: https://adventofcode.com/2020/day/4

# Part 1:
def build_list_of_passports(data):
    passports = []
    for j in data:
        d = {}
        person = j.split()
        for k in person:
            key, value = k.split(':')[0], k.split(':')[1]
            d[key] = value
        
        passports.append(d)
    
    return passports


def check_if_passport_is_valid(passports):
    valid = 0
    for i in passports:
        if len(i.keys()) == 8:
            valid +=1
        else:
            if ('cid' not in i.keys() and len(i.keys()) == 7):
                valid +=1

    return valid



# Part 2:

def chech_height(i):
    if i['hgt'][-2:] == 'cm' and 150<=int(i['hgt'][:-2])<=193:
        return True
    
    if i['hgt'][-2:] == 'in' and 59<=int(i['hgt'][:-2])<=76:
        return True

    return False


import re

def full_checks(passports):
    valid = 0
    for i in passports:
        if len(i.keys()) == 8:
             if len(i['byr']) == 4 and 1920<=int(i['byr'])<=2002 and \
                len(i['iyr']) == 4 and 2010<=int(i['iyr'])<=2020 and \
                len(i['eyr']) == 4 and 2020<=int(i['eyr'])<=2030 and \
                chech_height(i) and \
                re.match(r"^#[a-f\d]{6}$", i['hcl']) and \
                i['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
                len(i['pid']) == 9:
                    valid +=1
        else:
            if ('cid' not in i.keys() and len(i.keys()) == 7):
                if len(i['byr']) == 4 and 1920<=int(i['byr'])<=2002 and \
                len(i['iyr']) == 4 and 2010<=int(i['iyr'])<=2020 and \
                len(i['eyr']) == 4 and 2020<=int(i['eyr'])<=2030 and \
                chech_height(i) and \
                re.match(r"^#[a-f\d]{6}$", i['hcl']) and \
                i['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
                len(i['pid']) == 9:
                    valid +=1

    return valid



def main():

    with open('/Users/work/Documents/Advent-of-Code-2020/Inputs/day4_input.txt') as f:
        data = f.read().split('\n\n')

    passports = build_list_of_passports(data)
    valid = check_if_passport_is_valid(passports)
    print(valid)

    print(full_checks(passports))
    


main()
