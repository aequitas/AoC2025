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

grid = [list("X"+row+"X") for row in IN.splitlines()]
grid = [list('X'*len(grid[0]))] + grid + [list('X'*len(grid[0]))]

def print_grid(grid):
  for row in grid:
    print("".join(row))

print_grid(grid)

removed = 0
remove = []

prev_removed = 0

while True:
  for y, row in enumerate(grid):
    for x, cell in enumerate(row):
      if cell != '@':
        continue
      print(y,x)
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
        removed += 1
        grid[y][x] = 'r'
        print('removed')
  if removed == prev_removed:
    break
  prev_removed = removed

# for y,x in remove:
#   grid[y][x] = 'r'

print()
print_grid(grid)
print(removed)
