
# Question: https://adventofcode.com/2020/day/2#part2

with open('/Users/work/Documents/AdventOfCode2020/Inputs/day2_input.txt') as f:
    input_list= [i.strip() for i in f]


#Part 1

def get_password_policy(input_list):
    password = []
    policy = []
    low_high= []
    low = []
    high = []
    
    for i in input_list:
        password.append(i.split()[-1])
        policy.append(i.split()[1].replace(':',''))
        low_high.append(i.split()[0])
    
    for i in low_high:
        low.append(int(i.split('-')[0]))
        high.append(int(i.split('-')[1]))
        
    return password, policy, low, high


def check_pw_is_valid(password, policy, low, high):

    valid = 0

    for i in range(len(password)):
        if low[i]<=password[i].count(policy[i])<=high[i]:
            valid +=1
    
    return valid

password, policy, low, high = get_password_policy(input_list)


valid = check_pw_is_valid(password, policy, low, high)
print(valid)


# Part 2

def check_pw_is_valid_part_2(password, policy, low, high):
    valid = 0
    for i in range(len(password)):
        if (password[i][low[i]-1] == policy[i] and password[i][high[i]-1] != policy[i]) or (password[i][low[i]-1] != policy[i] and password[i][high[i]-1] == policy[i]):
            valid+=1
    return valid

valid = check_pw_is_valid_part_2(password, policy, low, high) 
print(valid)
