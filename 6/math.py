from collections import defaultdict
import re
from itertools import chain
from itertools import zip_longest


IN = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +  """

IN = open('input.txt').read()

problems = defaultdict(list)

regex = re.compile(r'\s+')

total = 0

for line in IN.splitlines():
  for x, col in enumerate(regex.split(line.strip())):
    problems[x].append(col)

for problem in problems.values():
  numbers, sign = problem[:-1], problem[-1]

  total += eval("".join(chain.from_iterable(zip_longest(numbers, [sign] * (len(numbers)-1), fillvalue=''))))
print(total)
