# Day3: https://adventofcode.com/2020/day/3

example_input = """..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#"""



#Part 1:

with open('/Users/work/Documents/AdventOfCode2020/Inputs/day3_input.txt') as f:
    tree_matrix = f.read().split('\n')


def checkTree(x,y,cols,trees_matrix,tree_count):
    if trees_matrix[x][y%cols] == '#':
        tree_count += 1
    return tree_count

def loop(right, down):
    rows = len(tree_matrix) 
    cols = len(tree_matrix[0]) 
    x,y = 0,0
    tree_count = 0

    for i in range(rows-down):
        try:
            x,y = x+down, y+right
            # print(x,y)
            tree_count = checkTree(x,y,cols,tree_matrix,tree_count)
            # print(tree_count)
        except:
            break
    return tree_count


print(loop(3,1))


# Part 2 :

print(loop(1,1)*loop(3,1)*loop(5,1)*loop(7,1)*loop(1,2))

#123