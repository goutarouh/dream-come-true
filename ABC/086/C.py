from sys import stdin

# stdin = open("../test.txt")

# N = int(stdin.readline())
# L = [list(map(int, stdin.readline().split(" "))) for _ in range(N)]
# L = [[0, 0, 0]] + L

# for i in range(0, N):
#     ok = False
#     dt = L[i + 1][0] - L[i][0]
#     dx = abs(L[i + 1][1] - L[i][1])
#     dy = abs(L[i + 1][2] - L[i][2])
#     dxy = dx + dy
#     if dxy <= dt * 1:
#         if dt % 2 == 0:
#             if dxy % 2 == 0:
#                 ok = True
#         else:
#             if dxy % 2 == 1:
#                 ok = True

#     if ok:
#         continue
#     else:
#         break

# if ok:
#     print("Yes")
# else:
#     print("No")


### theirs ###
N = int(input())
l = [[0, 0, 0]]
[l.append(list(map(int, input().split(" ")))) for _ in range(N)]

can = True
for i in range(0, N):
    dt = l[i + 1][0] - l[i][0]
    dist = abs(l[i + 1][1] - l[i][1]) + abs(l[i + 1][2] - l[i][2])
    if dt < dist:
        can = False
    if dist % 2 != dt % 2:
        can = False
    if not can:
        break

if can:
    print("Yes")
else:
    print("No")
