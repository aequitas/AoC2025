from collections import defaultdict
from email.policy import default
import json


IN = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

IN = open("input.txt").read()

ranges = []
fresh = []
total = 0

for i in IN.splitlines():
  if '-' in i:
    ranges.append([int(x) for x in i.split("-")])
  elif i == '':
    continue
  else:
    fresh.append(i)

# print(ranges, fresh)

for f in fresh:
  f = int(f)
  for b,e in ranges:
    # print(b,f,e)
    if f > b and f <= e:
      total += 1
      break

print(total)
