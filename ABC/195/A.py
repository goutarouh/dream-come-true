A, B, W = map(int, input().split())

W = 1000 * W

mn = float("INF")
mx = -1
for i in range(1, 10 ** 6 + 100):
    l = A * i
    r = B * i
    if l <= W <= r:
        print(i, l, r)
        mn = min(mn, i)
        mx = max(mx, i)

if mx == -1:
    print("UNSATISFIABLE")
else:
    print(mn, mx)
