from sys import stdin
import collections
import math


def div2(n):
    return n % 200


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


N = int(stdin.readline().rstrip())

A = list(map(div2, map(int, stdin.readline().rstrip().split())))

ans = 0
found = []
c = collections.Counter(A)
for i in range(N):
    count = c[A[i]]
    if count <= 1:
        continue
    if A[i] in found:
        continue
    found.append(A[i])
    f = combinations_count(count, 2)
    ans += f

print(ans)