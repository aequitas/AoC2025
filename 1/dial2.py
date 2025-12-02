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

START_POS = 50

ANSWER = 6

def run(moves, pos):
  moves = moves.strip().splitlines()

  zeros = 0

  for move in moves:
    move = move.strip()
    d,n = move[0], int(move[1:])
    print(pos, zeros, d, n)

    if d == 'L':
      if pos != 0 and pos - (n % 100) <= 0:
        zeros += 1

      zeros += n // 100

      pos -= n % 100
      if pos < 0:
        pos = 100 + pos

    elif d == 'R':
      if pos != 0 and pos + (n % 100) > 99:
        zeros += 1

      zeros += n // 100

      # zeros += n // 100
      pos += n % 100
      if pos >= 100:
        pos = pos % 100
    else:
      raise

  return zeros

zeros = run(IN, START_POS)
print(zeros)
assert zeros == ANSWER
print()

zeros = run("""
L25
R73
"""
, 25)
print(zeros )
assert zeros == 1

IN = open("input.txt").read()
zeros = run(IN, START_POS)
print(zeros)
assert zeros == ANSWER
print()

# def test_100():

# 5971
# 5993
