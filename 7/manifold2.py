IN = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

IN = open('input.txt').read()

width =len(IN.splitlines()[0])
beams = ["."] * width
total = 0
subtotal = 0

origins = [0] * width
for line in IN.splitlines():
  if line.count('.') == width:
   continue
  print("".join(str(x).center(1) for x in line))
  for i,v in enumerate(line):
    if v == 'S':
      origins[i] = 1
      break
    if v == '^' and origins[i] > 0:
      origins[i-1] += origins[i]
      origins[i+1] += origins[i]
      origins[i] = 0
  print("".join(str(x).center(1) for x in origins), sum(origins))




#   print("".join(beams), subtotal)
#   print("".join(line), '')
#   subtotal = 0
#   newbeams = ["."]*len(beams)
#   for i,v in enumerate(line):
#     if v == 'S':
#       beams[i] = '|'
#       break
#     if v == '^' and beams[i] == '|':
#       beams[i] = ' '
#       newbeams[i-1] = '|'
#       newbeams[i+1] = '|'

#   # print("".join(newbeams), 'n')
#   for x,v in enumerate(newbeams):
#     # print(v)
#     if v == '|':
#       beams[x] = '|'
#   subtotal += beams.count('|')
#   total += beams.count('|')



#     # if v in 'S' or (v in '|' and beams[i] == '|')]:
#     # beams[i] = '|'

# print(total)
