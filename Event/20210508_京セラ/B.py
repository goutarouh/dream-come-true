from sys import stdin

N, K = map(int, stdin.readline().rstrip().split())

for i in range(K):
    if N % 200 == 0:
        N /= 200
        N = int(N)
    else:
        N = int(str(N) + "200")

print(N)