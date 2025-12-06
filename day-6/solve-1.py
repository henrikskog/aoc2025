inp = [x.strip() for x in open("day-5/input1.txt").readlines()]

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

# print("opt")
# x = 0
# while x < len(r)-1:
#     if r[x+1][0] <= r[x][1]:
#         # print("overlap", r[x], r[x+1])
#         # print(r)
#         n = [r[x][0], r[x+1][1]]
#         # print(n)
#         r.insert(x+2, n)
#         # print(r)
#         r.pop(x)
#         # print(r)
#         r.pop(x)
#         # print(r)
#     x+=1


t = 0
for x in range(fi, len(inp)):
    val = int(inp[x].strip())
    # print(val)
    fresh = False

    for ran in r:
        # print(val, ran[0], ran[1])
        if val >= ran[0] and val <= ran[1]:
            # print("fresh")
            fresh = True
            break

    if fresh:
        t += 1

        
print(t)


