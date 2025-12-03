from itertools import permutations


IN = """987654321111111
811111111111119
234234234234278
818181911112111"""

IN = open("input.txt").read()

banks = [x.strip() for x in IN.strip().splitlines()]

joltage = 0

S = len(banks[0])

for bank in banks:
  batteries = [int(b) for b in bank]
  print(batteries)
  index = 0
  next = 0
  max_joltage = ""
  for i in range(12):
    print(f"{i=}, {index=}, {next=}")
    b = batteries[next:S-(11-i)]
    print(b)
    m = max(b)
    max_joltage += str(m)
    index = next + batteries[next:].index(m)
    next = index+1
    print(f"{index=}, {next=}, {m=}, ")
  print(f"{max_joltage=}")
  joltage += int(max_joltage)
  print()

print(joltage)
