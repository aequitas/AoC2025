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

ranges = defaultdict(dict)
fresh = 0
total = 0

def mktree(x, r):
  # print(x,r, ranges)
  r[int(x[0])] = r.get(int(x[0]), {})

  if len(x) == 1:
    r[int(x)][-1] = True
  else:
    mktree(x[1:], r[int(x[0])])

def lookup(x, r):
  if len(x) == 1:
    return r.get(int(x), {}).get(-1, False)
  else:
    return lookup(x[1:], r[int(x[0])])


for i in IN.splitlines():
  if '-' in i:
    s,e = i.split("-")
    for x in range(int(s), int(e)+1):
      mktree(str(x), ranges)
  elif i == '':
    # print(json.dumps(ranges, indent=2))
    continue
  else:
    if lookup(i,ranges):
      total += 1
print(total)
    # for r in ranges:
  #     # print(i, r)
  #     if int(i) in r:
  #       fresh += 1
  #       print(i)
  #       break
