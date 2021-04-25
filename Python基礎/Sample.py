from sys import stdin

# 一行読み込み
a = stdin.readline().rstrip()
print(a.upper())

# 数値変換
n = int(stdin.readline().rstrip())
print(n)

# リストで読みこみ
l = stdin.readline().rstrip().split()
A, B, C = stdin.readline().rstrip().split()
print(l)
print(A, B, C)

# 内包表記で読み込み
A, B, C, D, E, F, G = [int(x) for x in stdin.readline().split()]
print(A, B, C, D, E, F, G)

# 絞り込み
data = range(1, 10)
count = len([x for x in data if x % 3 == 0])
print(count)

# 複数行まとめてstdin
num = int(stdin.readline().rstrip())
print(num)
data = [stdin.readline().rstrip().split() for _ in range(num)]
print(data)
