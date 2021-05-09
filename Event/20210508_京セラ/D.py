from sys import stdin


def div2(n):
    return n % 200


N = int(stdin.readline().rstrip())

A = list(map(div2, map(int, stdin.readline().rstrip().split())))

A = sorted(set(A), key=A.index)


print(A)