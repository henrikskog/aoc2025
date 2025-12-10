from functools import reduce
from typing import Tuple, Any
inp = [x.strip() for x in open("day-10/example.txt").readlines()]

print("leny", len(inp))
print("lenx", len(inp[0]))

# https://stackoverflow.com/a/68188419
def matrix_turn_90(m: list[list[Any]]):
    # return [[x[i] for x in m] for i in range(len(m))][::-1]
    return list(list(x) for x in zip(*m))[::-1]

inpb = [[x1 for x1 in x] for x in inp[:-1]]

for x in inpb:
    print(x)

print("----")
a = matrix_turn_90(inpb)
for x in a:
    print(x)
exit(1)

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
# print("ops", ops)
nums: list[list[int]] = []
# for x in range(len(inp)-1):
#     for x1 in range(len(ops)):
#         nums[x1].append(inp[x][x1])

for x in range(len(inp)-1):
    nums.append([int(x) for x in splitweird(inp[x])])

# print("nums", nums)
nums = matrix_turn_90(nums)
nums.reverse()
print(nums)

weird_nums = []

t = 0
for x in range(len(nums)):
    r = []
    ind_nums = nums[x]

    longest = max([len(str(x1)) for x1 in ind_nums])


    ind_nums_str: list[list[str]] = []
    for x1 in range(len(ind_nums)):
        # if len(str(ind_nums[x1])) < longest:
        n = [str(x2) for x2 in str(ind_nums[x1])] + [" " for x in range(longest-len(str(ind_nums[x1])))]
        ind_nums_str.append(n)

    for x1 in ind_nums_str:
        print(x1)

    rot = matrix_turn_90(ind_nums_str)

    print(rot)
    fi = [int("".join(x1).strip()) for x1 in rot]
    print(fi)

    print("----")

    # for x1 in range(longest):
    #     for x2 in range(len(inp)-1):
    #         n = ind_nums[x1]
    #         if len(str())
    #         r.append(ind_nums[x2][longest-x1])






groups: list[Tuple[str, list[int]]] = [(ops[x], nums[x]) for x in range(len(ops))]

def eq(nums: list[int], op: str) -> int:
    r = 0
    if op == "*":
        r = reduce(lambda x, y: x * y, nums, 1)
    elif op == "+":
        r = reduce(lambda x, y: x + y, nums, 0)
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