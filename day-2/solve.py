example = ".".join(open("input2.txt").readlines()).split(",")


def invalidId(s: str) -> bool:
    for s1 in range(1, len(s)):
        ss = s[0:s1]
        spl = s.split(ss)
        print(f"{ss}+{spl}")
        if all([a == "" for a in spl]):
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

# print(invalidId("12"))
main()