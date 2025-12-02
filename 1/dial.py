IN = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

IN = open("input.txt").read()

START = 0
END = 99

START_POS = 50

ANSWER = 3

moves = IN.strip().splitlines()

pos = START_POS

zeros = 0

for move in moves:
  if pos == 0:
    zeros += 1
  d,n = move[0], int(move[1:])
  print(pos, d, n)
  if d == 'L':
    pos -= n % (END+1)
    if pos < START:
      pos = END + 1 + pos
  if d == 'R':
    pos += n % (END +1)
    if pos > END:
      pos = pos - 1 - END

print(zeros)
assert zeros == ANSWER
