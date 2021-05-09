from sys import stdin

# stdin = open("t.txt")

N = stdin.readline().rstrip()

print(N.count("ZONe"))


### theirs ###

# s.substr(開始, 長さ)
ans = 0
for i in range(len(N) - 3):
    if N[i : i + 4] == "ZONe":
        ans += 1
print(ans)