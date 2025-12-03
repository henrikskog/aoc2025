i = [x.strip() for x in open("day-3/input1.txt").readlines()]

def pos(a: set, i: int) -> int:
    for x in range(len(a)):
        if x == i:
            return x
    return -1

def jolt(line: str) -> int:
    s = set([int(x) for x in set(list(line))])
    c = s.copy()

    a = max(s)
    s.remove(a)
    b = max(s)

    if pos(c, a) < pos(c, b):
        return int(str(a) + str(b))

    return int(str(b) + str(a))


t = 0
for x in i:
    # print(x, jolt(x))
    t += jolt(x)
print(t)


