from functools import reduce
from typing import Tuple
inp = [x.strip() for x in open("day-6/input1.txt").readlines()]

print("leny", len(inp))
print("lenx", len(inp[0]))

# https://stackoverflow.com/a/68188419
def matrix_turn_90(m: list[list[int]]):
    # return [[x[i] for x in m] for i in range(len(m))][::-1]
    return list(list(x) for x in zip(*m))[::-1]


def splitweird(s: str) -> list[str]:
    o: list[str] = []
    g: list[str] = []
    for x in s:
        if x == " " or x == "\t":
            if len(g) != 0:
                o.append("".join(g))
                g = []
            continue
        g.append(x)
    if len(g) != 0:
        o.append("".join(g))
    return o

ops = splitweird(inp[-1])
print("ops", ops)
nums: list[list[int]] = []
# for x in range(len(inp)-1):
#     for x1 in range(len(ops)):
#         nums[x1].append(inp[x][x1])

for x in range(len(inp)-1):
    nums.append([int(x) for x in splitweird(inp[x])])

print("nums", nums)
nums = matrix_turn_90(nums)
print(nums)
nums.reverse()

groups: list[Tuple[str, list[int]]] = [(ops[x], nums[x]) for x in range(len(inp[:-1]))]

def eq(nums: list[int], op: str) -> int:
    r = 0
    if op == "*":
        r = reduce(lambda x, y: x * y, nums, 1)
    elif op == "+":
        r = reduce(lambda x, y: x + y, nums, 1)
    elif op == "-":
        raise Exception("what -")
    elif op == "/":
        raise Exception("what /")
    else:
        raise Exception("what" + op)

    print("eq", nums, op, r)
    return r



t = sum([eq(x[1],x[0]) for x in groups])
print(t)