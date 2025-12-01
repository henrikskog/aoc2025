inp = [x.strip() for x in open("input2.txt").readlines()]

start = 50
curr = 50
num_0 = 0

example = [x.strip() for x in """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".split("\n")]

def a(c, d, t, l):
    prev_curr = curr
    d = line[0]
    # print(line)
    d2 = int(line[1:]) if d == "R" else -int(line[1:])
    # print("d2", d2)
    
    c += d2
    # print("mid", c)

    if c < 0:
        c = 100 - abs(int(str(c)[-2:]))
    if c == 100:
        c = 0
    if c > 100:
        c = int(str(c)[-2:])

    # print("point", c)

   # task 2:

    # startet på prev_curr
    # flyttet oss d2
    # endte på c

    # hvis d2 < 0 && abs(d2) > c -> gått forbi 0
    # hvis d2 > 0 && d2 > (c-100) > c -> gått forbi 0

    print(f"{prev_curr} + {d2}({line}) = {c}")

    if d2 < 0 and abs(d2) > prev_curr and (prev_curr != 0 or (-d2 > 100)):
        num_times = 1 if abs(d2) < 100 else abs(d2) // 100
        print(f"passed 0 {num_times} times")
        t+=num_times

    elif d2 > 0 and d2 > (100-prev_curr) and (prev_curr != 0 or (d2 > 100)):
        num_times = 1 if abs(d2) < 100 else abs(d2) // 100
        print(f"passed 0 {num_times} times")
        t+=num_times

    else:
        print("passed 0 0 times")


    if c == 0:
        t+=1
        print("at 0: yes")
    else:
        print("at 0: no")

    print("num 0s: ", t)
    print()

    return (c, t)


total = 0
for line in example:
    (curr, t) = a(curr, line[0], total, line)
    total += t

print(total)