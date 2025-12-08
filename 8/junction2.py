from collections import defaultdict
from itertools import combinations, permutations, product
import json
from math import sqrt
import math
from typing import DefaultDict
from pprint import pprint
from typing_extensions import Counter


IN = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

COUNT = 10

IN = open("input.txt").read()
COUNT = 1000

boxes = [tuple(map(int, b.split(","))) for b in IN.splitlines()]

pairs = []

circuits = dict()

# print(boxes)
# print(len(list(combinations(boxes, 2))))

# print(len(boxes))

for box1, box2 in combinations(boxes, 2):
  distance = math.sqrt((box1[0]-box2[0])**2 + (box1[1]-box2[1])**2 + (box1[2]-box2[2])**2)
  pairs.append((distance, box1, box2))

count = 0
for _, box1,box2 in sorted(pairs, key=lambda x:x[0]):
  print(box1, circuits.get(box1),box2, circuits.get(box2))
  if circuits.get(box1) and circuits.get(box2) and circuits.get(box1) == circuits.get(box2):
    print(f"{box1=} and {box2=} already connected on {circuits[box1]}")
    continue
  # circuit = len(set(circuits.values()))
  if box1 in circuits and box2 in circuits:
    circuit = circuits[box2]
    print(f"merging circuits {circuits[box1]} and {circuits[box2]} to {circuit}")
    match = (circuits[box1], circuits[box2])
    for box,c in circuits.items():
      # print(match)
      if c in match:
        circuits[box] = circuit
  elif box1 in circuits:
    circuit = circuits[box1]
  elif box2 in circuits:
    circuit = circuits[box2]
  else:
    circuit = max(circuits.values() or [0])+1

  if box1 not in circuits:
    print(f'added {box1=} to circuit {circuit}')
    circuits[box1] = circuit
  if box2 not in circuits:
    print(f'added {box2=} to circuit {circuit}')
    circuits[box2] = circuit

  if len(circuits.keys()) == len(boxes):
    print(box1[0] *box2[0])
    break

# # pprint(sorted(circuits.items(), key=lambda x: x[1]))
# c = Counter(circuits.values())
# for i in range(max(circuits.values())+1, max(circuits.values())+1+len([box for box in boxes if box not in circuits])):
#   # print(i)
#   c[i] = 1
# # print(c)
# counts = sorted(c.values(), reverse=True)
# print(counts, len(counts))
# print(len(counts))

# # size = counts[0]*counts[1]*counts[2]
# print(size)
# assert size > 19800
# assert size > 30276
# assert size == 133574
