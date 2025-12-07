from collections import defaultdict
import json
import re
from itertools import chain
from itertools import zip_longest


IN = (
"123 328  51 64 \n"
" 45 64  387 23 \n"
"  6 98  215 314\n"
"*   +   *   +  \n")

IN = open('input.txt').read()

problems = defaultdict(lambda: defaultdict(str))

regex = re.compile(r'\ (?=[^\ ])')

total = 0

widths = [len(x) for x in regex.split(IN.splitlines()[-1])]
# print(widths)

for col in IN.splitlines():
  print(f"{col=}")
  pos = 0
  for x, width in enumerate(widths):
    num =  col[pos:pos+width]
    print(f"{x=} {pos=:3} {num=:3} {width=}")
    pos += width +1
    for y, v in enumerate(num):
      if v.strip() in ('+', '*'):
        problems[x][-1] = v.strip()
      else:
        problems[x][y] += v
      # print(x,y, v)

print(json.dumps(problems,indent=2))

for problem in problems.values():
  print(problem)
  sign = problem.pop(-1)
  numbers = problem.values()
  # print(sign, numbers)
  sum = eval("".join(chain.from_iterable(zip_longest(numbers, [sign] * (len(numbers)-1), fillvalue=''))))
  print(sum)
  total += sum
print(total)
