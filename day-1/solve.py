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
    prev_curr = c 
    d = l[0]
    # print(line)
    d2 = int(l[1:]) if d == "R" else -int(l[1:])
    # print("d2", d2)
    
    c += d2
    # print("mid", c)

    c = c % 100 

    # print("point", c)

   # task 2:

    # startet på prev_curr
    # flyttet oss d2
    # endte på c

    # hvis d2 < 0 && abs(d2) > c -> gått forbi 0
    # hvis d2 > 0 && d2 > (c-100) > c -> gått forbi 0

    print(f"{prev_curr} + {d2}({l}) = {c}")

    if d2 < 0:
        first_k = 100 if prev_curr == 0 else prev_curr
        if first_k <= abs(d2):
            num_times = 1 + (abs(d2) - first_k) // 100
            print(f"passed 0 {num_times} times")
            t += num_times
        else:
            print("passed 0 0 times")

    elif d2 > 0:
        first_k = 100 if prev_curr == 0 else 100 - prev_curr
        if first_k <= d2:
            num_times = 1 + (d2 - first_k) // 100
            print(f"passed 0 {num_times} times")
            t += num_times
        else:
            print("passed 0 0 times")

    else:
        print("passed 0 0 times")

    print("num 0s: ", t)
    print()

    return (c, t)


total = 0
for line in inp:
    (curr, total) = a(curr, line[0], total, line) 

print(total)
