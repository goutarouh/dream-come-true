from sys import stdin

N = int(stdin.readline().rstrip())

A = list(map(lambda x: x % 200, map(int, stdin.readline().rstrip().split())))


def intToS(bit):
    S = []
    for i in range(N):
        if bit & 1 << i:
            S.append(i)
    return S


seen = [[] for _ in range(200)]
for bit in range(1 << N):
    S = intToS(bit)
    ans = sum([A[i] for i in S]) % 200

    if seen[ans]:
        print("Yes")
        print(len(seen[ans]), *[x + 1 for x in seen[ans]], sep=" ")
        print(len(S), *[x + 1 for x in S], sep=" ")
        exit()

    seen[ans] = S
print("No")