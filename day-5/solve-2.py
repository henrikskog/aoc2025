inp = [x.strip() for x in open("day-5/input1.txt").readlines()] # same input part 2

r: list[list[int]] = []

print(inp)

fi = 0

for _x in range(len(inp)):
    x = inp[_x]
    if x == '':
        fi = _x+1
        break
    _a = x.split("-")
    f = int(_a[0])
    t = int(_a[1])

    r.append([f, t])


print(r)
r = sorted(r, key=lambda x: x[0])
print(r)

def overlap(r1: list[int], r2: list[int]):
    if (r2[0] > r1[1] and r2[1] > r1[1]) or (r1[0] > r2[1] and r1[1]> r2[1]):
        return False
    return True

print("opt")
x = 0
while x < len(r)-1:
    while True:
            if x == len(r) - 1:
                break
            elif overlap(r[x], r[x+1]):
                # print("overlap", r[x], r[x+1])
                # print(r)
                n = [r[x][0], max(r[x][1], r[x+1][1])]
                # print(n)
                r.insert(x+2, n)
                # print(r)
                r.pop(x)
                # print(r)
                r.pop(x)
                # print(r)
            else:
                break
    x+=1
    print("x", x)


t = 0
for x in r:
    t += x[1] - x[0]+1
        
print(t)


