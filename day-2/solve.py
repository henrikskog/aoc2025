example = ".".join(open("example1.txt").readlines()).split(",")


def invalidId(s: str) -> bool:
    return len(set(list(s))) != len(list(s))
    t = 0
    for s1 in range(len(s)):
        for s2 in range(len(s)):
            if s[s1] == s[s2]:
                t+=1
    if t > 1:
        return True
    return False
        
def invalidIdsInRange(a: int, b: int) -> int:
    t=0 
    for x1 in range(int(a), int(b)+1):
        print(x1)
        if invalidId(str(x1)):
            print("invalid")
            t+=x1
    return t


def main():
    t = 0
    for x in example:
        [a, b] = x.split("-")
        print(a,b)
        t += invalidIdsInRange(int(a),int(b))
    print(t)

main()