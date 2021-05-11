from sys import stdin
import itertools

# stdin = open("t.txt")

N = int(stdin.readline().rstrip())
# P = [list(map(int, stdin.readline().rstrip().split(" "))) for _ in range(N)]
P = [tuple(map(int, input().split())) for i in range(N)]

# teamMax = 0
# for i in itertools.combinations(P, 3):
#     print(i)
#     maxA = max(i[0][0], i[1][0], i[2][0])
#     maxB = max(i[0][1], i[1][1], i[2][1])
#     maxC = max(i[0][2], i[1][2], i[2][2])
#     maxD = max(i[0][3], i[1][3], i[2][3])
#     maxE = max(i[0][4], i[1][4], i[2][4])
#     tm = min(maxA, maxB, maxC, maxD, maxE)
#     if tm > teamMax:
#         teamMax = tm
# print(teamMax)

## theirs ##
# 最小値の最大化 -> 二分探索

ok = 0
ng = 10 ** 9 + 1


def check(x):
    s = set()
    for p in P:
        s.add(sum(1 << i for i in range(5) if p[i] >= x))
    for x in s:
        for y in s:
            for z in s:
                if x | y | z == 31:
                    return True
    return False


ok = 0
ng = 10 ** 9 + 1
while ng - ok > 1:
    cen = (ok + ng) // 2
    if check(cen):
        ok = cen
    else:
        ng = cen
print(ok)
