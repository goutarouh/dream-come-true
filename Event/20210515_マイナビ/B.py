N = int(input())

l = []
for i in range(N):
    mountInfo = input().split()
    mountInfo[1] = int(mountInfo[1])
    l.append(mountInfo)
    l.sort(key=lambda x: x[1], reverse=True)
    l = l[:2]
print(l[1][0])
