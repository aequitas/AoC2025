IN = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

IN = open("input.txt").read()

grid = ["X"+row+"X" for row in IN.splitlines()]
grid = ['X'*len(grid[0])] + grid + ['X'*len(grid[0])]

def print_grid(grid):
  for row in grid:
    print(row)

# print_grid(grid)

accessible = 0

for y, row in enumerate(grid):
  for x, cell in enumerate(row):
    if cell != '@':
      continue
    # print(y,x)
    rolls = 0
    if grid[y-1][x-1] == '@':
      rolls += 1
    if grid[y-1][x] == '@':
      rolls += 1
    if grid[y-1][x+1] == '@':
      rolls += 1
    if grid[y][x-1] == '@':
      rolls += 1
    # if grid[y-1][x] == '@':
    #   rolls += 1
    if grid[y][x+1] == '@':
      rolls += 1
    if grid[y+1][x-1] == '@':
      rolls += 1
    if grid[y+1][x] == '@':
      rolls += 1
    if grid[y+1][x+1] == '@':
      rolls += 1
    # print(rolls)
    if rolls < 4:
      accessible += 1

print(accessible)
