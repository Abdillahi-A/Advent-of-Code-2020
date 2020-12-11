#Question: https://adventofcode.com/2020/day/1

# lst = [1721,979,366,299,675,1456]

#Load input
with open('/Users/work/Documents/AdventOfCode2020/Inputs/day1_input.txt', mode='r') as f:
    lst = [int(i.strip()) for i in f]
    
# Part 1:
def find_sum_2020_part1(lst):
    for i in lst:
        for k in lst:
            if i + k == 2020:
                return i*k

print(find_sum_2020_part1(lst))

# Part 2:
def find_sum_2020_part2(lst):
    for i in lst:
        for k in lst:
            for j in lst:
                if i + k + j == 2020:
                    return i*k*j

print(find_sum_2020_part2(lst))
