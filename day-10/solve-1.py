from functools import reduce
from typing import Tuple, Any
import itertools
# inp = [x.strip() for x in open("day-10/input1.txt").readlines()]
inp = [x.strip() for x in open("day-10/input1.txt").readlines()]

def press_btn(i: list[bool], b: list[int]) ->list[bool]:
    c = i.copy()

    for x in b:
        c[x] = True if c[x] == False else False
    return c
    

# def find_btns(i: list[bool], b: list[list[int]]) -> int:
#     for r in range(1, 100):
#         combs = list(itertools.combinations_with_replacement(b, r))
#         print(combs)

#         for c in combs:
#             _indicators = i.copy()
#             for btn in c:
#                 if all(_indicators):
#                     print("fant comb", c)
#                     return r
#                 _indicators = press_btn(_indicators, btn)
#     exit(-1)

# find_btns([True, False, True], [[0, 1]])

t = 0
for _x in range(len(inp)):
    x = inp[_x]


    indicators = ""
    buttons = []

    s = x.split(" ")
    for x1 in s:
        if x1[0] == "[":
            indicators = x1[1:-1]
        elif x1[0] == "(":
            buttons.append(x1[1:-1])
        else:
            continue

    print(indicators)
    print(buttons)
    print("---------")
    indicators = [True if x1 == "." else False for x1 in indicators]
    buttons = [[int(x2) for x2 in x1.split(",")] for x1 in buttons]

    # print(indicators)
    # print(buttons)
    # print("---------")

    # just try 1 press, 2 press etc:
    found = False

    for r in range(1, 20):
        if found:
            break
        combs = list(itertools.combinations_with_replacement(buttons, r))
        print("alle combs med lengde ", r, combs)

        for c in combs:
            print("prøver comb: ", c)
            print("-------------")
            if found:
                break
            _indicators = indicators.copy()
            for btn in c:
                if found:
                    break
                _indicators2 = press_btn(_indicators, btn)
                # print("før: ", _indicators, "med: ", btn, "etter", _indicators2)
                if all(_indicators2):
                    print("fant comb", c, " r: ", r)
                    found = True
                    t+=r
                _indicators = _indicators2

        
print(t)






