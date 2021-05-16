S = input()

ans = 0
for i in range(10000):
    x = i
    z = [False] * 10
    for j in range(0, 4):
        index = x % 10
        x //= 10
        z[index] = True
    flag = True
    for j in range(0, 10):
        if S[j] == "o" and not z[j]:
            flag = False
        if S[j] == "x" and z[j]:
            flag = False
    ans += flag
print(ans)
