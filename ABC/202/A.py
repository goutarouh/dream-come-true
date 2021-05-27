a, b, c = map(int, input().rstrip().split())

m = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}

print(m[a] + m[b] + m[c])
