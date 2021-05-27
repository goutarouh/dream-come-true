import collections

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

m = {i: 0 for i in range(1, N + 1)}

# Counter
# cc = collections.Counter(A)

# dict
# keyがない場合は初期化が必要
# その後の参照でもkeyがない場合は要処理
# dd = {}
# for a in A:
#     if a not in dd:
#         dd[a] = 0
#     dd[a] += 1

# print(dd)


dd = collections.defaultdict(lambda: 0)
for a in A:
    dd[a] += 1


ans = 0

for c in C:
    b = B[c - 1]
    ans += dd[b]


print(ans)