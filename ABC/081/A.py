########## mine ##########
S = input()
ans = 0
for si in S:
    if si == "1":
        ans += 1
print(ans)

######### theirs ##########
s = input()
cnt = 0
for i in range(3):
    if s[i] == "1":
        cnt += 1
print(cnt)

######### theirs ##########
print(sum(list(map(int, list(input())))))