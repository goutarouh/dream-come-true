from sys import stdin

# stdin = open("t.txt")

# N, D, H = list(map(int, stdin.readline().rstrip().split()))
# d = []
# h = []
# for i in range(N):
#     di, hi = list(map(int, stdin.readline().rstrip().split()))
#     d.append(di)
#     h.append(hi)


# min = 0
# for i in range(N):
#     sch = H - ((H - h[i]) / (D - d[i])) * D
#     if sch > min:
#         min = sch
# print(min)


N, D, H = map(int, input().split())
dh = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for d, h in dh:
    y = h - (H - h) / (D - d) * d
    ans = max(ans, y)
print(ans)