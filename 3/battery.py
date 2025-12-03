from itertools import permutations


IN = """987654321111111
811111111111119
234234234234278
818181911112111"""

IN = open("input.txt").read()

banks = (x.strip() for x in IN.strip().splitlines())

joltage = 0

for bank in banks:
  batteries = [b for b in bank]
  max_joltage = 0
  for i, b in enumerate(batteries):
    for b2 in batteries[i+1:]:
      on = int(b+b2)
      # print(on)
      max_joltage = max(max_joltage, on)
  # joltage = max(int(a+b) for a,b in pairs)
  print(max_joltage)
  joltage += max_joltage

print(joltage)
