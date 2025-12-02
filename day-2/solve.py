example = ".".join(open("input1.txt").readlines()).split(",")


def invalidId(s: str) -> bool:
    return s[0:len(s)//2] == s[len(s)//2:]

def invalidIdsInRange(a: int, b: int) -> int:
    t=0 
    for x1 in range(int(a), int(b)+1):
        print(x1)
        if invalidId(str(x1)):
            print("invalid")
            t+=x1
    return t


print(example)

t = 0
for x in example:
    [a, b] = x.split("-")
    print(a,b)
    t += invalidIdsInRange(int(a),int(b))


print(t)