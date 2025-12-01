inp = [x.strip() for x in open("input2.txt").readlines()]

start = 50
curr = 50
num_0 = 0

example = [x.strip() for x in """L68
L30
R1048
L5
R60
L55
L1
L99
R14
L82""".split("\n")]

for line in example:
    prev_curr = curr
    d = line[0]
    # print(line)
    d2 = int(line[1:]) if d == "R" else -int(line[1:])
    # print("d2", d2)
    
    curr += d2
    # print("mid", curr)

    if curr < 0:
        curr = 100 - abs(int(str(curr)[-2:]))
    if curr == 100:
        curr = 0
    if curr > 100:
        curr = int(str(curr)[-2:])

    # print("point", curr)


   # task 2:

    # startet på prev_curr
    # flyttet oss d2
    # endte på curr

    # hvis d2 < 0 && abs(d2) > curr -> gått forbi 0
    # hvis d2 > 0 && d2 > (curr-100) > curr -> gått forbi 0

    print(f"{prev_curr} + {d2}({line}) = {curr}")

    if d2 < 0 and abs(d2) > prev_curr and (prev_curr != 0 or (-d2 > 100)):
        num_times = 1 if abs(d2) < 100 else abs(d2) // 100
        print(f"passed 0 {num_times} times")
        num_0+=num_times

    elif d2 > 0 and d2 > (100-prev_curr) and (prev_curr != 0 or (d2 > 100)):
        num_times = 1 if abs(d2) < 100 else abs(d2) // 100
        print(f"passed 0 {num_times} times")
        num_0+=num_times

    else:
        print("passed 0 0 times")


    if curr == 0:
        num_0+=1
        print("at 0: yes")
    else:
        print("at 0: no")

    print("num 0s: ", num_0)
    print()




print(num_0)