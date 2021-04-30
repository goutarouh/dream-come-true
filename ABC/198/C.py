import math

R, X, Y = list(map(int, input().split()))


dist = math.sqrt(X * X + Y * Y)

if dist < R:
    print(math.ceil((dist / R)) + 1)
else:
    print(math.ceil((dist / R)))