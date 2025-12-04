
lines = [[a for a in x.strip()] for x in open("day-4/input2.txt").readlines()]

def pm(m: list[list[str]]):
    for _y in m:
        print("".join(_y))

pm(lines)

def get_value(m: list[list[str]], y: int, x: int) -> (str):
    if x < 0 or x > len(m[0])-1 or y < 0 or y > len(m) -1:
        return "x"

    return m[y][x]

def get_block(m: list[list[str]], y: int, x: int) -> list[list[str]]:
    res = [["x" for _x in range(3)] for _y in range(3) ]
    for _y in range(3):
        for _x in range(3):
            res[_y][_x]=get_value(m, y+_y, x+_x)

    return res

def flatten_block(m: list[list[str]]) -> str:
    res = ""
    for y in m:
        res += "".join(y)
    return res

def num_in_block(m: list[list[str]], symb: str) -> int:
    res = 0
    for y in m:
        for x in y:
            if x == symb:
                res+=1
    
    return res



tot = 0
while True:
    to_remove: list[list[int]] = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "@":
                num_rolls = num_in_block(get_block(lines, y-1, x-1), "@")
                if num_rolls < 4 + 1: # + 1 is itself
                    to_remove.append([y, x])
                    print(to_remove)
    if len(to_remove) == 0:
        print(tot)
        break

    tot+=len(to_remove)
    for c in to_remove:
        y = c[0]
        x = c[1]
        lines[y][x] = "x"

print(tot)
