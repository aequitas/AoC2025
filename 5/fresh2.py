from collections import defaultdict
from email.policy import default
import json


IN = """3-5
12-18
10-14
16-20


1
5
8
11
17
32"""

IN = open("input.txt").read()

# IN = """1-3
# 5-7
# 9-12
# 2-10

# """

ranges = []
total = 0

for i in IN.splitlines():
  if '-' in i:
    b,e = [int(x) for x in i.split("-")]
    ranges.append([b,e])

done = 0
while not done:
  # print(ranges)
  ranges = sorted(ranges, key=lambda x:x[0])
  for r in ranges:
    b,e = r
    print(b,e)
    assert b <= e

    for r2 in ranges:
      if id(r2) == id(r):
        continue
      b2,e2 = r2
      # print(b,e,rb,re)
      # skip if falls within existing range
      if b >= b2 and e <= e2:
        print(f'drop range {r} within existing {r2}')
        ranges.remove(r)
        break

      if b >= b2 and b <= e2:
        print(f'expand end of {r2} to {e} for {r}')
        r2[1] = e
        break

      # if e >= b2 and e <= e2:
      #   print(f' shrink end to {b2-1} for {r2}')
      #   r[1] = b2-1
      #   break

    else:
      continue
    break
  else:
    done = True
  # elif i == '':
  #   break

print(ranges)


for b,e in ranges:
  # print(list(range(b,e+1)))
  total += e+1-b
  # print(total)

print(total)

assert total != 336611060989785
assert total != 340988828813600
assert total < 341054274206802
assert total > 324492590341666
assert total != 338074180439099
