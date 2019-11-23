import math
a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b != 0:
        if c == 0:
            print("x =",0)

        else:
            print("x = ",-c/b)
else:
    delta = float(b*b - 4*a*c)
    if delta < 0:
        print("no root")
    elif delta == 0:
        print("x = ",-b/(2*a))
    else:
        print("x1 =",(-b + math.sqrt(delta))/(2*a), "x2 =",(-b -math.sqrt(delta))/(2*a))
