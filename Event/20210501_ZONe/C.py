from sys import stdin
import itertools

# stdin = open("t.txt")

N = int(stdin.readline().rstrip())
P = [list(map(int, stdin.readline().rstrip().split(" "))) for _ in range(N)]

teamMax = 0
for i in itertools.combinations(P, 3):
    print(i)
    maxA = max(i[0][0], i[1][0], i[2][0])
    maxB = max(i[0][1], i[1][1], i[2][1])
    maxC = max(i[0][2], i[1][2], i[2][2])
    maxD = max(i[0][3], i[1][3], i[2][3])
    maxE = max(i[0][4], i[1][4], i[2][4])
    tm = min(maxA, maxB, maxC, maxD, maxE)
    if tm > teamMax:
        teamMax = tm
print(teamMax)

## theirs ##
# 最小値の最大化 -> 二分探索
