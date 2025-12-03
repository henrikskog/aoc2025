inp = [x.strip() for x in open("day-3/example.txt").readlines()]

def pos(a: set, i: int) -> int:
    for x in range(len(a)):
        if x == i:
            return x
    return -1

def largest(l: list[int]) -> int:
    b = -1
    i = 0
    for x in range(len(l)):
        n = l[x]
        if n > b:
            b = n
            i = x
    return i

# def next_biggest

def jolt(s: list[int]) -> int:
    return 0
    for x in range(12):

        b = max(s[0:len(s)-1])
        print(b)


        fi = -1
        for i in range(len(s)-1):
            if s[i] == b:
                print(s[i], i, b)
                fi = i
                break

        assert(fi != -1)

        # sb = set(s[])
        # sb.remove(b)
        nb = max(s[fi+1:])

        print(nb)

        si = -1
        for i in range(fi+1, len(s)):
            if s[i] == nb:
                print(s[i], i, nb)
                si = i

            
        assert(si != -1)

        r = int(str(b) + str(nb))

        # latest is the biggest
        last = s[-1]
        if last > r:
            return last

        return r

t = 0
num = 12
for _s in inp:
    print(_s)
    s = [int(x) for x in _s]
    r = []
    ci = 0
    for x in range(num):
        b = largest(s[ci+1:len(s)-num]) + ci
        r.append(s[b])
        print(b, r)
        ci=b

    print(r)
    r = int("".join([str(x) for x in r]))


    last = int("".join([str(x) for x in s[len(s)-num:]]))

    if last > r:
        print(last)
        t+=last
    print(r)
    t+=r

# print(len("3232221546315133223433433342253232332422524653333335332433322333355343313233335255322525232232347253"))
# t = 0
# for x in i:
#     l = [int(a) for a in x]
#     print(x)
#     j = jolt(l)
#     print(x, j)
#     t += j
# print(t)

